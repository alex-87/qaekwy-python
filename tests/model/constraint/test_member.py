# pylint: skip-file

import unittest
from qaekwy.model.constraint.member import ConstraintMember, ArrayVariable, Variable

class TestConstraintMember(unittest.TestCase):

    def setUp(self):
        self.array_variable = ArrayVariable("array_variable", length=5)
        self.variable_to_check = Variable("variable_to_check")

    def test_constraint_creation(self):
        constraint = ConstraintMember(self.array_variable, self.variable_to_check, "member_constraint")
        self.assertEqual(constraint.var_1, self.array_variable)
        self.assertEqual(constraint.var_2, self.variable_to_check)
        self.assertEqual(constraint.constraint_name, "member_constraint")

    def test_constraint_to_json(self):
        constraint = ConstraintMember(self.array_variable, self.variable_to_check, "member_constraint")
        expected_json = {
            "name": "member_constraint",
            "v1": "array_variable",
            "v2": "variable_to_check",
            "type": "member"
        }
        self.assertEqual(constraint.to_json(), expected_json)

if __name__ == '__main__':
    unittest.main()
