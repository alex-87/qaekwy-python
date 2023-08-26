"""RelationType Module

This module defines the RelationType enum, which represents different
types of relational comparisons.

Enums:
    RelationType: Represents different types of relational comparisons.

"""
from enum import Enum


class RelationType(Enum):
    """
    Represents different types of relational comparisons.

    The RelationType enum defines symbolic representations of common relational comparisons
    used in constraint-based modelling, such as greater than, greater than or equal to,
    equal to, not equal to, less than or equal to, and less than.

    Enum Members:
        GT (str): Greater than.
        GE (str): Greater than or equal to.
        EQ (str): Equal to.
        NE (str): Not equal to.
        LE (str): Less than or equal to.
        LT (str): Less than.

    Example:
        relation = RelationType.GE  # Represents "greater than or equal to"
    """

    GT = "GT"
    GE = "GE"
    EQ = "EQ"
    NE = "NE"
    LE = "LE"
    LT = "LT"
