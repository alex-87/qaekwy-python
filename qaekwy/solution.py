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

    def __init__(self, solution_json_content: list) -> None:
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

        for elem in self.items():
            self.__setattr__(elem[0], elem[1])
