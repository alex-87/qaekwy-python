"""
The `qaekwy.response` module provides classes for representing and handling responses
received from the optimization engine.

This module defines classes that encapsulate different types of responses that can be
received from the optimization engine, such as echo responses, version responses,
status responses, model JSON responses, solution responses, and explanation responses.

Classes:
    AbstractResponse: Base class for defining responses received from the optimization engine.
    EchoResponse: Class representing the response received from an 'echo' request.
    VersionResponse: Class representing the response received from a 'version' request.
    StatusResponse: Class representing the response received from various status-related requests.
    ModelJSonResponse: Class representing the response received after submitting a model.
    NodeStatus: Represents the status of a cluster node.
    SolutionResponse: Class representing the response received containing solution information.
    ExplanationResponse: Class representing the response containing explanation information.

Usage:
    # Create an instance of a response class with response content
    response = EchoResponse(response_content)

    # Retrieve the status from the response
    status = response.get_status()

    # Check if the status is 'Ok'
    is_ok = response.is_status_ok()

    # Retrieve the message from the response
    message = response.get_message()

    # Retrieve the content from the response
    content = response.get_content()

Note:
    The classes provided by this module are designed to encapsulate and facilitate the handling
    of various responses received from the optimization engine. They abstract away the details
    of response structure, allowing developers to easily access relevant information such as
    status, message, and content.

"""
from abc import ABC
from typing import List
import json
from qaekwy.explanation import Explanation

from qaekwy.solution import Solution


class NodeStatus:  # pylint: disable=too-many-instance-attributes, too-few-public-methods
    """
    Represents the status of a cluster node.
    """

    def __init__(  # pylint: disable=too-many-arguments
        self,
        identifier: str,
        url: str,
        is_enabled: bool,
        message: str,
        is_busy: bool,
        number_of_solutions: int,
        is_failed: bool,
        is_awake,
    ) -> None:
        self.identifier = identifier
        self.url = url
        self.is_enabled = is_enabled
        self.message = message
        self.is_busy = is_busy
        self.number_of_solutions = number_of_solutions
        self.is_failed = is_failed
        self.is_awake = is_awake


class AbstractResponse(ABC):
    """
    Abstract base class for defining responses received from the optimization engine.

    Attributes:
        response_content (dict): The content of the response received from the optimization engine.

    Methods:
        get_status(): Retrieve the status from the response.
        is_status_ok(): Check if the status is 'Ok'.
        get_message(): Retrieve the message from the response.
        get_content(): Retrieve the content from the response.

    """

    def __init__(self, response_content) -> None:
        """
        Initialize an AbstractResponse instance.

        Args:
            response_content (dict): The content of the response received
            from the optimization engine.
        """
        super().__init__()
        self.response_content = response_content

    def get_status(self) -> str:
        """
        Retrieve the status from the response.

        Returns:
            str: The status string extracted from the response.
        """
        if "status" not in self.response_content:
            return "Ok"
        return str(self.response_content["status"])

    def is_status_ok(self) -> bool:
        """
        Check if the status is 'Ok'.

        Returns:
            bool: True if the status is 'Ok', False otherwise.
        """
        return bool(self.get_status() == "Ok")

    def get_message(self) -> str:
        """
        Retrieve the message from the response.

        Returns:
            str: The message string extracted from the response.
        """
        if "message" not in self.response_content:
            return ""
        return str(self.response_content["message"])

    def get_content(self) -> any:
        """
        Retrieve the content from the response.

        Returns:
            any: The content extracted from the response.
        """
        if "content" not in self.response_content:
            return self.response_content
        return self.response_content["content"]


class EchoResponse(AbstractResponse):
    """
    Represents a response containing an echoed message from the optimization engine.

    Attributes:
        response_content (dict): The content of the response received from the optimization engine.

    Methods:
        get_status(): Retrieve the status of the response (always returns an empty string).
        is_status_ok(): Check if the response status is OK (always returns True).
        get_message(): Retrieve the echoed message from the response.
        get_content(): Retrieve the content of the response.

    """

    def get_status(self) -> str:
        """
        Retrieve the status of the response.

        Returns:
            str: The status of the response (always an empty string).
        """
        return ""

    def is_status_ok(self) -> bool:
        """
        Check if the response status is OK.

        Returns:
            bool: True, indicating that the response status is always OK.
        """
        return True

    def get_message(self) -> str:
        """
        Retrieve the echoed message from the response.

        Returns:
            str: The echoed message extracted from the response.
        """
        return str(self.response_content)

    def get_content(self) -> any:
        """
        Retrieve the content of the response.

        Returns:
            any: The content of the response, which is the echoed message.
        """
        return str(self.response_content)


class ModelJSonResponse(AbstractResponse):
    """
    ModelJSonResponse class represents a response containing a JSON representation of a model.
    """


