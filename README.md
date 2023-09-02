# Qaekwy Python Client

*Operational Research at your fingertips.*

The Qaekwy Python Client serves as a powerful tool to interact with the Qaekwy optimization
solver engine through its API. This client provides a convenient and programmatic way to
**create**, **model**, and **solve** optimization problems using Qaekwy, streamlining
the process of **formulating complex problems and finding optimal solutions**.

Qaekwy is small optimization problem solver engine designed to tackle a wide range of
real-world challenges. It provides powerful modeling capabilities and efficient solving
algorithms to find optimal solutions to complex problems.


## Features

- **Modeling Made Easy:** Define variables, constraints, and objective functions seamlessly.
Qaekwy's `Modeller` class helps you create optimization models with clarity and precision.

- **Diverse Constraint Support:** Qaekwy supports various constraint types, from simple arithmetic
to complex mathematical expressions. Create constraints that accurately represent real-world scenarios.

- **Effortless Optimization:** Qaekwy abstracts away the complexities of communication with
optimization engine. Send requests and receive responses using intuitive methods.

- **Flexibility**: You can leverage the Qaekwy Python Client to tailor optimization problems to their specific
needs by utilizing Qaekwy's modelling capabilities. This includes handling various types of constraints,
objectives, and solver algorithms.


## Installation

```shell
pip install qaekwy
```


## Documentation

Explore the [Qaekwy Documentation](https://docs.qaekwy.io) for in-depth guides, examples, and usage details.


## Example

How to use the Qaekwy Python Client to solve a very small optimization problem:

```python
from qaekwy.engine import DirectEngine
from qaekwy.model.constraint.relational import RelationalExpression
from qaekwy.model.specific import SpecificMaximum
from qaekwy.model.variable.integer import IntegerVariable
from qaekwy.model.modeller import Modeller
from qaekwy.model.searcher import SearcherType

# Define the optimization problem using Qaekwy Python Client
class SimpleOptimizationProblem(Modeller):
    def __init__(self):
        super().__init__()

        # Create a integer variables
        x = IntegerVariable(var_name="x", domain_low=0, domain_high=10)
        y = IntegerVariable(var_name="y", domain_low=0, domain_high=10)
        z = IntegerVariable(var_name="z", domain_low=0, domain_high=10)

        # Constraints
        constraint_1 = RelationalExpression(y > 2 * x)
        constraint_2 = RelationalExpression(x >= 4)
        constraint_3 = RelationalExpression(z == y - x)

        # Objective: Maximize z
        self.add_objective(
            SpecificMaximum(variable=z)
        )

        # Add variable and constraint to the problem
        self.add_variable(x)
        self.add_variable(y)
        self.add_variable(z)
        self.add_constraint(constraint_1)
        self.add_constraint(constraint_2)
        self.add_constraint(constraint_3)

        # Set the search strategy
        self.set_searcher(SearcherType.BAB)

# Create a Qaekwy engine for interaction with the freely-available Cloud instance
qaekwy_engine = DirectEngine()

# Create the optimization problem instance
optimization_problem = SimpleOptimizationProblem()

# Request the Qaekwy engine to solve the problem
response = qaekwy_engine.model(model=optimization_problem)

# Retrieve the list of solutions from the response
list_of_solutions = response.get_solutions()

# Print the solution(s) obtained
for solution in list_of_solutions:
    print(f"Optimal solution: x = {solution.x}")
    print(f"Optimal solution: y = {solution.y}")
    print(f"Optimal solution: z = {solution.z}")
```

Output:

```
Optimal solution: x = 4
Optimal solution: y = 10
Optimal solution: z = 6
```

## License

This software is licensed under the **European Union Public License v1.2**
