# pylint: skip-file


import unittest

from qaekwy.model.variable.variable import Expression
from qaekwy.model.variable.integer import IntegerVariable

from qaekwy.model.constraint.relational import RelationalExpression


class TestRelationalExpression(unittest.TestCase):

    def setUp(self):
        self.var_1 = IntegerVariable("var_1", 0, 10)
        self.var_2 = IntegerVariable("var_2", 0, 10)
        self.var_3 = IntegerVariable("var_3", 0, 10)
        self.expression = Expression(self.var_1 + self.var_2 >= self.var_3 + 1)

    def test_constraint_creation(self):
        constraint = RelationalExpression(self.expression, "relational_constraint")
        self.assertEqual(constraint.expr, self.expression)
        self.assertEqual(constraint.constraint_name, "relational_constraint")

    def test_constraint_to_json(self):
        constraint = RelationalExpression(self.expression, "relational_constraint")
        expected_json = {
            "name": "relational_constraint",
            "expr": "(((var_1 + var_2)) >= ((var_3 + 1)))",
            "type": "rel"
        }
        self.assertEqual(constraint.to_json(), expected_json)

if __name__ == '__main__':
    unittest.main()
