"""
This module provides concrete implementations of the Cutoff abstract base class for
specifying optimization cutoff conditions. Each concrete class represents a specific
type of optimization cutoff condition, such as constant, Fibonacci, and geometric progression.

Classes:
    CutoffConstant: Represents a constant optimization cutoff condition.
    CutoffFibonacci: Represents a Fibonacci optimization cutoff condition.
    CutoffGeometric: Represents a geometric progression optimization cutoff condition.
    CutoffLuby: Represents a Luby sequence optimization cutoff condition.
    CutoffLinear: Represents a linear optimization cutoff condition.
    CutoffRandom: Represents a random optimization cutoff condition.

This module also provides various meta-cutoff classes that allow users to combine
and manipulate different cutoff conditions. Meta-cutoffs are composite cutoff conditions that
apply multiple cutoffs in a specific manner to determine whether a search should be terminated.

Classes:
    - MetaCutoffAppender: Combines two cutoff conditions by appending the second cutoff to the
      first after a certain number of solutions.
    - MetaCutoffMerger: Merges two cutoff conditions into a single cutoff by applying
      both conditions.
    - MetaCutoffRepeater: Repeats a sub-cutoff condition a specified number of times.

Usage:
    from qaekwy.model.cutoff.meta_cutoff import (
        MetaCutoffAppender,
        MetaCutoffMerger,
        MetaCutoffRepeater
    )

    # Example usage of MetaCutoffAppender
    first_cutoff = CutoffConstant(100)
    second_cutoff = CutoffFibonacci()
    appender = MetaCutoffAppender(first_cutoff, number_from_first=10, second_cutoff=second_cutoff)

    # Example usage of MetaCutoffMerger
    first_cutoff = CutoffConstant(100)
    second_cutoff = CutoffGeometric(base=1.5, scale=10)
    merger = MetaCutoffMerger(first_cutoff, second_cutoff)

    # Example usage of MetaCutoffRepeater
    sub_cutoff = CutoffLinear(scale=5)
    repeater = MetaCutoffRepeater(sub_cutoff, repeat=3)

"""

from abc import ABC, abstractmethod


class Cutoff(ABC):  # pylint: disable=too-few-public-methods
    """
    An abstract base class representing an optimization cutoff condition.

    Methods:
        is_meta() -> bool:
            Check if the cutoff condition is a meta-cutoff.

        to_json():
            Convert the cutoff condition to a JSON representation.

    """

    @abstractmethod
    def is_meta(self) -> bool:
        """
        Check if the cutoff condition is a meta-cutoff.

        Returns:
            bool: True if the cutoff is a meta-cutoff, False otherwise.

        """

    @abstractmethod
    def to_json(self):
        """
        Convert the cutoff condition to a JSON representation.

        Returns:
            dict: A JSON representation of the cutoff condition.

        """


class CutoffConstant(Cutoff):  # pylint: disable=too-few-public-methods
    """
    Represents a constant optimization cutoff condition.

    Methods:
        is_meta() -> bool:
            Check if the cutoff condition is a meta-cutoff.

        to_json():
            Convert the cutoff condition to a JSON representation.

    """

    def __init__(self, constant_value: int) -> None:
        super().__init__()
        self.constant_value = constant_value

    def is_meta(self) -> bool:
        """
        Check if the cutoff condition is a meta-cutoff.

        Returns:
            bool: False, indicating that this is not a meta-cutoff.

        """
        return False

    def to_json(self):
        """
        Convert the cutoff condition to a JSON representation.

        Returns:
            dict: A JSON representation of the cutoff condition.

        """
        return {"name": "constant", "value": self.constant_value}


class CutoffFibonacci(Cutoff):  # pylint: disable=too-few-public-methods
    """
    Represents a Fibonacci optimization cutoff condition.

    Methods:
        is_meta() -> bool:
            Check if the cutoff condition is a meta-cutoff.

        to_json():
            Convert the cutoff condition to a JSON representation.

    """

    def is_meta(self) -> bool:
        """
        Check if the cutoff condition is a meta-cutoff.

        Returns:
            bool: False, indicating that this is not a meta-cutoff.

        """
        return False

    def to_json(self):
        """
        Convert the cutoff condition to a JSON representation.

        Returns:
            dict: A JSON representation of the cutoff condition.

        """
        return {"name": "fibonacci"}


