"""
This module provides the Modeller class for building optimization models.

Classes:
    Modeller: Represents a modeller used to construct optimization models.

Methods:
    add_variable(variable: Union[Variable, ArrayVariable]) -> Modeller:
        Adds a variable to the optimization model.

    add_constraint(constraint: Union[AbstractConstraint, Expression]) -> Modeller:
        Adds a constraint to the optimization model.

    add_objective(objective: Union[SpecificMinimum, SpecificMaximum]) -> Modeller:
        Adds an objective to the optimization model.

    set_searcher(searcher: SearcherType) -> Modeller:
        Sets the searcher type for optimization.

    set_cutoff(cutoff: Cutoff) -> Modeller:
        Sets a cutoff condition for optimization.

    set_callback_url(callback_url: str) -> Modeller:
        Sets a callback URL for optimization.

    to_json() -> dict:
        Converts the optimization model to a JSON representation.

Note:
    Refer to the individual method documentation for more details about their usage.

"""

from typing import Union
from qaekwy.exception.model_failure import ModelFailure
from qaekwy.model.constraint.abstract_constraint import AbstractConstraint
from qaekwy.model.constraint.relational import RelationalExpression
from qaekwy.model.cutoff import Cutoff
from qaekwy.model.searcher import SearcherType
from qaekwy.model.specific import SpecificMaximum, SpecificMinimum
from qaekwy.model.variable.variable import ArrayVariable, Expression, Variable


class Modeller:
    """
    Represents a modeller used to build optimization models.

    Attributes:
        constraint_list (list[AbstractConstraint]): A list of constraints.
        variable_list (list[Union[Variable, ArrayVariable]]): A list of variables.
        objective_list (list[Union[SpecificMinimum, SpecificMaximum]]): A list of objectives.
        searcher (SearcherType): The type of searcher to be used for optimization.
        cutoff (Cutoff): The cutoff condition for stopping the optimization.
        callback_url (str): The URL to which the optimization callback will be sent.

    Methods:
        add_variable(variable: Union[Variable, ArrayVariable]): Add a variable to the model.
        add_constraint(constraint: Union[AbstractConstraint, Expression]): Add a constraint to the model.
        add_objective(objective: Union[SpecificMinimum, SpecificMaximum]): Add an objective.
        set_searcher(searcher: SearcherType): Set the searcher type for optimization.
        set_cutoff(cutoff: Cutoff): Set the cutoff condition for optimization.
        set_callback_url(callback_url: str): Set the callback URL for optimization.
        to_json() -> dict: Convert the modeller and its components to a JSON representation.

    """

    def __init__(self) -> None:
        """
        Initialize a Modeller instance.
        """
        self.constraint_list = []
        self.variable_list = []
        self.objective_list = []
        self.searcher = None
        self.cutoff = None
        self.callback_url = None

    def add_variable(self, variable: Union[Variable, ArrayVariable]):
        """
        Add a variable to the model.

        Args:
            variable (Union[Variable, ArrayVariable]): The variable to be added.

        Returns:
            Modeller: The modeller instance for method chaining.
        """
        self.variable_list.append(variable)
        return self

    def add_constraint(self, constraint: Union[AbstractConstraint, Expression]):
        """
        Add a constraint to the model.

        Args:
            constraint (Union[AbstractConstraint, Expression]): The constraint to be added.

        Returns:
            Modeller: The modeller instance for method chaining.
        """
        self.constraint_list.append(
            RelationalExpression(constraint)
            if isinstance(constraint, Expression)
            else constraint
        )
        return self

    def add_objective(self, objective: Union[SpecificMinimum, SpecificMaximum]):
        """
        Add an objective to the model.

        Args:
            objective (Union[SpecificMinimum, SpecificMaximum]): The objective to be added.

        Returns:
            Modeller: The modeller instance for method chaining.
        """
        self.objective_list.append(objective)
        return self

    def set_searcher(self, searcher: SearcherType):
        """
        Set the searcher type for optimization.

        Args:
            searcher (SearcherType): The type of searcher to be used.

        Returns:
            Modeller: The modeller instance for method chaining.
        """
        self.searcher = searcher
        return self

    def set_cutoff(self, cutoff: Cutoff):
        """
        Set the cutoff condition for optimization.

        Args:
            cutoff (Cutoff): The cutoff condition.

        Returns:
            Modeller: The modeller instance for method chaining.
        """
        self.cutoff = cutoff
        return self

    def set_callback_url(self, callback_url: str):
        """
        Set the callback URL to call after model optimization.

        Args:
            callback_url (str): The callback URL.

        Returns:
            Modeller: The modeller instance for method chaining.
        """
        self.callback_url = callback_url
        return self

    def to_json(self) -> dict:
        """
        Convert the modeller and its components to a JSON representation.

        Returns:
            dict: A dictionary representing the modeller in JSON format.
        """
        res = {}

        if self.searcher is None:
            raise ModelFailure(
                "Not any SearcherType has been set (through 'set_searcher' method of 'Modeller')."
            )

        res["searcher"] = self.searcher.value

        res["var"] = []
        for var_elem in self.variable_list:
            res["var"].append(var_elem.to_json())

        res["constraint"] = []
        for constraint_elem in self.constraint_list:
            res["constraint"].append(constraint_elem.to_json())

        res["specific"] = []
        for specific_elem in self.objective_list:
            res["specific"].append(specific_elem.to_json())

        if self.cutoff is not None:
            res[
                "meta_cutoff" if self.cutoff.is_meta() else "cutoff"
            ] = self.cutoff.to_json()

        if self.callback_url is not None:
            res["callback_url"] = str(self.callback_url)

        res["solution_limit"] = 1

        return res