class StatusResponse(AbstractResponse):
    """
    Represents a response containing status information from the optimization engine.

    Attributes:
        response_content (dict): The content of the response received from the optimization engine.

    Methods:
        get_status(): Retrieve the status of the response.
        is_status_ok(): Check if the response status is OK.
        get_message(): Retrieve the message from the response.
        get_type(): Retrieve the type of the status response.
        get_code(): Retrieve the code associated with the status response.
        is_busy(): Check if the engine is currently busy.
        get_number_of_solution_found(): Retrieve the number of solutions found by the engine.

    """

    def get_type(self) -> str:
        """
        Retrieve the type of the status response.

        Returns:
            str: The type of the status response, or an empty string if not present in the response.
        """
        if "type" in self.response_content:
            return str(self.response_content["type"])
        return ""

    def get_code(self) -> int:
        """
        Retrieve the code associated with the status response.

        Returns:
            int: The code associated with the status response, or -1 if not present in the response.
        """
        if "code" in self.response_content:
            return int(self.response_content["code"])
        return -1

    def is_busy(self) -> bool:
        """
        Check if the engine is currently busy.

        Returns:
            bool: True if the engine is busy, False otherwise.
        """
        if "busy_node" in self.response_content:
            return bool(self.response_content["busy_node"])
        return False

    def get_number_of_solution_found(self) -> int:
        """
        Retrieve the number of solutions found by the engine.

        Returns:
            int: The number of solutions found, or -1 if not present in the response.
        """
        if "current_solution_found" in self.response_content:
            return int(self.response_content["current_solution_found"])
        return -1


class SolutionResponse(AbstractResponse):
    """
    Represents a response containing solutions from the optimization engine.

    Attributes:
        response_content (dict): The content of the response received from the optimization engine.

    Methods:
        get_status(): Retrieve the status of the response.
        is_status_ok(): Check if the response status is OK.
        get_message(): Retrieve the message from the response.
        get_solutions(): Retrieve a list of solutions provided by the engine.

    """

    def get_solutions(self) -> List[Solution]:
        """
        Retrieve a list of solutions provided by the engine.

        Returns:
            List[Solution]: A list of Solution objects representing the solutions.
                          Returns None if the response status is not OK.
        """
        if not self.is_status_ok():
            return None
        return [Solution(c) for c in self.get_content()]


class ExplanationResponse(AbstractResponse):
    """
    Represents a response containing explanations from the optimization engine.

    Attributes:
        response_content (dict): The content of the response received from the optimization engine.

    Methods:
        get_status(): Retrieve the status of the response.
        is_status_ok(): Check if the response status is OK.
        get_message(): Retrieve the message from the response.
        get_explanation(): Retrieve an Explanation object containing explanations.

    """

    def get_explanation(self) -> Explanation:
        """
        Retrieve an Explanation object containing explanations provided by the engine.

        Returns:
            Explanation: An Explanation object representing the explanations.
                         Returns None if the response status is not OK.
        """
        if not self.is_status_ok():
            return None
        return Explanation(self.get_content())


class VersionResponse(AbstractResponse):
    """
    Represents a response containing version information from the optimization engine.

    Attributes:
        response_content (dict): The content of the response received from the optimization engine.

    Methods:
        get_status(): Retrieve the status of the response.
        is_status_ok(): Check if the response status is OK.
        get_message(): Retrieve the message from the response.
        get_app(): Retrieve the name of the application.
        get_author(): Retrieve the author of the application.
        get_version(): Retrieve the version of the application.
        get_version_major(): Retrieve the major version number of the application.
        get_version_minor(): Retrieve the minor version number of the application.
        get_version_build(): Retrieve the build version number of the application.
        get_release(): Retrieve the release information of the application.

    """

    def get_app(self) -> str:
        """
        Retrieve the name of the application.

        Returns:
            str: The name of the application.
        """
        return self.response_content["app"]

    def get_author(self) -> str:
        """
        Retrieve the name of the author of the application.

        Returns:
            str: The author of the application.
        """
        return self.response_content["author"]

    def get_version(self) -> str:
        """
        Retrieve the version of the application.

        Returns:
            str: The version of the application.
        """
        return self.response_content["version"]

    def get_version_major(self) -> int:
        """
        Retrieve the major version number of the application.

        Returns:
            int: The major version number of the application.
        """
        return self.response_content["version_major"]

    def get_version_minor(self) -> int:
        """
        Retrieve the minor version number of the application.

        Returns:
            int: The minor version number of the application.
        """
        return self.response_content["version_minor"]

    def get_version_build(self) -> int:
        """
        Retrieve the build version number of the application.

        Returns:
            int: The build version number of the application.
        """
        return self.response_content["version_build"]

    def get_release(self) -> str:
        """
        Retrieve the release information of the application.

        Returns:
            str: The release information of the application.
        """
        return self.response_content["version_release"]


class ClusterStatusResponse:  # pylint: disable=too-few-public-methods
    """
    Represents a response containing cluster status information from the optimization engine.

    Attributes:
        response_content (str): The content of the response received from the optimization engine.
        node_status_list (list[NodeStatus]): A list of NodeStatus instances.

    Methods:
        get_node_status_list(): Retrieve the list of NodeStatus instances.

    """

    def __init__(self, response_content):
        """
        Initialize a ClusterStatusResponse instance.

        Args:
            response_content (str): The content of the response received from
            the optimization engine.
        """
        node_status_list = []
        j = json.loads(response_content)

        if isinstance(j, list):
            for node in j:
                node_status_list.append(
                    NodeStatus(
                        identifier=node["identifier"],
                        url=node["url"],
                        is_enabled=node["enabled"],
                        message=node["message"],
                        is_busy=node["busy_node"],
                        number_of_solutions=node["current_solution_found"],
                        is_failed=node["failure"],
                        is_awake=node["awake"],
                    )
                )

            self.node_status_list = node_status_list
