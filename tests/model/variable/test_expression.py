# pylint: skip-file

import unittest
from qaekwy.model.variable.variable import Expression

class TestExpression(unittest.TestCase):

    def test_arithmetic_operators(self):
        expr = Expression(2)
        
        self.assertEqual(str(expr + 3), "(2 + 3)")
        self.assertEqual(str(4 + expr), "(4 + 2)")
        
        self.assertEqual(str(expr - 3), "(2 - 3)")
        self.assertEqual(str(4 - expr), "(4 - 2)")
        
        self.assertEqual(str(expr * 3), "2 * 3")
        self.assertEqual(str(4 * expr), "4 * 2")
        
        self.assertEqual(str(expr / 3), "((2) / (3))")
        self.assertEqual(str(4 / expr), "((4) / (2))")
        
        self.assertEqual(str(expr % 3), "((2) % (3))")
        self.assertEqual(str(4 % expr), "((4) % (2))")

    def test_logical_operators(self):
        expr1 = Expression(True)
        expr2 = Expression(False)
        
        self.assertEqual(str(expr1 & expr2), "True & False")
        self.assertEqual(str(expr1 | expr2), "(True | False)")
        self.assertEqual(str(expr1 ^ expr2), "((True) ^ (False))")
        
    def test_relational_operators(self):
        expr = Expression(5)
        
        self.assertEqual(str(expr == 5), "((5) == (5))")
        self.assertEqual(str(expr != 5), "((5) != (5))")
        self.assertEqual(str(expr < 6), "((5) < (6))")
        self.assertEqual(str(expr <= 6), "((5) <= (6))")
        self.assertEqual(str(expr > 4), "((5) > (4))")
        self.assertEqual(str(expr >= 4), "((5) >= (4))")

if __name__ == '__main__':
    unittest.main()
