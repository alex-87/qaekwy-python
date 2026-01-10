"""Solution Class

This module defines the Solution class, which represents a solution to a model.

Classes:
    Solution: Represents a solution to a model.

"""


class Solution(dict):
    """
    Represents a solution to a model.

    The Solution class provides a way to represent a solution to a model in the
    form of a dictionary. It allows easy access to variable assignments and their
    values in the solution.

    Example:
        # A Solution instance with solution JSON content
        solution_content = [
            {"name": "x", "assigned": True, "value": 5},
            {"name": "y", "assigned": True, "value": 10},
            {"name": "z", "assigned": False, "value": None}
        ]
        solution = Solution(solution_content)

        # Access variable assignments and their values in the solution
        x_value = solution["x"]  # Returns 5
        y_value = solution["y"]  # Returns 10
        z_value = solution["z"]  # Returns None

        # Or access variable assignments through the Solution attributes:
        x_value = solution.x  # x_value = 5
        y_value = solution.y  # y_value = 10
        z_value = solution.z  # z_value is None
    """

    def __init__(  # pylint: disable=too-many-locals
        self, solution_json_content: list[dict]
    ) -> None:
        self.solution_json_content = solution_json_content

        for element in self.solution_json_content:
            variable = element["name"]

            if element["assigned"] is True:
                val = element["value"]
            else:
                val = None

            if "position" in element:
                position = element["position"]
                if variable not in self:
                    self[variable] = []

                while len(self[variable]) < position + 1:
                    self[variable].append(None)

                self[variable][position] = val

            else:
                self[variable] = val

        matrix_keys_replacement: list[tuple] = []
        for elem in self.items():
            if isinstance(elem[1], list):
                if elem[0].startswith("MATRIX$"):
                    parts = elem[0].split("$", 3)
                    if len(parts) == 4 and parts[1].isdigit() and parts[2].isdigit():
                        row = int(parts[1])
                        col = int(parts[2])
                        matrix_value = [[None]]
                        rows, cols = row, col
                        flat = elem[1]
                        matrix_value = [
                            flat[i * cols : (i + 1) * cols] for i in range(rows)
                        ]
                        matrix_keys_replacement.append(
                            (elem[0], parts[3], matrix_value)
                        )
                        elem = (parts[3], matrix_value)

            self.__setattr__(elem[0], elem[1])

        for original_key, new_key, original_value in matrix_keys_replacement:
            self[new_key] = original_value
            self.__delitem__(original_key)

    def __repr__(self) -> str:
        return f"Solution({super().__repr__()})"

    def pretty_print(self) -> None:
        """
        Pretty prints the solution in a readable format, handling scalars, arrays, and matrices.
        """
        if not self:
            print("Empty solution")
            return

        print("-" * 40)
        print("Solution:")
        print("-" * 40)

        def display_name(key):
            if key.startswith("MATRIX$"):
                parts = key.split("$", 3)
                return parts[3] if len(parts) == 4 else key
            return key

        sorted_keys = sorted(self.keys(), key=display_name)
        max_name_length = max(len(display_name(k)) for k in sorted_keys)

        for key in sorted_keys:
            value = self[key]
            name = display_name(key)

            if value is None:
                print(f"{name:<{max_name_length}}: unassigned")
            elif isinstance(value, list):
                if value and isinstance(value[0], list):
                    rows = len(value)
                    cols = len(value[0]) if value else 0
                    print(f"{name}: ({rows} x {cols} matrix)")
                    for row in value:
                        formatted = " ".join(
                            str(cell) if cell is not None else "-" for cell in row
                        )
                        print(f"    {formatted}")
                else:
                    formatted = ", ".join(
                        str(v) if v is not None else "-" for v in value
                    )
                    print(f"{name:<{max_name_length}}: [{formatted}]")
            else:
                print(f"{name:<{max_name_length}}: {value}")

        print("-" * 40)
