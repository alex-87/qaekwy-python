# pylint: skip-file

import unittest

from qaekwy.explanation import Explanation

class ExplanationTest(unittest.TestCase):

    def test_init(self):
        explanation_content = [
            {"name": "x", "type": "var", "explanation": "x is a variable"},
            {"name": "y", "type": "constraint", "explanation": "y is a constraint"},
        ]
        explanation = Explanation(explanation_content)

        self.assertEqual(explanation.get_variables()["x"]["type"], "var")
        self.assertEqual(explanation.get_variables()["x"]["explanation"], "x is a variable")
        self.assertEqual(explanation.get_constraints()["y"]["type"], "constraint")
        self.assertEqual(explanation.get_constraints()["y"]["explanation"], "y is a constraint")

    def test_missing_variable(self):
        explanation_content = [
            {"name": "y", "type": "constraint", "explanation": "y is a constraint"},
        ]
        explanation = Explanation(explanation_content)

        with self.assertRaises(KeyError):
            explanation.get_variables()["x"]

    def test_missing_constraint(self):
        explanation_content = [
            {"name": "x", "type": "var", "explanation": "x is a variable"},
        ]
        explanation = Explanation(explanation_content)

        with self.assertRaises(KeyError):
            explanation.get_constraints()["y"]

if __name__ == "__main__":
    unittest.main()
