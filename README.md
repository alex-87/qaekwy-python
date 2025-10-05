# Qaekwy Python Client

*An Open-source Python framework for constraint programming and optimization*

![GitHub License](https://img.shields.io/github/license/alex-87/qaekwy-python) ![PyPI - Version](https://img.shields.io/pypi/v/qaekwy)
 ![PyPI - Downloads](https://img.shields.io/pypi/dm/qaekwy) 

The Qaekwy Python Client serves as a powerful tool to interact with the Qaekwy optimization solver engine through its
API. This client provides a convenient and programmatic way to **create**, **model**, and **solve** optimization problems
by streamlining the process of **formulating complex problems and finding optimal solutions**.

Qaekwy is small optimization problem solver engine designed to  provide
powerful modeling capabilities and efficient solving algorithms to find optimal solutions to complex problems.

## Features

- **Variables**: Supports integer, float, and boolean variables, including arrays for complex models.
- **Constraints**: Offers a wide range of constraints for flexible problem modeling.
- **Optimization**: Minimize or maximize objective functions to find optimal solutions.
- **Flexible Search Strategies**: Choose from algorithms like Depth-First Search (DFS) and Branch and Bound (BAB).


## Documentation

Explore the [Qaekwy Documentation](https://docs.qaekwy.io) for in-depth guides, examples, and usage details.

## Getting Started

### Prerequisites

- **Python 3.12** or higher
- **pip** (Python package manager)

### Installation

```
pip install qaekwy
```

### Verify the installation

```
python -m qaekwy --version
```

### Code

Get started with Qaekwy in just a few steps:

- Create a model by defining:
    - variables
    - constraints
    - objectives (*optional*)
- Run your model and retrieve solutions.

See the Example below for a practical demonstration:

```python
from qaekwy.engine import DirectEngine
from qaekwy.model.specific import SpecificMaximum
from qaekwy.model.variable.integer import (
    IntegerVariable,
    IntegerExpressionVariable
)
from qaekwy.model.modeller import Modeller
from qaekwy.model.searcher import SearcherType

# Define the optimization model
class SimpleOptimizationProblem(Modeller):
    def __init__(self):
        super().__init__()

        # Define integer variables with domain [0, 10]
        x = IntegerVariable("x", domain_low=0, domain_high=10)
        y = IntegerVariable("y", domain_low=0, domain_high=10)
        z = IntegerExpressionVariable("z", expression=y - x)

        # Add variables to the model
        self.add_variable(x).add_variable(y).add_variable(z)

        # Define constraints
        self.add_constraint(y > 2 * x)
        self.add_constraint(x >= 4)

        # Set objective: Maximize z
        self.add_objective(
            SpecificMaximum(variable=z)
        )

        # Set search strategy
        self.set_searcher(SearcherType.BAB)

# Instantiate the cloud-based solver
qaekwy_engine = DirectEngine()

# Build and solve the model
model = SimpleOptimizationProblem()
response = qaekwy_engine.model(model=model)

# Display solutions
for solution in response.get_solutions():
    print(f"Optimal solution:")
    print(f"- x = {solution.x}")
    print(f"- y = {solution.y}")
    print(f"- z = {solution.z}")
```

Output:

```
Optimal solution:
- x = 4
- y = 10
- z = 6
```

## License

- Released under the [European Union Public Licence 1.2 (EUPL 1.2)](https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12).
- Qaekwy backend [Terms & Conditions](https://docs.qaekwy.io/docs/terms-and-conditions/)
