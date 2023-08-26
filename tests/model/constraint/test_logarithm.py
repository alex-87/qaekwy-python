# pylint: skip-file

import unittest

from qaekwy.model.variable.float import FloatVariable
from qaekwy.model.constraint.logarithm import ConstraintLogarithme


class TestConstraintLogarithme(unittest.TestCase):

    def setUp(self):
        self.variable_to_log = FloatVariable("variable_to_log", 0.0, 10.0)
        self.result_variable = FloatVariable("result_variable", 0.0, 10.0)

    def test_constraint_creation(self):
        constraint = ConstraintLogarithme(self.variable_to_log, self.result_variable, "logarithmic_constraint")
        self.assertEqual(constraint.var_1, self.variable_to_log)
        self.assertEqual(constraint.var_2, self.result_variable)
        self.assertEqual(constraint.constraint_name, "logarithmic_constraint")

    def test_constraint_to_json(self):
        constraint = ConstraintLogarithme(self.variable_to_log, self.result_variable, "logarithmic_constraint")
        expected_json = {
            "name": "logarithmic_constraint",
            "v1": "variable_to_log",
            "v2": "result_variable",
            "type": "log"
        }
        self.assertEqual(constraint.to_json(), expected_json)

if __name__ == '__main__':
    unittest.main()
