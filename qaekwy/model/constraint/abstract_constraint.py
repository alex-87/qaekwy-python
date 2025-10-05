"""Abstract Constraint Class

This module defines the AbstractConstraint class, an abstract
base class for representing constraints in a modelling.

Classes:
    AbstractConstraint: Represents an abstract constraint.

"""

import random
import string
from abc import ABC, abstractmethod


class AbstractConstraint(ABC):
    """Represents an abstract constraint.

    This class serves as an abstract base class for defining constraints
    within a modelling. Constraints encapsulate relationships and rules that
    must be satisfied within the model.

    Attributes:
        constraint_name: The name of the constraint.
    """

    def random_constraint_name(self) -> str:
        """Generates a random constraint name.

        Returns:
            A randomly generated constraint name.
        """
        return "".join(
            random.choices(
                string.ascii_lowercase + string.ascii_uppercase + string.digits, k=16
            )
        )

    def __init__(self, constraint_name) -> None:
        """Initializes an AbstractConstraint instance.

        Args:
            constraint_name: The name of the constraint. If None, a random
                name is generated.
        """
        self.constraint_name = (
            constraint_name
            if constraint_name is not None
            else self.random_constraint_name()
        )

    @abstractmethod
    def to_json(self) -> dict:
        """Converts the constraint to a JSON representation.

        This method must be implemented in concrete subclasses to provide
        a JSON representation of the constraint.

        Returns:
            A dictionary representing the constraint in JSON format.
        """
        return {}
