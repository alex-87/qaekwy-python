"""SearcherType Module

This module defines the SearcherType enum, which represents different types of search algorithms
used in constraint-based modeling and optimization.

Enums:
    SearcherType: Represents different types of search algorithms.

"""
from enum import Enum


class SearcherType(Enum):
    """
    Represents different types of search algorithms.

    The SearcherType enum defines symbolic representations of various search algorithms used
    in constraint-based modeling and optimization, such as Depth-First Search (DFS),
    Branch and Bound (BAB), Limited Discrepancy Search (LDS), Portfolio-Based Search (PBS),
    and Randomized Binary Search (RBS).

    Enum Members:
        DFS (str): Depth-First Search algorithm.
        BAB (str): Branch and Bound algorithm.
        LDS (str): Limited Discrepancy Search algorithm.
        PBS (str): Portfolio-Based Search algorithm.
        RBS (str): Randomized Binary Search algorithm.

    Example:
        searcher = SearcherType.LDS  # Represents "Limited Discrepancy Search"
    """

    DFS = "DFS"
    BAB = "BAB"
    LDS = "LDS"
    PBS = "PBS"
    RBS = "RBS"
