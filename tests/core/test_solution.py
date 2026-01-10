# pylint: skip-file

import unittest

from io import StringIO
from contextlib import redirect_stdout

from qaekwy.core.solution import Solution

class TestSolutionScalars(unittest.TestCase):

    def test_scalar_assigned(self):
        content = [
            {"name": "x", "assigned": True, "value": 5},
            {"name": "y", "assigned": True, "value": 10},
        ]

        sol = Solution(content)

        self.assertEqual(sol["x"], 5)
        self.assertEqual(sol["y"], 10)

        self.assertEqual(sol.x, 5)
        self.assertEqual(sol.y, 10)

    def test_scalar_unassigned(self):
        content = [
            {"name": "x", "assigned": False, "value": None},
        ]

        sol = Solution(content)

        self.assertIsNone(sol["x"])
        self.assertIsNone(sol.x)

class TestSolutionArrays(unittest.TestCase):

    def test_array_with_positions(self):
        content = [
            {"name": "a", "assigned": True, "value": 1, "position": 0},
            {"name": "a", "assigned": True, "value": 3, "position": 2},
            {"name": "a", "assigned": False, "value": None, "position": 1},
        ]

        sol = Solution(content)

        self.assertEqual(sol["a"], [1, None, 3])
        self.assertEqual(sol.a, [1, None, 3])

    def test_sparse_array_positions(self):
        content = [
            {"name": "b", "assigned": True, "value": 7, "position": 3},
        ]

        sol = Solution(content)

        self.assertEqual(sol["b"], [None, None, None, 7])

class TestSolutionMatrices(unittest.TestCase):

    def test_matrix_reconstruction(self):
        content = [
            {"name": "MATRIX$2$3$m", "assigned": True, "value": 1, "position": 0},
            {"name": "MATRIX$2$3$m", "assigned": True, "value": 2, "position": 1},
            {"name": "MATRIX$2$3$m", "assigned": True, "value": 3, "position": 2},
            {"name": "MATRIX$2$3$m", "assigned": True, "value": 4, "position": 3},
            {"name": "MATRIX$2$3$m", "assigned": True, "value": 5, "position": 4},
            {"name": "MATRIX$2$3$m", "assigned": True, "value": 6, "position": 5},
        ]

        sol = Solution(content)

        expected = [
            [1, 2, 3],
            [4, 5, 6],
        ]

        self.assertIn("m", sol)
        self.assertNotIn("MATRIX$2$3$m", sol)

        self.assertEqual(sol["m"], expected)
        self.assertEqual(sol.m, expected)

class TestSolutionMixed(unittest.TestCase):

    def test_mixed_solution(self):
        content = [
            {"name": "x", "assigned": True, "value": 9},
            {"name": "arr", "assigned": True, "value": 1, "position": 0},
            {"name": "arr", "assigned": True, "value": 2, "position": 1},
            {"name": "MATRIX$1$2$m", "assigned": True, "value": 4, "position": 0},
            {"name": "MATRIX$1$2$m", "assigned": True, "value": 5, "position": 1},
        ]

        sol = Solution(content)

        self.assertEqual(sol.x, 9)
        self.assertEqual(sol.arr, [1, 2])
        self.assertEqual(sol.m, [[4, 5]])

class TestSolutionRepr(unittest.TestCase):

    def test_repr(self):
        content = [{"name": "x", "assigned": True, "value": 1}]
        sol = Solution(content)

        rep = repr(sol)

        self.assertTrue(rep.startswith("Solution("))
        self.assertIn("'x': 1", rep)

class TestSolutionPrettyPrint(unittest.TestCase):

    def test_pretty_print_scalar(self):
        content = [{"name": "x", "assigned": True, "value": 5}]
        sol = Solution(content)

        buf = StringIO()
        with redirect_stdout(buf):
            sol.pretty_print()

        output = buf.getvalue()

        self.assertIn("Solution:", output)
        self.assertIn("x", output)
        self.assertIn("5", output)

    def test_pretty_print_array(self):
        content = [
            {"name": "a", "assigned": True, "value": 1, "position": 0},
            {"name": "a", "assigned": False, "value": None, "position": 1},
        ]
        sol = Solution(content)

        buf = StringIO()
        with redirect_stdout(buf):
            sol.pretty_print()

        output = buf.getvalue()

        self.assertIn("[1, -]", output)

    def test_pretty_print_matrix(self):
        content = [
            {"name": "MATRIX$2$2$m", "assigned": True, "value": 1, "position": 0},
            {"name": "MATRIX$2$2$m", "assigned": True, "value": 2, "position": 1},
            {"name": "MATRIX$2$2$m", "assigned": True, "value": 3, "position": 2},
            {"name": "MATRIX$2$2$m", "assigned": True, "value": 4, "position": 3},
        ]

        sol = Solution(content)

        buf = StringIO()
        with redirect_stdout(buf):
            sol.pretty_print()

        output = buf.getvalue()

        self.assertIn("(2 x 2 matrix)", output)
        self.assertIn("1 2", output)
        self.assertIn("3 4", output)

    def test_pretty_print_empty(self):
        sol = Solution([])

        buf = StringIO()
        with redirect_stdout(buf):
            sol.pretty_print()

        self.assertIn("Empty solution", buf.getvalue())
