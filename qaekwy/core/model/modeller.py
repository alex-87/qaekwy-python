"""
This module defines the Modeller class, which provides an interface
for building and exporting optimization models.

Classes:
    Modeller: Encapsulates variables, constraints, objectives, and solver settings
              used to define a complete optimization model.

Typical usage example:

    modeller = Modeller()
    modeller.add_variable(...)
            .add_constraint(...)
            .add_objective(...)
            .set_searcher(...)
            .set_cutoff(...)
            .set_callback_url(...)
    json_model = modeller.to_json()
"""

from typing import Any, Optional, Union

from qaekwy.core.exception.model_failure import ModelFailure

from qaekwy.core.model.constraint.abstract_constraint import AbstractConstraint
from qaekwy.core.model.constraint.abs import ConstraintAbs
from qaekwy.core.model.constraint.acos import ConstraintACos
from qaekwy.core.model.constraint.asin import ConstraintASin
from qaekwy.core.model.constraint.atan import ConstraintATan
from qaekwy.core.model.constraint.cos import ConstraintCos
from qaekwy.core.model.constraint.distinct import (
    ConstraintDistinctArray,
    ConstraintDistinctCol,
    ConstraintDistinctRow,
    ConstraintDistinctSlice,
)
from qaekwy.core.model.constraint.divide import ConstraintDivide
from qaekwy.core.model.constraint.element import ConstraintElement
from qaekwy.core.model.constraint.exponential import ConstraintExponential
from qaekwy.core.model.constraint.logarithm import ConstraintLogarithm
from qaekwy.core.model.constraint.maximum import ConstraintMaximum
from qaekwy.core.model.constraint.minimum import ConstraintMinimum
from qaekwy.core.model.constraint.modulo import ConstraintModulo
from qaekwy.core.model.constraint.member import ConstraintMember
from qaekwy.core.model.constraint.multiply import ConstraintMultiply
from qaekwy.core.model.constraint.nroot import ConstraintNRoot
from qaekwy.core.model.constraint.power import ConstraintPower
from qaekwy.core.model.constraint.relational import RelationalExpression
from qaekwy.core.model.constraint.sin import ConstraintSin
from qaekwy.core.model.constraint.sort import ConstraintSorted, ConstraintReverseSorted
from qaekwy.core.model.constraint.tan import ConstraintTan
from qaekwy.core.model.constraint.if_then_else import ConstraintIfThenElse

from qaekwy.core.model.cutoff import Cutoff
from qaekwy.core.model.searcher import SearcherType
from qaekwy.core.model.specific import SpecificMaximum, SpecificMinimum
from qaekwy.core.model.variable.variable import (
    ArrayVariable,
    Expression,
    MatrixVariable,
    Variable,
    VariableType,
)


