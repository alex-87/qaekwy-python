# pylint: skip-file

import unittest

from qaekwy.model.variable.integer import IntegerVariable
from qaekwy.model.constraint.modulo import ConstraintModulo

class TestConstraintModulo(unittest.TestCase):

    def setUp(self):
        self.dividend_variable = IntegerVariable("dividend_variable", 0, 10)
        self.divisor_variable = IntegerVariable("divisor_variable", 0, 10)
        self.result_variable = IntegerVariable("result_variable", 0, 10)

    def test_constraint_creation(self):
        constraint = ConstraintModulo(
            self.dividend_variable,
            self.divisor_variable,
            self.result_variable,
            "modulo_constraint"
        )
        self.assertEqual(constraint.var_1, self.dividend_variable)
        self.assertEqual(constraint.var_2, self.divisor_variable)
        self.assertEqual(constraint.var_3, self.result_variable)
        self.assertEqual(constraint.constraint_name, "modulo_constraint")

    def test_constraint_to_json(self):
        constraint = ConstraintModulo(
            self.dividend_variable,
            self.divisor_variable,
            self.result_variable,
            "modulo_constraint"
        )
        expected_json = {
            "name": "modulo_constraint",
            "v1": "dividend_variable",
            "v2": "divisor_variable",
            "v3": "result_variable",
            "type": "mod"
        }
        self.assertEqual(constraint.to_json(), expected_json)

if __name__ == '__main__':
    unittest.main()
