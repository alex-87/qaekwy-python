# pylint: skip-file

import unittest

from qaekwy.model.variable.integer import IntegerVariable
from qaekwy.model.constraint.minimum import ConstraintMinimum

class TestConstraintMinimum(unittest.TestCase):

    def setUp(self):
        self.variable_1 = IntegerVariable("variable_1", 0, 10)
        self.variable_2 = IntegerVariable("variable_2", 0, 10)
        self.variable_3 = IntegerVariable("variable_3", 0, 10)

    def test_constraint_creation(self):
        constraint = ConstraintMinimum(self.variable_1, self.variable_2, self.variable_3, "min_constraint")
        self.assertEqual(constraint.var_1, self.variable_1)
        self.assertEqual(constraint.var_2, self.variable_2)
        self.assertEqual(constraint.var_3, self.variable_3)
        self.assertEqual(constraint.constraint_name, "min_constraint")

    def test_constraint_to_json(self):
        constraint = ConstraintMinimum(self.variable_1, self.variable_2, self.variable_3, "min_constraint")
        expected_json = {
            "name": "min_constraint",
            "v1": "variable_1",
            "v2": "variable_2",
            "v3": "variable_3",
            "type": "min"
        }
        self.assertEqual(constraint.to_json(), expected_json)

if __name__ == '__main__':
    unittest.main()
