# pylint: skip-file

import unittest

from qaekwy.core.model.variable.float import FloatVariable
from qaekwy.core.model.constraint.exponential import ConstraintExponential


class TestConstraintExponential(unittest.TestCase):

    def setUp(self):
        self.base_variable = FloatVariable("base_variable", 0.0, 10.0)
        self.result_variable = FloatVariable("result_variable", 0.0, 10.0)

    def test_constraint_creation(self):
        constraint = ConstraintExponential(
            self.base_variable, self.result_variable, "exponential_constraint"
        )
        self.assertEqual(constraint.var_1, self.base_variable)
        self.assertEqual(constraint.var_2, self.result_variable)
        self.assertEqual(constraint.constraint_name, "exponential_constraint")

    def test_constraint_to_json(self):
        constraint = ConstraintExponential(
            self.base_variable, self.result_variable, "exponential_constraint"
        )
        expected_json = {
            "name": "exponential_constraint",
            "v1": "base_variable",
            "v2": "result_variable",
            "type": "exp",
        }
        self.assertDictEqual(
            constraint.to_json(),
            constraint.from_json(
                expected_json, [self.base_variable, self.result_variable]
            ).to_json(),
            expected_json,
        )


if __name__ == "__main__":
    unittest.main()
