# pylint: skip-file

import unittest
from unittest.mock import MagicMock

from qaekwy.core.model.constraint.abs import ConstraintAbs
from qaekwy.core.model.modeller import Modeller
from qaekwy.core.model.specific import SpecificMinimum
from qaekwy.core.model.searcher import SearcherType
from qaekwy.core.model.cutoff import CutoffFibonacci
from qaekwy.core.model.variable.integer import IntegerVariable
from qaekwy.core.model.cutoff import Cutoff
from qaekwy.core.model.variable.variable import Expression
from qaekwy.core.exception.model_failure import ModelFailure


class TestModeller(unittest.TestCase):

    def setUp(self):
        self.modeller = Modeller()
        self.var1 = IntegerVariable("var1", 0, 10)
        self.var2 = IntegerVariable("var2", 0, 10)
        self.constraint = ConstraintAbs(
            var_1=self.var1, var_2=self.var2, constraint_name="abs"
        )
        self.objective = SpecificMinimum(self.var1)
        self.searcher = SearcherType.DFS
        self.cutoff = CutoffFibonacci()
        self.callback_url = "https://example.com/callback"

    def test_add_variable(self):
        self.modeller.add_variable(self.var1).add_variable(self.var2)
        self.assertEqual(self.modeller.variable_list, [self.var1, self.var2])

    def test_add_constraint(self):
        self.modeller.add_constraint(self.constraint)
        self.assertEqual(self.modeller.constraint_list, [self.constraint])

    def test_add_objective(self):
        self.modeller.add_objective(self.objective)
        self.assertEqual(self.modeller.objective_list, [self.objective])

    def test_set_searcher(self):
        self.modeller.set_searcher(self.searcher)
        self.assertEqual(self.modeller.searcher, self.searcher)

    def test_set_cutoff(self):
        self.modeller.set_cutoff(self.cutoff)
        self.assertEqual(self.modeller.cutoff, self.cutoff)

    def test_set_callback_url(self):
        self.modeller.set_callback_url(self.callback_url)
        self.assertEqual(self.modeller.callback_url, self.callback_url)

    def test_to_json(self):
        self.modeller.add_variable(self.var1).add_variable(self.var2).add_constraint(
            self.constraint
        ).add_objective(self.objective)
        self.modeller.set_searcher(self.searcher).set_cutoff(
            self.cutoff
        ).set_callback_url(self.callback_url)

        expected_json = {
            "callback_url": "https://example.com/callback",
            "constraint": [{"name": "abs", "type": "abs", "v1": "var1", "v2": "var2"}],
            "cutoff": {"name": "fibonacci"},
            "solution_limit": 1,
            "specific": [{"type": "minimize", "var": "var1"}],
            "var": [
                {
                    "brancher_value": "VAL_RND",
                    "branching_order": -1,
                    "domlow": 0,
                    "domup": 10,
                    "name": "var1",
                    "type": "integer",
                },
                {
                    "brancher_value": "VAL_RND",
                    "branching_order": -1,
                    "domlow": 0,
                    "domup": 10,
                    "name": "var2",
                    "type": "integer",
                },
            ],
        }

        print(
            self.modeller.from_json(
                self.modeller.from_json(expected_json).to_json(serialization=True)
            ).to_json(serialization=True)
        )

        self.assertDictEqual(
            self.modeller.to_json(serialization=True),
            self.modeller.from_json(expected_json).to_json(serialization=True),
            self.modeller.from_json(
                self.modeller.from_json(expected_json).to_json(serialization=True)
            ).to_json(serialization=True),
        )

        self.assertDictEqual(
            self.modeller.to_json(serialization=True),
            expected_json,
        )

class TestModellerBasic(unittest.TestCase):

    def test_add_variable(self):
        m = Modeller()
        v = MagicMock()

        result = m.add_variable(v)

        self.assertIs(result, m)
        self.assertIn(v, m.variable_list)

    def test_add_constraint_expression_wrapped(self):
        m = Modeller()
        expr = MagicMock(spec=Expression)

        m.add_constraint(expr)

        self.assertEqual(len(m.constraint_list), 1)
        self.assertNotEqual(m.constraint_list[0], expr)

class TestModellerToJson(unittest.TestCase):

    def setUp(self):
        self.m = Modeller()
        self.m.variable_list = []
        self.m.constraint_list = []
        self.m.objective_list = []

    def test_to_json_no_searcher_raises(self):
        with self.assertRaises(ModelFailure):
            self.m.to_json()

    def test_to_json_serialization_skips_searcher(self):
        json_data = self.m.to_json(serialization=True)
        self.assertNotIn("searcher", json_data)

    def test_to_json_with_searcher(self):
        self.m.set_searcher(SearcherType.DFS)

        json_data = self.m.to_json()
        self.assertEqual(json_data["searcher"], SearcherType.DFS.value)

    def test_to_json_meta_cutoff(self):
        cutoff = MagicMock(spec=Cutoff)
        cutoff.is_meta.return_value = True
        cutoff.to_json.return_value = {"t": 1}

        self.m.set_searcher(SearcherType.DFS)
        self.m.set_cutoff(cutoff)

        json_data = self.m.to_json()
        self.assertIn("meta_cutoff", json_data)

    def test_to_json_callback_url(self):
        self.m.set_searcher(SearcherType.DFS)
        self.m.set_callback_url("https://callback")

        json_data = self.m.to_json()
        self.assertEqual(json_data["callback_url"], "https://callback")

class TestConstraintFactory(unittest.TestCase):

    def test_unknown_constraint_type(self):
        with self.assertRaises(ValueError):
            Modeller._constraints_factory(
                {"type": "unknown"},
                []
            )

class TestModellerFromJsonExtras(unittest.TestCase):

    def test_solution_limit_default(self):
        m = Modeller.from_json({})
        self.assertEqual(m.solution_limit, 1)

    def test_solution_limit_custom(self):
        m = Modeller.from_json({"solution_limit": 5})
        self.assertEqual(m.solution_limit, 5)

    def test_cutoff_parsing(self):
        with unittest.mock.patch(
            "qaekwy.core.model.cutoff.Cutoff.from_json",
            return_value="cutoff"
        ):
            m = Modeller.from_json({"cutoff": {"x": 1}})

        self.assertEqual(m.cutoff, "cutoff")


class TestModellerFromJsonVariables(unittest.TestCase):

    def test_scalar_variable(self):
        json_data = {
            "var": [{"type": "integer", "name": "x", "brancher_value": "VAL_RND"}],
        }

        m = Modeller.from_json(json_data)
        self.assertEqual(len(m.variable_list), 1)

    def test_array_variable(self):
        json_data = {
            "var": [
                {
                    "type": "integer_array",
                    "name": "a",
                    "length": 5,
                    "brancher_variable": "VAR_RND",
                    "brancher_value": "VAL_RND"
                }
            ],
        }

        m = Modeller.from_json(json_data)
        self.assertEqual(len(m.variable_list), 1)

    def test_matrix_variable(self):
        json_data = {
            "var": [
                {
                    "type": "integer_array",
                    "subtype": "matrix",
                    "name": "m",
                    "cols": 2,
                    "rows": 3,
                    "brancher_variable": "VAR_RND",
                    "brancher_value": "VAL_RND"
                }
            ],
        }

        m = Modeller.from_json(json_data)
        self.assertEqual(len(m.variable_list), 1)


if __name__ == "__main__":
    unittest.main()
