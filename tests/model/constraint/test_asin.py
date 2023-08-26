# pylint: skip-file

import unittest
from qaekwy.model.constraint.asin import ConstraintASin
from qaekwy.model.variable.float import FloatVariable

class TestConstraintASin(unittest.TestCase):

    def setUp(self):
        self.var_angle = FloatVariable("var_angle", 0.0, 10.0)
        self.var_value = FloatVariable("var_value", 0.0, 10.0)

    def test_constraint_creation(self):
        constraint = ConstraintASin(self.var_angle, self.var_value, "asin_constraint")
        self.assertEqual(constraint.var_1, self.var_angle)
        self.assertEqual(constraint.var_2, self.var_value)
        self.assertEqual(constraint.constraint_name, "asin_constraint")

    def test_constraint_to_json(self):
        constraint = ConstraintASin(self.var_angle, self.var_value, "asin_constraint")
        expected_json = {
            "name": "asin_constraint",
            "v1": "var_angle",
            "v2": "var_value",
            "type": "asin"
        }
        self.assertEqual(constraint.to_json(), expected_json)

if __name__ == '__main__':
    unittest.main()
