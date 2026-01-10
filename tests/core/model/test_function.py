# pylint: skip-file

import unittest

import qaekwy as qw
from qaekwy.core.model.variable.variable import Expression, ExpressionArray

class TestMathExpressions(unittest.TestCase):

    def setUp(self):
        self.expr_a = Expression("x")
        self.expr_b = Expression("y")
        self.array = ExpressionArray([self.expr_a, self.expr_b])

    def test_maximum(self):
        result = qw.math.maximum(self.array)
        self.assertEqual(result, "max(x,y)")

    def test_minimum(self):
        result = qw.math.minimum(self.array)
        self.assertEqual(result, "min(x,y)")

    def test_sum_of(self):
        result = qw.math.sum_of(self.array)
        self.assertEqual(result, "sum(x,y)")

    def test_absolute(self):
        result = qw.math.absolute(self.expr_a)
        self.assertEqual(result, "abs(x)")

    def test_power(self):
        result = qw.math.power(self.expr_a, 3)
        self.assertEqual(result, "(pow(x, 3))")

    def test_nroot(self):
        result = qw.math.nroot(self.expr_a, 2)
        self.assertEqual(result, "nroot(x, 2)")

    def test_sqr(self):
        result = qw.math.sqr(self.expr_a)
        self.assertEqual(result, "sqr(x)")

    def test_sqrt(self):
        result = qw.math.sqrt(self.expr_a)
        self.assertEqual(result, "sqrt(x)")

    def test_trigonometry(self):
        self.assertEqual(qw.math.sin(self.expr_a), "sin(x)")
        self.assertEqual(qw.math.cos(self.expr_a), "cos(x)")
        self.assertEqual(qw.math.tan(self.expr_a), "tan(x)")

    def test_inverse_trigonometry(self):
        self.assertEqual(qw.math.asin(self.expr_a), "asin(x)")
        self.assertEqual(qw.math.acos(self.expr_a), "acos(x)")
        self.assertEqual(qw.math.atan(self.expr_a), "atan(x)")

    def test_log_and_exp(self):
        self.assertEqual(qw.math.log(self.expr_a), "log(x)")
        self.assertEqual(qw.math.exp(self.expr_a), "exp(x)")

if __name__ == "__main__":
    unittest.main()
