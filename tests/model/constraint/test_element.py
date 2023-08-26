# pylint: skip-file

import unittest

from qaekwy.model.variable.integer import IntegerVariable, IntegerVariableArray
from qaekwy.model.constraint.element import ConstraintElement

class TestConstraintElement(unittest.TestCase):

    def setUp(self):
        self.mapping_array = IntegerVariable("mapping_array", 3)
        self.variable_1 = IntegerVariable("variable_1", 0, 10)
        self.variable_2 = IntegerVariable("variable_2", 0, 10)

    def test_constraint_creation(self):
        constraint = ConstraintElement(self.mapping_array, self.variable_1, self.variable_2, "element_constraint")
        self.assertEqual(constraint.map_array, self.mapping_array)
        self.assertEqual(constraint.var_1, self.variable_1)
        self.assertEqual(constraint.var_2, self.variable_2)
        self.assertEqual(constraint.constraint_name, "element_constraint")

    def test_constraint_to_json(self):
        constraint = ConstraintElement(self.mapping_array, self.variable_1, self.variable_2, "element_constraint")
        expected_json = {
            "name": "element_constraint",
            "map": "mapping_array",
            "v1": "variable_1",
            "v2": "variable_2",
            "type": "element"
        }
        self.assertEqual(constraint.to_json(), expected_json)

if __name__ == '__main__':
    unittest.main()
