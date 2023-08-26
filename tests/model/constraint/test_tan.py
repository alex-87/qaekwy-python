# pylint: skip-file

import unittest

from qaekwy.model.variable.float import FloatVariable
from qaekwy.model.constraint.tan import ConstraintTan


class TestConstraintTan(unittest.TestCase):

    def test_tan_constraint_creation(self):
        var_1 = FloatVariable("var_1", 0.0, 10.0)
        var_2 = FloatVariable("var_2", 0.0, 10.0)
        tan_constraint = ConstraintTan(var_1, var_2, "tan_constraint")
        
        self.assertEqual(tan_constraint.var_1, var_1)
        self.assertEqual(tan_constraint.var_2, var_2)
        self.assertEqual(tan_constraint.constraint_name, "tan_constraint")

    def test_tan_constraint_to_json(self):
        var_1 = FloatVariable("var_1", 0.0, 10.0)
        var_2 = FloatVariable("var_2", 0.0, 10.0)
        tan_constraint = ConstraintTan(var_1, var_2, "tan_constraint")
        
        expected_json = {
            "name": "tan_constraint",
            "v1": "var_1",
            "v2": "var_2",
            "type": "tan"
        }
        
        self.assertEqual(tan_constraint.to_json(), expected_json)

if __name__ == '__main__':
    unittest.main()
