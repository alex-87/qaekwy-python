# pylint: skip-file

import unittest
from qaekwy.model.constraint.divide import ConstraintDivide
from qaekwy.model.variable.integer import IntegerVariable

class TestConstraintDivide(unittest.TestCase):

    def setUp(self):
        self.numerator = IntegerVariable("numerator", 0, 100)
        self.denominator = IntegerVariable("denominator", 1, 10)
        self.result = IntegerVariable("result", 1, 10)

    def test_constraint_creation(self):
        constraint = ConstraintDivide(self.numerator, self.denominator, self.result, "divide_constraint")
        self.assertEqual(constraint.var_1, self.numerator)
        self.assertEqual(constraint.var_2, self.denominator)
        self.assertEqual(constraint.var_3, self.result)
        self.assertEqual(constraint.constraint_name, "divide_constraint")

    def test_constraint_to_json(self):
        constraint = ConstraintDivide(self.numerator, self.denominator, self.result, "divide_constraint")
        expected_json = {
            "name": "divide_constraint",
            "v1": "numerator",
            "v2": "denominator",
            "v3": "result",
            "type": "div"
        }
        self.assertEqual(constraint.to_json(), expected_json)

if __name__ == '__main__':
    unittest.main()
