# pylint: skip-file

import unittest

from qaekwy.model.modeller import Modeller
from qaekwy.model.constraint.if_then_else import ConstraintIfThenElse
from qaekwy.model.searcher import SearcherType
from qaekwy.model.variable.integer import IntegerVariable


class TestConstraintIfThenElse(unittest.TestCase):

    def setUp(self):
        self.modeller = Modeller()
        self.x = IntegerVariable("x", 0, 10)
        self.y = IntegerVariable("y", 0, 20)
        self.modeller.add_variable(self.x).add_variable(self.y)
        self.modeller.set_searcher(SearcherType.DFS)

    def test_if_then_decomposition(self):
        # IF x > 5 THEN y == 10
        self.modeller.add_constraint(
            ConstraintIfThenElse(
                condition=self.x > 5,
                then_constraint=self.y == 10,
            )
        )

        model_json = self.modeller.to_json()
        print(model_json)

        self.assertEqual(len(model_json["constraint"]), 1)
        constraint = model_json["constraint"][0]
        self.assertEqual(constraint["expr"], "((x) > (5)) & ((y) == (10))")
        self.assertEqual(constraint["type"], "rel")
        self.assertEqual(constraint["subtype"], "ite")
        self.assertEqual(constraint["ite_condition"], "((x) > (5))")
        self.assertEqual(constraint["ite_then"], "((y) == (10))")
        self.assertEqual(constraint["ite_else"], "None")
        self.assertEqual(constraint["varset"], "integer")

    def test_if_then_else_decomposition(self):
        # IF x > 5 THEN y == 10 ELSE y == 0
        self.modeller.add_constraint(
            ConstraintIfThenElse(
                condition=self.x > 5,
                then_constraint=self.y == 10,
                else_constraint=self.y == 0,
            )
        )

        model_json = self.modeller.to_json()
        print(model_json)

        self.assertEqual(len(model_json["var"]), 2)

        self.assertEqual(len(model_json["constraint"]), 1)
        constraint = model_json["constraint"][0]
        self.assertEqual(constraint["expr"], "(((x) > (5)) & ((y) == (10)) | !(((x) > (5))) & ((y) == (0)))")
        self.assertEqual(constraint["type"], "rel")
        self.assertEqual(constraint["subtype"], "ite")
        self.assertEqual(constraint["ite_condition"], "((x) > (5))")
        self.assertEqual(constraint["ite_then"], "((y) == (10))")
        self.assertEqual(constraint["ite_else"], "((y) == (0))")
        self.assertEqual(constraint["varset"], "integer")

    def test_from_json(self):
        json_data = {
            "name": "my_if_then_else",
            "type": "rel",
            "subtype": "ite",
            "expr": "(((x > 5) & (y == 10)) | ((~(x > 5)) & (y == 0)))",
            "ite_condition": "(x > 5)",
            "ite_then": "(y == 10)",
            "ite_else": "(y == 0)",
            "varset": "integer",
        }
        constraint = ConstraintIfThenElse.from_json(json_data)
        self.assertIsInstance(constraint, ConstraintIfThenElse)
        self.assertEqual(constraint.constraint_name, "my_if_then_else")
        self.assertEqual(str(constraint.condition), "(x > 5)")
        self.assertEqual(str(constraint.then_constraint), "(y == 10)")
        self.assertEqual(str(constraint.else_constraint), "(y == 0)")


if __name__ == "__main__":
    unittest.main()
