# pylint: skip-file

import unittest
from qaekwy.model.constraint.abs import ConstraintAbs
from qaekwy.model.modeller import Modeller
from qaekwy.model.specific import SpecificMinimum
from qaekwy.model.searcher import SearcherType
from qaekwy.model.cutoff import CutoffFibonacci
from qaekwy.model.variable.integer import IntegerVariable

class TestModeller(unittest.TestCase):

    def setUp(self):
        self.modeller = Modeller()
        self.var1 = IntegerVariable("var1", 0, 10)
        self.var2 = IntegerVariable("var2", 0, 10)
        self.constraint = ConstraintAbs(var_1=self.var1, var_2=self.var2, constraint_name="abs")
        self.objective = SpecificMinimum(self.var1)
        self.searcher = SearcherType.DFS
        self.cutoff = CutoffFibonacci()
        self.callback_url = "https://example.com/callback"

    def test_add_variable(self):
        self.modeller.add_variable(self.var1)
        self.assertEqual(self.modeller.variable_list, [self.var1])

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
        self.modeller.add_variable(self.var1).add_constraint(self.constraint).add_objective(self.objective)
        self.modeller.set_searcher(self.searcher).set_cutoff(self.cutoff).set_callback_url(self.callback_url)

        expected_json = {
            'callback_url': 'https://example.com/callback',
            'constraint': [
                {'name': 'abs', 'type': 'abs', 'v1': 'var1', 'v2': 'var2'}
            ],
            'cutoff': {'name': 'fibonacci'},
            'searcher': 'DFS',
            'solution_limit': 1,
            'specific': [{'type': 'minimize', 'var': 'var1'}],
            'var': [
                {'brancher_value': 'VAL_RND', 'domlow': 0, 'domup': 10, 'name': 'var1', 'type': 'integer'}
            ]
        }

        self.assertEqual(self.modeller.to_json(), expected_json)

if __name__ == '__main__':
    unittest.main()