class CutoffGeometric(Cutoff):  # pylint: disable=too-few-public-methods
    """
    Represents a geometric progression optimization cutoff condition.

    Methods:
        is_meta() -> bool:
            Check if the cutoff condition is a meta-cutoff.

        to_json():
            Convert the cutoff condition to a JSON representation.

    """

    def __init__(self, base: float, scale: int) -> None:
        super().__init__()
        self.base = base
        self.scale = scale

    def is_meta(self) -> bool:
        """
        Check if the cutoff condition is a meta-cutoff.

        Returns:
            bool: False, indicating that this is not a meta-cutoff.

        """
        return False

    def to_json(self):
        """
        Convert the cutoff condition to a JSON representation.

        Returns:
            dict: A JSON representation of the cutoff condition.

        """
        return {"name": "geometric", "scale": self.scale, "base": self.base}


class CutoffLuby(Cutoff):  # pylint: disable=too-few-public-methods
    """
    Represents a Luby sequence optimization cutoff condition.

    Methods:
        is_meta() -> bool:
            Check if the cutoff condition is a meta-cutoff.

        to_json():
            Convert the cutoff condition to a JSON representation.

    """

    def __init__(self, scale: int) -> None:
        """
        Initialize the CutoffLuby instance.

        Args:
            scale (int): The scaling factor for the Luby sequence.

        Returns:
            None

        """
        super().__init__()
        self.scale = scale

    def is_meta(self) -> bool:
        """
        Check if the cutoff condition is a meta-cutoff.

        Returns:
            bool: False, indicating that this is not a meta-cutoff.

        """
        return False

    def to_json(self):
        """
        Convert the cutoff condition to a JSON representation.

        Returns:
            dict: A JSON representation of the cutoff condition.

        """
        return {"name": "luby", "scale": self.scale}


class CutoffLinear(Cutoff):  # pylint: disable=too-few-public-methods
    """
    Represents a linear optimization cutoff condition.

    Methods:
        is_meta() -> bool:
            Check if the cutoff condition is a meta-cutoff.

        to_json():
            Convert the cutoff condition to a JSON representation.

    """

    def __init__(self, scale: int) -> None:
        """
        Initialize the CutoffLinear instance.

        Args:
            scale (int): The scaling factor for the linear cutoff.

        Returns:
            None

        """
        super().__init__()
        self.scale = scale

    def is_meta(self) -> bool:
        """
        Check if the cutoff condition is a meta-cutoff.

        Returns:
            bool: False, indicating that this is not a meta-cutoff.

        """
        return False

    def to_json(self):
        """
        Convert the cutoff condition to a JSON representation.

        Returns:
            dict: A JSON representation of the cutoff condition.

        """
        return {"name": "linear", "scale": self.scale}


class CutoffRandom(Cutoff):  # pylint: disable=too-few-public-methods
    """
    Represents a random optimization cutoff condition.

    Methods:
        is_meta() -> bool:
            Check if the cutoff condition is a meta-cutoff.

        to_json():
            Convert the cutoff condition to a JSON representation.

    """

    def __init__(self, seed: int, minimum: int, maximum: int, round_value: int) -> None:
        """
        Initialize the CutoffRandom instance.

        Args:
            seed (int): The seed value for the random number generator.
            minimum (int): The minimum cutoff value.
            maximum (int): The maximum cutoff value.
            round_value (int): The value to round the cutoff to.

        Returns:
            None

        """
        super().__init__()
        self.seed = seed
        self.minimum = minimum
        self.maximum = maximum
        self.round_value = round_value

    def is_meta(self) -> bool:
        """
        Check if the cutoff condition is a meta-cutoff.

        Returns:
            bool: False, indicating that this is not a meta-cutoff.

        """
        return False

    def to_json(self):
        """
        Convert the cutoff condition to a JSON representation.

        Returns:
            dict: A JSON representation of the cutoff condition.

        """
        return {
            "name": "random",
            "seed": self.seed,
            "min": self.minimum,
            "max": self.maximum,
            "round": self.round_value,
        }


