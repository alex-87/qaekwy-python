"""Branch Module

This module defines classes related to brancher strategies.

Classes:
    BranchVal: Represents brancher value strategies.
    BranchVar: Represents brancher variable strategies.
    BranchIntegerVal: Represents brancher value strategies specific to integers.
    BranchFloatVal: Represents brancher value strategies specific to floats.
    BranchBooleanVal: Represents brancher value strategies specific to booleans.
    BranchIntegerVar: Represents brancher variable strategies specific to integers.
    BranchFloatVar: Represents brancher variable strategies specific to floats.
    BranchBooleanVar: Represents brancher variable strategies specific to booleans.

"""

from enum import Enum


class BranchVal(Enum):  # pylint: disable=too-few-public-methods
    """
    Represents brancher value strategies.

    The BranchVal class defines enumeration values that represent different
    strategies for selecting brancher values during the search process.
    """


class BranchVar(Enum):  # pylint: disable=too-few-public-methods
    """
    Represents brancher variable strategies.

    The BranchVar class defines enumeration values that represent different
    strategies for selecting brancher variables during the search process.
    """


class BranchIntegerVal(BranchVal):
    """
    Represents brancher value strategies specific to integers.

    The BranchIntegerVal class extends the BranchVal class and defines
    enumeration values that represent specific brancher value strategies
    for integer variables.
    """

    VAL_RND = "VAL_RND"
    VAL_MIN = "VAL_MIN"
    VAL_MED = "VAL_MED"
    VAL_MAX = "VAL_MAX"
    VALUES_MIN = "VALUES_MIN"
    VALUES_MAX = "VALUES_MAX"
    VAL_RANGE_MIN = "VAL_RANGE_MIN"
    VAL_RANGE_MAX = "VAL_RANGE_MAX"
    VAL_SPLIT_MIN = "VAL_SPLIT_MIN"
    VAL_SPLIT_MAX = "VAL_SPLIT_MAX"


class BranchFloatVal(BranchVal):
    """
    Represents brancher value strategies specific to floats.

    The BranchFloatVal class extends the BranchVal class and defines
    enumeration values that represent specific brancher value strategies
    for float variables.
    """

    VAL_RND = "VAL_RND"
    VAL_MIN = "VAL_MIN"
    VAL_MAX = "VAL_MAX"
    VAL_SPLIT_MIN = "VAL_SPLIT_MIN"
    VAL_SPLIT_MAX = "VAL_SPLIT_MAX"


class BranchBooleanVal(BranchVal):
    """
    Represents brancher value strategies specific to booleans.

    The BranchBooleanVal class extends the BranchVal class and defines
    enumeration values that represent specific brancher value strategies
    for boolean variables.
    """

    VAL_RND = "VAL_RND"
    VAL_MIN = "VAL_MIN"
    VAL_MAX = "VAL_MAX"


class BranchIntegerVar(BranchVar):
    """
    Represents brancher variable strategies specific to integers.

    The BranchIntegerVar class extends the BranchVar class and defines
    enumeration values that represent specific brancher variable strategies
    for integer variables.
    """

    VAR_NONE = "VAR_NONE"
    VAR_RND = "VAR_RND"
    VAR_SIZE_MIN = "VAR_SIZE_MIN"
    VAR_SIZE_MAX = "VAR_SIZE_MAX"
    VAR_REGRET_MIN_MIN = "VAR_REGRET_MIN_MIN"
    VAR_REGRET_MIN_MAX = "VAR_REGRET_MIN_MAX"
    VAR_DEGREE_MIN = "VAR_DEGREE_MIN"
    VAR_DEGREE_MAX = "VAR_DEGREE_MAX"
    VAR_MIN_MIN = "VAR_MIN_MIN"
    VAR_MIN_MAX = "VAR_MIN_MAX"
    VAR_MAX_MIN = "VAR_MAX_MIN"
    VAR_MAX_MAX = "VAR_MAX_MAX"
    VAR_DEGREE_SIZE_MIN = "VAR_DEGREE_SIZE_MIN"
    VAR_DEGREE_SIZE_MAX = "VAR_DEGREE_SIZE_MAX"


class BranchFloatVar(BranchVar):
    """
    Represents brancher variable strategies specific to floats.

    The BranchFloatVar class extends the BranchVar class and defines
    enumeration values that represent specific brancher variable strategies
    for float variables.
    """

    VAR_RND = "VAR_RND"
    VAR_SIZE_MIN = "VAR_SIZE_MIN"
    VAR_SIZE_MAX = "VAR_SIZE_MAX"
    VAR_DEGREE_MIN = "VAR_DEGREE_MIN"
    VAR_DEGREE_MAX = "VAR_DEGREE_MAX"
    VAR_MIN_MIN = "VAR_MIN_MIN"
    VAR_MIN_MAX = "VAR_MIN_MAX"
    VAR_MAX_MIN = "VAR_MAX_MIN"
    VAR_MAX_MAX = "VAR_MAX_MAX"
    VAR_DEGREE_SIZE_MIN = "VAR_DEGREE_SIZE_MIN"
    VAR_DEGREE_SIZE_MAX = "VAR_DEGREE_SIZE_MAX"


class BranchBooleanVar(BranchVar):
    """
    Represents brancher variable strategies specific to booleans.

    The BranchBooleanVar class extends the BranchVar class and defines
    enumeration values that represent specific brancher variable strategies
    for boolean variables.
    """

    VAR_RND = "VAR_RND"
    VAR_DEGREE_SIZE_MIN = "VAR_DEGREE_SIZE_MIN"
    VAR_DEGREE_SIZE_MAX = "VAR_DEGREE_SIZE_MAX"
