"""Abstract Constraint Class

This module defines the AbstractConstraint class, an abstract
base class for representing constraints in a modelling.

Classes:
    AbstractConstraint: Represents an abstract constraint.

"""

from abc import ABC, abstractmethod

import random
import string


class AbstractConstraint(ABC):
    """
    Represents an abstract constraint.

    The AbstractConstraint class serves as an abstract base class for defining
    constraints within a modelling. Constraints encapsulate relationships
    and rules that must be satisfied within the model.

    Attributes:
        constraint_name (str): The name of the constraint.

    Methods:
        random_constraint_name(): Generates a random constraint name.
        to_json(): Converts the constraint to a JSON representation.

    """

    def random_constraint_name(self) -> str:
        """
        Generate a random constraint name.

        Returns:
            str: A randomly generated constraint name.
        """
        return "".join(
            random.choices(
                string.ascii_lowercase + string.ascii_uppercase + string.digits, k=16
            )
        )

    def __init__(self, constraint_name) -> None:
        """
        Initialize an AbstractConstraint instance.

        Args:
            constraint_name (str): The name of the constraint. If None, a random name is generated.

        """
        self.constraint_name = (
            constraint_name
            if constraint_name is not None
            else self.random_constraint_name()
        )

    @abstractmethod
    def to_json(self):
        """
        Convert the constraint to a JSON representation.

        This method must be implemented in concrete subclasses to provide
        a JSON representation of the constraint.

        Returns:
            dict: A dictionary representing the constraint in JSON format.

        """
        return {}
