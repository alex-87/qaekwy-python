# pylint: skip-file

import unittest

from qaekwy.solution import Solution

class SolutionTest(unittest.TestCase):

    def test_init(self):
        solution_json_content = [
            {"name": "x", "assigned": True, "value": 5},
            {"name": "y", "assigned": True, "value": 10},
            {"name": "z", "assigned": False, "value": None}
        ]
        solution = Solution(solution_json_content)

        self.assertEqual(solution["x"], 5)
        self.assertEqual(solution["y"], 10)
        self.assertEqual(solution["z"], None)

        self.assertTrue(hasattr(solution, "x"))
        self.assertTrue(hasattr(solution, "y"))
        self.assertTrue(hasattr(solution, "z"))

        self.assertEqual(solution.x, 5)
        self.assertEqual(solution.y, 10)
        self.assertEqual(solution.z, None)

    def test_positional_assignment(self):
        solution_json_content = [
            {"name": "x", "assigned": True, "value": 5, "position": 1},
            {"name": "y", "assigned": True, "value": 10, "position": 0},
            {"name": "z", "assigned": False, "value": None}
        ]
        solution = Solution(solution_json_content)

        self.assertEqual(solution["x"], [None, 5])
        self.assertEqual(solution["y"][0], 10)
        self.assertEqual(solution["z"], None)

    def test_missing_variable(self):
        solution_json_content = [
            {"name": "x", "assigned": True, "value": 5},
            {"name": "y", "assigned": True, "value": 10},
        ]
        solution = Solution(solution_json_content)

        with self.assertRaises(KeyError):
            solution["z"]

    def test_invalid_position(self):
        solution_json_content = [
            {"name": "x", "assigned": True, "value": 5, "position": 1},
            {"name": "y", "assigned": True, "value": 10, "position": 0},
            {"name": "z", "assigned": False, "value": None}
        ]
        solution = Solution(solution_json_content)

        with self.assertRaises(IndexError):
            solution["x"][2]

if __name__ == "__main__":
    unittest.main()
