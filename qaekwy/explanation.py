"""Explanation Class

This module defines the Explanation class, which represents an explanation for a model.

Classes:
    Explanation: Represents an explanation for a model.

"""


class Explanation:
    """
    Represents an explanation for a model.

    The Explanation class provides methods to extract variable and constraint explanations
    from the explanation JSON content. It allows users to easily retrieve explanations for
    variables and constraints provided in the explanation content.

    Attributes:
        explanation_content (list): A list containing JSON content representing the explanation.

    Methods:
        __init__(explanation_content): Initialize an Explanation instance with JSON content.
        get_variables(): Extract and return explanations for variables.
        get_constraints(): Extract and return explanations for constraints.
    """

    def __init__(self, explanation_content: list) -> None:
        self.explanation_content = explanation_content

    def get_variables(self) -> dict:
        """
        Extract and return explanations for variables.

        Returns:
            dict: A dictionary containing variable explanations with variable names as keys.

        """
        dico_final = {}
        for element in self.explanation_content:
            variable_name = element["name"]
            variable_type = element["type"]
            variable_expl = element["explanation"]

            if element["type"] == "var":
                dico_final[variable_name] = {
                    "type": variable_type,
                    "explanation": variable_expl,
                }

        return dico_final

    def get_constraints(self) -> dict:
        """
        Extract and return explanations for constraints.

        Returns:
            dict: A dictionary containing constraint explanations with constraint names as keys.

        """
        dico_final = {}
        for element in self.explanation_content:
            constraint_name = element["name"]
            constraint_type = element["type"]
            constraint_expl = element["explanation"]

            if element["type"] == "constraint":
                dico_final[constraint_name] = {
                    "type": constraint_type,
                    "explanation": constraint_expl,
                }

        return dico_final
