# pylint: skip-file

import unittest

from qaekwy.core.model.variable.float import FloatVariable
from qaekwy.core.model.constraint.sin import ConstraintSin


class TestConstraintSin(unittest.TestCase):

    def test_constraint_creation(self):
        var_1 = FloatVariable("var_1", 0.0, 10.0)
        var_2 = FloatVariable("var_2", 0.0, 10.0)
        constraint = ConstraintSin(var_1, var_2, "sine_constraint")

        self.assertEqual(constraint.var_1, var_1)
        self.assertEqual(constraint.var_2, var_2)
        self.assertEqual(constraint.constraint_name, "sine_constraint")

    def test_constraint_to_json(self):
        var_1 = FloatVariable("var_1")
        var_2 = FloatVariable("var_2")
        constraint = ConstraintSin(var_1, var_2, "sine_constraint")

        expected_json = {
            "name": "sine_constraint",
            "v1": "var_1",
            "v2": "var_2",
            "type": "sin",
        }

        self.assertDictEqual(
            constraint.to_json(),
            constraint.from_json(expected_json, [var_1, var_2]).to_json(),
            expected_json,
        )


if __name__ == "__main__":
    unittest.main()
