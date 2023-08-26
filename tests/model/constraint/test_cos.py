# pylint: skip-file

import unittest
from qaekwy.model.constraint.cos import ConstraintCos
from qaekwy.model.variable.float import FloatVariable

class TestConstraintCos(unittest.TestCase):

    def setUp(self):
        self.var_angle = FloatVariable("var_angle", 0.0, 10.0)
        self.var_value = FloatVariable("var_value", 0.0, 10.0)

    def test_constraint_creation(self):
        constraint = ConstraintCos(self.var_angle, self.var_value, "cos_constraint")
        self.assertEqual(constraint.var_1, self.var_angle)
        self.assertEqual(constraint.var_2, self.var_value)
        self.assertEqual(constraint.constraint_name, "cos_constraint")

    def test_constraint_to_json(self):
        constraint = ConstraintCos(self.var_angle, self.var_value, "cos_constraint")
        expected_json = {
            "name": "cos_constraint",
            "v1": "var_angle",
            "v2": "var_value",
            "type": "cos"
        }
        self.assertEqual(constraint.to_json(), expected_json)

if __name__ == '__main__':
    unittest.main()