class MetaCutoffAppender(Cutoff):  # pylint: disable=too-few-public-methods
    """
    Represents a meta-cutoff that appends two different cutoff conditions.

    Methods:
        __init__(first_cutoff: Cutoff, number_from_first: int, second_cutoff: Cutoff) -> None:
            Initialize the MetaCutoffAppender instance.

        is_meta() -> bool:
            Check if the cutoff condition is a meta-cutoff.

        to_json():
            Convert the cutoff condition to a JSON representation.

    """

    def __init__(
        self, first_cutoff: Cutoff, number_from_first: int, second_cutoff: Cutoff
    ) -> None:
        """
        Initialize the MetaCutoffAppender instance.

        Args:
            first_cutoff (Cutoff): The first cutoff condition.
            number_from_first (int): The number of solutions from the first cutoff to append.
            second_cutoff (Cutoff): The second cutoff condition.

        """
        super().__init__()
        self.first_cutoff = first_cutoff
        self.number_from_first = number_from_first
        self.second_cutoff = second_cutoff

    def is_meta(self) -> bool:
        """
        Check if the cutoff condition is a meta-cutoff.

        Returns:
            bool: True, indicating that this is a meta-cutoff.

        """
        return True

    def to_json(self):
        """
        Convert the cutoff condition to a JSON representation.

        Returns:
            dict: A JSON representation of the cutoff condition.

        """
        return {
            "name": "appender",
            "first_cutoff": self.first_cutoff.to_json(),
            "number_from_first": self.number_from_first,
            "second_cutoff": self.second_cutoff.to_json(),
        }


class MetaCutoffMerger(Cutoff):  # pylint: disable=too-few-public-methods
    """
    Represents a meta-cutoff that merges two different cutoff conditions.

    Methods:
        __init__(first_cutoff: Cutoff, second_cutoff: Cutoff) -> None:
            Initialize the MetaCutoffMerger instance.

        is_meta() -> bool:
            Check if the cutoff condition is a meta-cutoff.

        to_json():
            Convert the cutoff condition to a JSON representation.

    """

    def __init__(self, first_cutoff: Cutoff, second_cutoff: Cutoff) -> None:
        """
        Initialize the MetaCutoffMerger instance.

        Args:
            first_cutoff (Cutoff): The first cutoff condition.
            second_cutoff (Cutoff): The second cutoff condition.

        Returns:
            None

        """
        super().__init__()
        self.first_cutoff = first_cutoff
        self.second_cutoff = second_cutoff

    def is_meta(self) -> bool:
        """
        Check if the cutoff condition is a meta-cutoff.

        Returns:
            bool: True, indicating that this is a meta-cutoff.

        """
        return True

    def to_json(self):
        """
        Convert the cutoff condition to a JSON representation.

        Returns:
            dict: A JSON representation of the cutoff condition.

        """
        return {
            "name": "merger",
            "first_cutoff": self.first_cutoff.to_json(),
            "second_cutoff": self.second_cutoff.to_json(),
        }


class MetaCutoffRepeater(Cutoff):  # pylint: disable=too-few-public-methods
    """
    Represents a meta-cutoff that repeats a sub-cutoff condition multiple times.

    Methods:
        __init__(sub_cutoff: Cutoff, repeat: int) -> None:
            Initialize the MetaCutoffRepeater instance.

        is_meta() -> bool:
            Check if the cutoff condition is a meta-cutoff.

        to_json():
            Convert the cutoff condition to a JSON representation.

    """

    def __init__(self, sub_cutoff: Cutoff, repeat: int) -> None:
        """
        Initialize the MetaCutoffRepeater instance.

        Args:
            sub_cutoff (Cutoff): The sub-cutoff condition to be repeated.
            repeat (int): The number of times to repeat the sub-cutoff.

        Returns:
            None

        """
        super().__init__()
        self.sub_cutoff = sub_cutoff
        self.repeat = repeat

    def is_meta(self) -> bool:
        """
        Check if the cutoff condition is a meta-cutoff.

        Returns:
            bool: True, indicating that this is a meta-cutoff.

        """
        return True

    def to_json(self):
        """
        Convert the cutoff condition to a JSON representation.

        Returns:
            dict: A JSON representation of the cutoff condition.

        """
        return {
            "name": "repeater",
            "sub_cutoff": self.sub_cutoff.to_json(),
            "repeat": self.repeat,
        }