class Modeller:
    """
    Constructs and configures optimization models.

    Attributes:
        variable_list (list[Union[Variable, ArrayVariable]]): Collection of model variables.
        constraint_list (list[Union[AbstractConstraint]]): Collection of model constraints.
        objective_list (list[Union[SpecificMinimum, SpecificMaximum]]): Optimization objectives (minimize or maximize).
        searcher (SearcherType): Strategy for searching solution space.
        cutoff (Cutoff): Optional stopping condition.
        callback_url (str): Optional URL for post-solution callback.
        solution_limit (int): Maximum number of solutions to return.
    """

    def __init__(self) -> None:
        """
        Initializes an empty Modeller instance.
        """
        self.variable_list: list[Union[Variable, ArrayVariable]] = []
        self.constraint_list: list[Union[AbstractConstraint]] = []
        self.objective_list: list[Union[SpecificMinimum, SpecificMaximum]] = []
        self.searcher: Optional[SearcherType] = None
        self.cutoff: Optional[Cutoff] = None
        self.callback_url: Optional[str] = None
        self.solution_limit: int = 1

    def add_variable(self, variable: Union[Variable, ArrayVariable]) -> "Modeller":
        """
        Adds a variable or array of variables to the model.

        Args:
            variable: A single Variable or ArrayVariable instance.

        Returns:
            self: Enables method chaining.
        """
        self.variable_list.append(variable)
        return self

    def add_constraint(
        self,
        constraint: Union[AbstractConstraint, Expression],
        domain: VariableType = VariableType.INTEGER,
    ) -> "Modeller":
        """
        Adds a constraint to the model.

        Args:
            constraint: Either an AbstractConstraint or a plain Expression,
                        which is wrapped in a RelationalExpression.

        Returns:
            self: Enables method chaining.
        """
        if isinstance(constraint, Expression):
            constraint = RelationalExpression(constraint, domain=domain)
        self.constraint_list.append(constraint)
        return self

    def add_objective(
        self, objective: Union[SpecificMinimum, SpecificMaximum]
    ) -> "Modeller":
        """
        Adds an optimization objective (minimization or maximization).

        Args:
            objective: SpecificMinimum or SpecificMaximum instance.

        Returns:
            self: Enables method chaining.
        """
        self.objective_list.append(objective)
        return self

    def set_searcher(self, searcher: SearcherType) -> "Modeller":
        """
        Defines the search strategy for solving the model.

        Args:
            searcher: A valid SearcherType.

        Returns:
            self: Enables method chaining.
        """
        self.searcher = searcher
        return self

    def set_cutoff(self, cutoff: Cutoff | None) -> "Modeller":
        """
        Sets a cutoff condition to terminate optimization early.

        Args:
            cutoff: A Cutoff instance representing a configurable limit.

        Returns:
            self: Enables method chaining.
        """
        self.cutoff = cutoff
        return self

    def set_callback_url(self, callback_url: str) -> "Modeller":
        """
        Specifies a callback URL to receive results upon solution completion.

        Args:
            callback_url: A valid HTTP/HTTPS URL.

        Returns:
            self: Enables method chaining.
        """
        self.callback_url = callback_url
        return self

    def set_solution_limit(self, solution_limit: int) -> "Modeller":
        """
        Sets the maximum number of solutions to return.

        Args:
            solution_limit: The maximum number of solutions.

        Returns:
            self: Enables method chaining.
        """
        self.solution_limit = solution_limit
        return self

    def to_json(self, serialization: bool = False) -> dict:
        """
        Serializes the model into a JSON-compatible dictionary
        for submission to a solver engine.

        Args:
            serialization: False if the serialization is made for Qaekwy Engine.

        Returns:
            dict: JSON representation of the optimization model.

        Raises:
            ModelFailure: If no searcher is defined before export.
        """
        if self.searcher is None and serialization is False:
            raise ModelFailure(
                "No SearcherType defined. Use 'set_searcher' before exporting the model."
            )

        model_json: dict[str, Any] = {
            "var": [v.to_json() for v in self.variable_list if v is not None],
            "constraint": [c.to_json() for c in self.constraint_list if c is not None],
            "specific": [o.to_json() for o in self.objective_list if o is not None],
            "solution_limit": self.solution_limit,
        }

        if self.searcher is not None and not serialization:
            model_json["searcher"] = self.searcher.value

        if self.cutoff:
            key = "meta_cutoff" if self.cutoff.is_meta() else "cutoff"
            model_json[key] = self.cutoff.to_json()

        if self.callback_url:
            model_json["callback_url"] = str(self.callback_url)

        return model_json

    @staticmethod
    def _constraints_factory(
        constraint_data: dict, variable_list: list[Union[Variable, ArrayVariable]]
    ) -> AbstractConstraint:
        """
        Factory method to create a Constraint instance from JSON data.

        Args:
            constraint_data (dict): A dictionary containing constraint information.
            variable_list (list[Union[Variable, ArrayVariable]]): A list of Variable instances.

        Returns:
            AbstractConstraint: An AbstractConstraint instance.
        """
        if constraint_data.get("type") == "abs":
            return ConstraintAbs.from_json(constraint_data, variable_list)
        if constraint_data.get("type") == "acos":
            return ConstraintACos.from_json(constraint_data, variable_list)
        if constraint_data.get("type") == "asin":
            return ConstraintASin.from_json(constraint_data, variable_list)
        if constraint_data.get("type") == "atan":
            return ConstraintATan.from_json(constraint_data, variable_list)
        if constraint_data.get("type") == "cos":
            return ConstraintCos.from_json(constraint_data, variable_list)
        if constraint_data.get("type") == "distinct_array":
            return ConstraintDistinctArray.from_json(constraint_data, variable_list)
        if constraint_data.get("type") == "distinct_col":
            return ConstraintDistinctCol.from_json(constraint_data, variable_list)
        if constraint_data.get("type") == "distinct_row":
            return ConstraintDistinctRow.from_json(constraint_data, variable_list)
        if constraint_data.get("type") == "distinct_slice":
            return ConstraintDistinctSlice.from_json(constraint_data, variable_list)
        if constraint_data.get("type") == "divide":
            return ConstraintDivide.from_json(constraint_data, variable_list)
        if constraint_data.get("type") == "element":
            return ConstraintElement.from_json(constraint_data, variable_list)
        if constraint_data.get("type") == "exponential":
            return ConstraintExponential.from_json(constraint_data, variable_list)
        if constraint_data.get("type") == "logarithm":
            return ConstraintLogarithm.from_json(constraint_data, variable_list)
        if constraint_data.get("type") == "maximum":
            return ConstraintMaximum.from_json(constraint_data, variable_list)
        if constraint_data.get("type") == "minimum":
            return ConstraintMinimum.from_json(constraint_data, variable_list)
        if constraint_data.get("type") == "modulo":
            return ConstraintModulo.from_json(constraint_data, variable_list)
        if constraint_data.get("type") == "member":
            return ConstraintMember.from_json(constraint_data, variable_list)
        if constraint_data.get("type") == "multiply":
            return ConstraintMultiply.from_json(constraint_data, variable_list)
        if constraint_data.get("type") == "nroot":
            return ConstraintNRoot.from_json(constraint_data, variable_list)
        if constraint_data.get("type") == "power":
            return ConstraintPower.from_json(constraint_data, variable_list)
        if constraint_data.get("type") == "rel":
            return RelationalExpression.from_json(constraint_data)
        if constraint_data.get("type") == "sin":
            return ConstraintSin.from_json(constraint_data, variable_list)
        if constraint_data.get("type") == "sorted":
            return ConstraintSorted.from_json(constraint_data, variable_list)
        if constraint_data.get("type") == "rsorted":
            return ConstraintReverseSorted.from_json(constraint_data, variable_list)
        if constraint_data.get("type") == "tan":
            return ConstraintTan.from_json(constraint_data, variable_list)
        if constraint_data.get("type") == "if_then_else":
            return ConstraintIfThenElse.from_json(constraint_data)

        raise ValueError(f"Unknown constraint type: {constraint_data.get('type')}")

    @staticmethod
    def from_json(json_data: dict) -> "Modeller":
        """
        Creates a Modeller instance from a JSON representation.

        Args:
            json_data (dict): A dictionary containing model information in JSON format.

        Returns:
            Modeller: A Modeller instance.
        """
        modeller = Modeller()
        modeller.variable_list = (
            [Variable.from_json(v) for v in json_data.get("var", []) if v is not None]
            + [
                ArrayVariable.from_json(v)
                for v in json_data.get("var", [])
                if v is not None
            ]
            + [
                MatrixVariable.from_json(v)
                for v in json_data.get("var", [])
                if v is not None
            ]
        )
        modeller.constraint_list = []
        for c in json_data.get("constraint", []):
            constraint = Modeller._constraints_factory(c, modeller.variable_list)
            modeller.constraint_list.append(constraint)

        modeller.objective_list = [
            (
                SpecificMinimum.from_json(o, modeller.variable_list)
                if o.get("type") == "minimize"
                else SpecificMaximum.from_json(o, modeller.variable_list)
            )
            for o in json_data.get("specific", [])
        ]

        cutoff_data = json_data.get("meta_cutoff") or json_data.get("cutoff")
        if cutoff_data:
            modeller.cutoff = Cutoff.from_json(cutoff_data)

        modeller.set_solution_limit(int(json_data.get("solution_limit", 1)))
        modeller.set_callback_url(str(json_data.get("callback_url")))

        return modeller
