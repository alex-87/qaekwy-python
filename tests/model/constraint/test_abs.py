# pylint: skip-file

import unittest
from qaekwy.model.constraint.abs import ConstraintAbs
from qaekwy.model.variable.integer import IntegerVariable


class TestConstraintAbs(unittest.TestCase):

    def setUp(self):
        self.var1 = IntegerVariable("var1", 0, 10)
        self.var2 = IntegerVariable("var2", 0, 10)

    def test_constraint_creation(self):
        constraint = ConstraintAbs(self.var1, self.var2, "abs_constraint")
        self.assertEqual(constraint.var_1, self.var1)
        self.assertEqual(constraint.var_2, self.var2)
        self.assertEqual(constraint.constraint_name, "abs_constraint")

    def test_constraint_to_json(self):
        constraint = ConstraintAbs(self.var1, self.var2, "abs_constraint")
        expected_json = {
            "name": "abs_constraint",
            "v1": "var1",
            "v2": "var2",
            "type": "abs"
        }
        self.assertEqual(constraint.to_json(), expected_json)

if __name__ == '__main__':
    unittest.main()
