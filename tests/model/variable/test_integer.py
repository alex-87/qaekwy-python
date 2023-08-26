# pylint: skip-file

import unittest

from qaekwy.model.variable.integer import IntegerVariable
from qaekwy.model.variable.variable import Expression

class TestExpression(unittest.TestCase):
    def test_arithmetic_operations(self):
        expr = Expression("x")
        expr_add = expr + 2
        self.assertEqual(str(expr_add), "(x + 2)")
        
        expr_sub = expr - 3
        self.assertEqual(str(expr_sub), "(x - 3)")
        
        expr_mul = expr * 4
        self.assertEqual(str(expr_mul), "x * 4")
        
        expr_div = expr / 5
        self.assertEqual(str(expr_div), "((x) / (5))")
        
        expr_mod = expr % 6
        self.assertEqual(str(expr_mod), "((x) % (6))")

class TestVariable(unittest.TestCase):
    def test_variable_to_json(self):
        var = IntegerVariable("x", domain_low=0, domain_high=10)
        
        var_json = var.to_json()
        self.assertEqual(var_json["name"], "x")
        self.assertEqual(var_json["type"], "integer")
        self.assertEqual(var_json["brancher_value"], "VAL_RND")
        self.assertEqual(var_json["domlow"], 0)
        self.assertEqual(var_json["domup"], 10)


class TestSpecificDomainVariable(unittest.TestCase):
    def test_variable_to_json(self):
        var = IntegerVariable("x", specific_domain=[2, 4, 6])
        
        var_json = var.to_json()
        self.assertEqual(var_json["name"], "x")
        self.assertEqual(var_json["type"], "integer")
        self.assertEqual(var_json["brancher_value"], "VAL_RND")
        self.assertEqual(var_json["specific_domain"], [2, 4, 6])


class TestExprVariable(unittest.TestCase):
    def test_variable_to_json(self):
        var = IntegerVariable("x")
        var_expr = var + 2
        var.expression = var_expr
        
        var_json = var.to_json()
        self.assertEqual(var_json["name"], "x")
        self.assertEqual(var_json["type"], "integer")
        self.assertEqual(var_json["brancher_value"], "VAL_RND")
        self.assertEqual(var_json["expr"], "(x + 2)")


class TestIntegerVariable(unittest.TestCase):
    def test_integer_variable_to_json(self):
        int_var = IntegerVariable("y", domain_low=1, domain_high=5)
        int_var_json = int_var.to_json()
        self.assertEqual(int_var_json["name"], "y")
        self.assertEqual(int_var_json["type"], "integer")
        self.assertEqual(int_var_json["brancher_value"], "VAL_RND")
        self.assertEqual(int_var_json["domlow"], 1)
        self.assertEqual(int_var_json["domup"], 5)


if __name__ == "__main__":
    unittest.main()
