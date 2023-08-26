"""Math Functions Module

This module defines various mathematical functions that can be applied to expressions
or arrays of expressions.

Functions:
    maximum(expr: ExpressionArray) -> Expression: Returns an expression representing the max value.
    minimum(expr: ExpressionArray) -> Expression: Returns an expression representing the min value.
    sum_of(expr: ExpressionArray) -> Expression: Returns an expression representing the sum.
    absolute(expr: Expression) -> Expression: Returns an expression representing the absolute value.
    power(expr: Expression, val) -> Expression: Returns an expression representing pow(expr, val).
    nroot(expr: Expression, val) -> Expression: Returns an expression representing the nth root.
    sqr(expr: Expression) -> Expression: Returns an expression representing the square.
    sqrt(expr: Expression) -> Expression: Returns an expression representing the square root.
    sin(expr: Expression) -> Expression: Returns an expression representing the sine.
    cos(expr: Expression) -> Expression: Returns an expression representing the cosine.
    tan(expr: Expression) -> Expression: Returns an expression representing the tangent.
    asin(expr: Expression) -> Expression: Returns an expression representing the arcsine.
    acos(expr: Expression) -> Expression: Returns an expression representing the arccosine.
    atan(expr: Expression) -> Expression: Returns an expression representing the arctangent.
    log(expr: Expression) -> Expression: Returns an expression representing the natural logarithm.
    exp(expr: Expression) -> Expression: Returns an expression representing the exponential.

"""

from qaekwy.model.variable.variable import Expression, ExpressionArray


def maximum(expr: ExpressionArray) -> Expression:
    """
    Returns an expression representing the maximum value of an expression array.

    Args:
        expr (ExpressionArray): The array of expressions.

    Returns:
        Expression: An expression representing the maximum value.
    """
    return Expression(f"max({expr})")


def minimum(expr: ExpressionArray) -> Expression:
    """
    Returns an expression representing the minimum value of an expression array.

    Args:
        expr (ExpressionArray): The array of expressions.

    Returns:
        Expression: An expression representing the minimum value.
    """
    return Expression(f"min({expr})")


def sum_of(expr: ExpressionArray) -> Expression:
    """
    Returns an expression representing the sum of an expression array.

    Args:
        expr (ExpressionArray): The array of expressions.

    Returns:
        Expression: An expression representing the sum.
    """
    return Expression(f"sum({expr})")


def absolute(expr: Expression) -> Expression:
    """
    Returns an expression representing the absolute value of an expression.

    Args:
        expr (Expression): The expression.

    Returns:
        Expression: An expression representing the absolute value.
    """
    return Expression(f"abs({expr})")


def power(expr: Expression, val) -> Expression:
    """
    Returns an expression representing the exponentiation of an expression by a value.

    Args:
        expr (Expression): The expression.
        val: The exponent value.

    Returns:
        Expression: An expression representing the exponentiation result.
    """

    return Expression(f"pow({expr}, {val})")


def nroot(expr: Expression, val) -> Expression:
    """
    Returns an expression representing the nth root of an expression by a value.

    Args:
        expr (Expression): The expression.
        val: The root value.

    Returns:
        Expression: An expression representing the nth root result.
    """
    return Expression(f"nroot({expr}, {val})")


def sqr(expr: Expression) -> Expression:
    """
    Returns an expression representing the square of an expression.

    Args:
        expr (Expression): The expression.

    Returns:
        Expression: An expression representing the square.
    """
    return Expression(f"sqr({expr})")


def sqrt(expr: Expression) -> Expression:
    """
    Returns an expression representing the square root of an expression.

    Args:
        expr (Expression): The expression.

    Returns:
        Expression: An expression representing the square root.
    """
    return Expression(f"sqrt({expr})")


def sin(expr: Expression) -> Expression:
    """
    Returns an expression representing the sine of an expression.

    Args:
        expr (Expression): The expression.

    Returns:
        Expression: An expression representing the sine value.
    """
    return Expression(f"sin({expr})")


def cos(expr: Expression) -> Expression:
    """
    Returns an expression representing the cosine of an expression.

    Args:
        expr (Expression): The expression.

    Returns:
        Expression: An expression representing the cosine value.
    """
    return Expression(f"cos({expr})")


def tan(expr: Expression) -> Expression:
    """
    Returns an expression representing the tangent of an expression.

    Args:
        expr (Expression): The expression.

    Returns:
        Expression: An expression representing the tangent value.
    """
    return Expression(f"tan({expr})")


def asin(expr: Expression) -> Expression:
    """
    Returns an expression representing the arcsine of an expression.

    Args:
        expr (Expression): The expression.

    Returns:
        Expression: An expression representing the arcsine value.
    """
    return Expression(f"asin({expr})")


def acos(expr: Expression) -> Expression:
    """
    Returns an expression representing the arccosine of an expression.

    Args:
        expr (Expression): The expression.

    Returns:
        Expression: An expression representing the arccosine value.
    """
    return Expression(f"acos({expr})")


def atan(expr: Expression) -> Expression:
    """
    Returns an expression representing the arctangent of an expression.

    Args:
        expr (Expression): The expression.

    Returns:
        Expression: An expression representing the arctangent value.
    """
    return Expression(f"atan({expr})")


def log(expr: Expression) -> Expression:
    """
    Returns an expression representing the natural logarithm of an expression.

    Args:
        expr (Expression): The expression.

    Returns:
        Expression: An expression representing the natural logarithm value.
    """
    return Expression(f"log({expr})")


def exp(expr: Expression) -> Expression:
    """
    Returns an expression representing the exponential function of an expression.

    Args:
        expr (Expression): The expression.

    Returns:
        Expression: An expression representing the exponential function value.
    """
    return Expression(f"exp({expr})")
