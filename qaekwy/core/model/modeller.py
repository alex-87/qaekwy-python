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

from typing import Any, Callable, Dict, Optional, Union

from ..exception.model_failure import ModelFailure
from .constraint.abs import ConstraintAbs
from .constraint.abstract_constraint import AbstractConstraint
from .constraint.acos import ConstraintACos
from .constraint.asin import ConstraintASin
from .constraint.atan import ConstraintATan
from .constraint.cos import ConstraintCos
from .constraint.distinct import (
    ConstraintDistinctArray,
    ConstraintDistinctCol,
    ConstraintDistinctRow,
    ConstraintDistinctSlice,
)
from .constraint.divide import ConstraintDivide
from .constraint.element import ConstraintElement
from .constraint.exponential import ConstraintExponential
from .constraint.if_then_else import ConstraintIfThenElse
from .constraint.logarithm import ConstraintLogarithm
from .constraint.maximum import ConstraintMaximum
from .constraint.member import ConstraintMember
from .constraint.minimum import ConstraintMinimum
from .constraint.modulo import ConstraintModulo
from .constraint.multiply import ConstraintMultiply
from .constraint.nroot import ConstraintNRoot
from .constraint.power import ConstraintPower
from .constraint.relational import RelationalExpression
from .constraint.sin import ConstraintSin
from .constraint.sort import ConstraintReverseSorted, ConstraintSorted
from .constraint.tan import ConstraintTan
from .cutoff import Cutoff
from .searcher import SearcherType
from .specific import SpecificMaximum, SpecificMinimum
from .variable.variable import (
    ArrayVariable,
    Expression,
    MatrixVariable,
    Variable,
    VariableType,
)

ConstraintFactory = Callable[
    [dict, list[Union[Variable, ArrayVariable, MatrixVariable]]],
    AbstractConstraint,
]


class Modeller:
    """
    Constructs and configures optimization models.

    Attributes:
        variable_list (list[Union[Variable, ArrayVariable, MatrixVariable]]): Collection of model variables.
        constraint_list (list[Union[AbstractConstraint]]): Collection of model constraints.
        objective_list (list[Union[SpecificMinimum, SpecificMaximum]]): Optimization objectives (minimize or maximize).
        searcher (SearcherType): Strategy for searching solution space.
        cutoff (Cutoff): Optional stopping condition.
        callback_url (str): Optional URL for post-solution callback.
        solution_limit (int): Maximum number of solutions to return.
    """

    CONSTRAINT_REGISTRY: Dict[str, ConstraintFactory] = {
        "abs": ConstraintAbs.from_json,
        "acos": ConstraintACos.from_json,
        "asin": ConstraintASin.from_json,
        "atan": ConstraintATan.from_json,
        "cos": ConstraintCos.from_json,
        "distinct_array": ConstraintDistinctArray.from_json,
        "distinct_col": ConstraintDistinctCol.from_json,
        "distinct_row": ConstraintDistinctRow.from_json,
        "distinct_slice": ConstraintDistinctSlice.from_json,
        "divide": ConstraintDivide.from_json,
        "element": ConstraintElement.from_json,
        "exponential": ConstraintExponential.from_json,
        "logarithm": ConstraintLogarithm.from_json,
        "maximum": ConstraintMaximum.from_json,
        "minimum": ConstraintMinimum.from_json,
        "modulo": ConstraintModulo.from_json,
        "member": ConstraintMember.from_json,
        "multiply": ConstraintMultiply.from_json,
        "nroot": ConstraintNRoot.from_json,
        "power": ConstraintPower.from_json,
        "rel": lambda data, _: RelationalExpression.from_json(data),
        "sin": ConstraintSin.from_json,
        "sorted": ConstraintSorted.from_json,
        "rsorted": ConstraintReverseSorted.from_json,
        "tan": ConstraintTan.from_json,
        "if_then_else": lambda data, _: ConstraintIfThenElse.from_json(data),
    }

    def __init__(self) -> None:
        """
        Initializes an empty Modeller instance.
        """
        self.variable_list: list[Union[Variable, ArrayVariable, MatrixVariable]] = []
        self.constraint_list: list[Union[AbstractConstraint]] = []
        self.objective_list: list[Union[SpecificMinimum, SpecificMaximum]] = []
        self.searcher: Optional[SearcherType] = None
        self.cutoff: Optional[Cutoff] = None
        self.callback_url: Optional[str] = None
        self.solution_limit: int = 1

    def add_variable(
        self, variable: Union[Variable, ArrayVariable, MatrixVariable]
    ) -> "Modeller":
        """
        Adds a variable or array of variables to the model.

        Args:
            variable: A single Variable, ArrayVariable or MatrixVariable instance.

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

    def set_cutoff(self, cutoff: Union[Cutoff, None]) -> "Modeller":
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
        constraint_data: dict,
        variable_list: list[Union[Variable, ArrayVariable, MatrixVariable]],
    ) -> AbstractConstraint:
        """
        Factory method to create a Constraint instance from JSON data.
        """
        constraint_type: str = str(constraint_data.get("type"))

        try:
            factory = Modeller.CONSTRAINT_REGISTRY[constraint_type]
        except KeyError as exc:
            raise ValueError(f"Unknown constraint type: {constraint_type}") from exc

        return factory(constraint_data, variable_list)

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

        variable_list: list = []
        array_variable_list: list = []
        matrix_variable_list: list = []
        for v in json_data.get("var", []):
            var_type = VariableType.from_json(v["type"])
            if var_type in [
                VariableType.INTEGER_ARRAY,
                VariableType.FLOAT_ARRAY,
                VariableType.BOOLEAN_ARRAY,
            ]:
                if v.get("subtype", "") == "matrix":
                    matrix_variable_list.append(MatrixVariable.from_json(v))
                else:
                    array_variable_list.append(ArrayVariable.from_json(v))
            elif var_type in [
                VariableType.INTEGER,
                VariableType.FLOAT,
                VariableType.BOOLEAN,
            ]:
                variable_list.append(Variable.from_json(v))

        modeller.variable_list = (
            variable_list + array_variable_list + matrix_variable_list
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
