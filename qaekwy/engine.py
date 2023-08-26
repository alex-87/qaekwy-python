"""
The `qaekwy.engine` module provides classes and utilities for interacting with the
optimization engine.

This module defines classes that encapsulate various actions that can be performed
on the optimization engine, such as sending requests, retrieving responses, and interacting
with the engine's functionality. It also includes utilities for handling responses and
model submissions.

This module also defines the ClusterEngine class, which extends the Engine class to interact
with a cluster-based optimization engine, as well as the DirectEngine class to interact with
the Cloud-hosted instance.

Classes:
    AbstractAction: Base class for defining actions to be performed on the optimization engine.
    EchoAction: Action class to send an 'echo' request and retrieve the echo from the engine.
    VersionAction: Action class to request the version information of the optimization engine.
    ResetAction: Action class to reset the state of the optimization engine.
    StopAction: Action class to stop the optimization engine.
    StatusAction: Action class to check the status of the optimization engine.
    ModelAction: Action class to submit a model for optimization to the engine.
    CurrentModelAction: Action class to retrieve the current model from the optimization engine.
    SolutionAction: Action class to retrieve the solution from the optimization engine.
    Engine: Class representing the optimization engine and providing methods for interaction.
    CurrentExplainAction: Represents an action to retrieve the current explanation.
    ExplainAction: Represents an action to request an explanation for a model.
    CleanAction: Represents an action to clean the engine's environment.
    ClusterStatusAction: Represents an action to check the cluster's health status.
    RemoveNodeAction: Represents an action to remove a node from the cluster.
    EnableNodeAction: Represents an action to enable a disabled node in the cluster.
    DisableNodeAction: Represents an action to disable a node in the cluster.
    ClusterEngine: Extends the Engine class to interact with a cluster-based optimization engine.

Utilities:
    AbstractResponse: Base class for defining responses received from the optimization engine.
    EchoResponse: Class representing the response received from the 'echo' request.
    VersionResponse: Class representing the response received from the 'version' request.
    StatusResponse: Class representing the response received from various status-related requests.
    ModelJSonResponse: Class representing the response received after submitting a model.
    SolutionResponse: Class representing the response received containing solution information.
    Modeller: Class for creating and managing optimization models.

Usage:
    # Create an Engine client instance to connect to the endpoint URL
    engine = Engine(endpoint="http://localhost:8000")

    # Send an 'echo' request to the engine
    echo_response = engine.echo()

    # Request the version information of the engine
    version_response = engine.version()

    # Submit a model to the engine for optimization
    model = Modeller()
    model.add_variable(...)
    model.add_constraint(...)
    model_response = engine.model(model)

    # Retrieve the solution from the engine
    solution_response = engine.solution()
    list_of_solutions = solution_response.get_solutions()

    # Reset the engine's state
    reset_response = engine.reset()

    # Check the status of the engine
    status_response = engine.status()

Note:
    The classes and utilities provided by this module are designed to facilitate
    communication and interaction with the optimization engine. They abstract away
    the details of request creation and response handling, allowing developers to
    focus on utilizing the engine's capabilities without dealing with low-level HTTP
    operations.

"""

from abc import ABC, abstractmethod

import json
import requests
from qaekwy.model import DIRECTENGINE_API_ENDPOINT
from qaekwy.model.modeller import Modeller

from qaekwy.response import (
    AbstractResponse,
    ClusterStatusResponse,
    EchoResponse,
    ExplanationResponse,
    ModelJSonResponse,
    SolutionResponse,
    StatusResponse,
    VersionResponse,
)


class AbstractAction(ABC):
    """
    Base abstract class for defining actions to be performed on the optimization engine.

    This class defines the common structure and behavior for various actions that can be
    executed on the optimization engine. It provides methods for executing the action and
    defining the abstract method 'action()' that should be implemented by concrete action classes.

    Methods:
        execute(): Execute the action and return the response from the engine.
        action(): Abstract method to be implemented by concrete action classes.
    """

    def __init__(self, endpoint: str, command: str, body: str = None) -> None:
        """
        Initialize an AbstractAction instance.

        Args:
            endpoint (str): The endpoint URL of the optimization engine.
            command (str): The command to be executed on the engine.
            body (str): The optional body of the request (default is None).
        """
        super().__init__()
        self.endpoint = endpoint
        self.command = command
        self.body = body

    def execute(self) -> requests.Response:
        """
        Execute the action on the optimization engine and return the response.

        Returns:
            requests.Response: The response from the optimization engine.
        """

        res = None

        if len(self.endpoint) < 6:
            return None

        request_line = self.endpoint
        if self.endpoint[len(self.endpoint) - 1] != "/":
            request_line = request_line + "/" + self.command
        else:
            request_line = request_line + self.command

        if self.body is None:
            res = requests.get(request_line, timeout=30)
        else:
            res = requests.post(request_line, self.body, timeout=30)

        return res

    @abstractmethod
    def action(self) -> AbstractResponse:
        """
        Abstract method to be implemented by concrete action classes.
        Represents the specific action to be performed on the engine.

        Returns:
            AbstractResponse: The response from the optimization engine.
        """


class EchoAction(AbstractAction):
    """
    Action class to perform an 'echo' request on the optimization engine.

    This class defines an action to send an 'echo' request to the optimization engine
    and retrieve an echo response.

    Methods:
        action(): Execute the 'echo' action and return the echo response.
    """

    def __init__(self, endpoint: str) -> None:
        """
        Initialize an EchoAction instance.

        Args:
            endpoint (str): The endpoint URL of the optimization engine.
        """
        super().__init__(endpoint, "echo", "ECHO")

    def action(self) -> EchoResponse:
        """
        Execute the 'echo' action on the optimization engine and return the echo response.

        Returns:
            EchoResponse: The echo response from the optimization engine.
        """
        res = self.execute()

        if res is None:
            return None

        return EchoResponse(str(res.content))


class VersionAction(AbstractAction):
    """
    Action class to perform a 'version' request on the optimization engine.

    This class defines an action to request the version information of the optimization engine.

    Methods:
        action(): Execute the 'version' action and return the version response.
    """

    def __init__(self, endpoint: str) -> None:
        """
        Initialize a VersionAction instance.

        Args:
            endpoint (str): The endpoint URL of the optimization engine.
        """
        super().__init__(endpoint, "version")

    def action(self) -> VersionResponse:
        """
        Execute the 'version' action on the optimization engine and return the version response.

        Returns:
            VersionResponse: The version response from the optimization engine.
        """
        res = self.execute()

        if res is None:
            return None

        return VersionResponse(res.json())


class ResetAction(AbstractAction):
    """
    Action class to perform a 'reset' request on the optimization engine.

    This class defines an action to request the version information of the optimization engine.

    Methods:
        action(): Execute the 'reset' action and return the version response.
    """

    def __init__(self, endpoint: str) -> None:
        """
        Initialize a ResetAction instance.

        Args:
            endpoint (str): The endpoint URL of the optimization engine.
        """
        super().__init__(endpoint, "reset")

    def action(self) -> StatusResponse:
        """
        Execute the 'reset' action on the optimization engine and return the status response.

        Returns:
            StatusResponse: The status response from the optimization engine.
        """
        res = self.execute()

        if res is None:
            return None

        return StatusResponse(res.json())


class StopAction(AbstractAction):
    """
    Action class to perform a 'stop' request on the optimization engine.

    This class defines an action to request the version information of the optimization engine.

    Methods:
        action(): Execute the 'stop' action and return the version response.
    """

    def __init__(self, endpoint: str) -> None:
        """
        Initialize a StopAction instance.

        Args:
            endpoint (str): The endpoint URL of the optimization engine.
        """
        super().__init__(endpoint, "stop")

    def action(self) -> AbstractResponse:
        """
        Execute the 'stop' action on the optimization engine and return the status response.

        Returns:
            StatusResponse: The status response from the optimization engine.
        """
        res = self.execute()

        if res is None:
            return None

        return StatusResponse(res.json())


class StatusAction(AbstractAction):
    """
    Action class to perform a 'status' request on the optimization engine.

    This class defines an action to request the version information of the optimization engine.

    Methods:
        action(): Execute the 'status' action and return the version response.
    """

    def __init__(self, endpoint: str) -> None:
        """
        Initialize a StatusAction instance.

        Args:
            endpoint (str): The endpoint URL of the optimization engine.
        """
        super().__init__(endpoint, "status")

    def action(self) -> StatusResponse:
        """
        Execute the 'status' action on the optimization engine and return the status response.

        Returns:
            StatusResponse: The status response from the optimization engine.
        """
        res = self.execute()

        if res is None:
            return None

        return StatusResponse(res.json())


class ModelAction(AbstractAction):
    """
    Action class to perform a 'model' request on the optimization engine.

    This class defines an action to request the version information of the optimization engine.

    Methods:
        action(): Execute the 'model' action and return the status response.
    """

    def __init__(self, endpoint: str, model: Modeller) -> None:
        """
        Initialize a ModelAction instance.

        Args:
            endpoint (str): The endpoint URL of the optimization engine.
        """
        super().__init__(endpoint, "model", json.dumps(model.to_json()))

    def action(self) -> StatusResponse:
        """
        Execute the 'model' action on the optimization engine and return the StatusResponse
        response.

        Returns:
            StatusResponse: The response from the optimization engine.
        """
        res = self.execute()

        if res is None:
            return None

        return StatusResponse(res.json())


class DirectModelAction(AbstractAction):
    """
    Action class to perform a 'model' request on the optimization engine. This class
    perfoms the exact same action as ModelAction, but expects a solution object to be
    returned instead of the status.

    This class defines an action to request the version information of the optimization engine.

    Methods:
        action(): Execute the 'model' action and return the solution response.
    """

    def __init__(self, endpoint: str, model: Modeller) -> None:
        """
        Initialize a ModelAction instance.

        Args:
            endpoint (str): The endpoint URL of the optimization engine.
        """
        super().__init__(endpoint, "model", json.dumps(model.to_json()))

    def action(self) -> SolutionResponse:
        """
        Execute the 'model' action on the optimization engine and return the ModelJSon response.

        Returns:
            SolutionResponse: The response from the optimization engine.
        """
        res = self.execute()

        if res is None:
            return None

        return SolutionResponse(res.json())


class CurrentModelAction(AbstractAction):
    """
    Action class to perform a 'current' request on the optimization engine.

    This class defines an action to request the version information of the optimization engine.

    Methods:
        action(): Execute the 'current' action and return the version response.
    """

    def __init__(self, endpoint: str) -> None:
        """
        Initialize a CurrentModelnAction instance.

        Args:
            endpoint (str): The endpoint URL of the optimization engine.
        """
        super().__init__(endpoint, "current")

    def action(self) -> ModelJSonResponse:
        """
        Execute the 'current' action on the optimization engine and return
        the current model response.

        Returns:
            ModelJSonResponse: The current model from the optimization engine.
        """
        res = self.execute()

        if res is None:
            return None

        return ModelJSonResponse(res.json())


class SolutionAction(AbstractAction):
    """
    Action class to perform a 'result' request on the optimization engine.

    This class defines an action to request the version information of the optimization engine.

    Methods:
        action(): Execute the 'result' action and return the version response.
    """

    def __init__(self, endpoint: str) -> None:
        """
        Initialize a SolutionAction instance.

        Args:
            endpoint (str): The endpoint URL of the optimization engine.
        """
        super().__init__(endpoint, "result")

    def action(self) -> SolutionResponse:
        """
        Execute the 'result' action on the optimization engine and return the solution response.

        Returns:
            EchoResponse: The solution response from the optimization engine.
        """
        res = self.execute()

        if res is None:
            return None

        return SolutionResponse(res.json())


class Engine:
    """
    Class representing the optimization engine and providing methods to interact with it.

    This class serves as an interface for interacting with the optimization engine. It provides
    methods to perform various actions such as requesting version information, submitting a model,
    retrieving solutions, and more.

    Methods:
        echo(): Send an 'echo' request to the engine and retrieve the echo response.
        version(): Request the version information of the engine.
        reset(): Reset the engine's state.
        stop(): Stop the engine.
        status(): Check the status of the engine.
        model(model: Modeller): Submit a model to the engine for optimization.
        current_model(): Retrieve the current model from the engine.
        solution(): Retrieve the solution from the engine.
    """

    def __init__(self, endpoint: str) -> None:
        """
        Initialize an Engine instance.

        Args:
            endpoint (str): The endpoint URL of the optimization engine.
        """
        self.endpoint = endpoint

    def echo(self):
        """
        Send an 'echo' request to the engine and retrieve the echo response.

        Returns:
            EchoResponse: The echo response from the optimization engine.
        """
        return EchoAction(self.endpoint).action()

    def version(self):
        """
        Request the version information of the engine.

        Returns:
            VersionResponse: The version response from the optimization engine.
        """
        return VersionAction(self.endpoint).action()

    def reset(self):
        """
        Reset the engine's state.

        Returns:
            StatusResponse: The status response from the optimization engine.
        """
        return ResetAction(self.endpoint).action()

    def stop(self):
        """
        Stop the engine.

        Returns:
            StatusResponse: The status response from the optimization engine.
        """
        return StopAction(self.endpoint).action()

    def status(self):
        """
        Check the status of the engine.

        Returns:
            StatusResponse: The status response from the optimization engine.
        """
        return StatusAction(self.endpoint).action()

    def model(self, model: Modeller):
        """
        Submit a model to the engine for optimization.

        Args:
            model (Modeller): The model to be submitted.

        Returns:
            ModelJSonResponse: The model submission response from the optimization engine.
        """
        return ModelAction(self.endpoint, model).action()

    def current_model(self):
        """
        Retrieve the current model from the engine.

        Returns:
            ModelJSonResponse: The current model response from the optimization engine.
        """
        return CurrentModelAction(self.endpoint).action()

    def solution(self):
        """
        Retrieve the solution from the engine.

        Returns:
            SolutionResponse: The solution response from the optimization engine.
        """
        return SolutionAction(self.endpoint).action()


class DirectEngine:
    """
    Class representing the Cloud optimization engine demonstration endpoint and providing
    methods to interact with it.

    This Cloud optimization engine is design to handle small modellings and to directly send
    the solution back once a model is submitted.

    Methods:
        echo(): Send an 'echo' request to the engine and retrieve the echo response.
        version(): Request the version information of the engine.
        model(model: Modeller): Submit a model to the engine for optimization and
        receive the solution, if any.
    """

    def __init__(self) -> None:
        """
        Initialize an DirectEngine instance.

        Args:
            endpoint (str): The endpoint URL of the optimization engine.
        """
        self.endpoint = DIRECTENGINE_API_ENDPOINT

    def echo(self):
        """
        Send an 'echo' request to the engine and retrieve the echo response.

        Returns:
            EchoResponse: The echo response from the optimization engine.
        """
        return EchoAction(self.endpoint).action()

    def version(self):
        """
        Request the version information of the engine.

        Returns:
            VersionResponse: The version response from the optimization engine.
        """
        return VersionAction(self.endpoint).action()

    def model(self, model: Modeller):
        """
        Submit a model to the engine for optimization.

        Args:
            model (Modeller): The model to be submitted.

        Returns:
            ModelJSonResponse: The model submission response from the optimization engine.
        """
        return DirectModelAction(self.endpoint, model).action()


###
# Cluster
###


###
# Actions
###


class CurrentExplainAction(
    AbstractAction
):  # pylint: disable=too-many-instance-attributes, too-few-public-methods
    """
    Represents an action to retrieve the current explanation.
    """

    def __init__(self, endpoint: str) -> None:
        super().__init__(endpoint=endpoint, command="explain")

    def action(self) -> ExplanationResponse:
        """
        Execute the action and returns a response.
        """

        ret = self.execute()

        if ret is None:
            return None

        return ExplanationResponse(json.loads(str(ret.content)))


class ExplainAction(AbstractAction):  # pylint: disable=too-few-public-methods
    """
    Represents an action to request an explanation for a model.
    """

    def __init__(self, endpoint: str, model: Modeller) -> None:
        super().__init__(
            endpoint=endpoint, command="explain", body=str(model.to_json())
        )

    def action(self) -> ExplanationResponse:
        """
        Execute the action and returns a response.
        """
        res = self.execute()

        if res is None:
            return None

        return ExplanationResponse(res.json())


class CleanAction(AbstractAction):
    """
    Represents an action to clean the engine's environment.
    """

    def __init__(self, endpoint: str) -> None:
        super().__init__(endpoint=endpoint, command="clean")

    def action(self) -> StatusResponse:
        """
        Execute the action and returns a response.
        """
        res = self.execute()

        if res is None:
            return None

        return StatusResponse(res.json())


class ClusterStatusAction(AbstractAction):
    """
    Represents an action to check the cluster's health status.
    """

    def __init__(self, endpoint: str) -> None:
        super().__init__(endpoint=endpoint, command="healthcheck")

    def action(self) -> AbstractResponse:
        """
        Execute the action and returns a response.
        """

    def get_status(self) -> ClusterStatusResponse:
        """
        Execute the status request and returns a response.
        """


class RemoveNodeAction(AbstractAction):  # pylint: disable=too-few-public-methods
    """
    Represents an action to remove a node from the cluster.
    """

    def __init__(self, endpoint: str, identifier: str) -> None:
        super().__init__(
            endpoint=endpoint,
            command="remove",
            body=json.dumps({"identifier": identifier}),
        )

    def action(self) -> StatusResponse:
        """
        Execute the action and returns a response.
        """
        res = self.execute()

        if res is None:
            return None

        return StatusResponse(res.json())


class EnableNodeAction(AbstractAction):  # pylint: disable=too-few-public-methods
    """
    Represents an action to enable a disabled node in the cluster.
    """

    def __init__(self, endpoint: str, identifier: str) -> None:
        super().__init__(
            endpoint=endpoint,
            command="enable",
            body=json.dumps({"identifier": identifier}),
        )

    def action(self) -> StatusResponse:
        """
        Execute the action and returns a response.
        """
        res = self.execute()

        if res is None:
            return None

        return StatusResponse(res.json())


class DisableNodeAction(AbstractAction):  # pylint: disable=too-few-public-methods
    """
    Represents an action to disable a node in the cluster.
    """

    def __init__(self, endpoint: str, identifier: str) -> None:
        super().__init__(
            endpoint=endpoint,
            command="disable",
            body=json.dumps({"identifier": identifier}),
        )

    def action(self) -> StatusResponse:
        """
        Execute the action and returns a response.
        """
        res = self.execute()

        if res is None:
            return None

        return StatusResponse(res.json())


class ClusterEngine(Engine):
    """
    Extends the Engine class to interact with a cluster-based optimization engine.

    This class provides methods to interact with a cluster-based optimization engine.
    It allows you to perform various actions such as retrieving explanations, checking
    the cluster status, enabling/disabling nodes, and more.

    Methods:
        explain_current(): Retrieve the current explanation from the engine.
        explain(model: Modeller): Request an explanation for the given model.
        clean(): Clean the environment of the engine.
        status(): Check the health status of the cluster.
        remove_node(identifier: str): Remove a node from the cluster by its identifier.
        enable_node(identifier: str): Enable a disabled node in the cluster by its identifier.
        disable_node(identifier: str): Disable a node in the cluster by its identifier.
    """

    def explain_current(self):
        """
        Retrieve the explanation of the current model from the engine.

        Returns:
            ExplanationResponse: The response containing the current explanation.
        """
        return CurrentExplainAction(self.endpoint).action()

    def explain(self, model: Modeller):
        """
        Request an explanation for the given model.

        Args:
            model (Modeller): The model for which to request an explanation.

        Returns:
            ExplanationResponse: The response containing the explanation for the model.
        """
        return ExplainAction(self.endpoint, model).action()

    def clean(self):
        """
        Clean the environment of the engine.

        Returns:
            StatusResponse: The response indicating the success of the clean operation.
        """
        return CleanAction(self.endpoint).action()

    def status(self):
        """
        Check the health status of the cluster.

        Returns:
            ClusterStatusResponse: The response containing the cluster's health status.
        """
        return ClusterStatusAction(self.endpoint).action()

    def remove_node(self, identifier: str):
        """
        Remove a node from the cluster by its identifier.

        Args:
            identifier (str): The identifier of the node to be removed.

        Returns:
            StatusResponse: The response indicating the success of the node removal.
        """
        return RemoveNodeAction(self, identifier).action

    def disable_node(self, identifier: str):
        """
        Disable a node in the cluster by its identifier.

        Args:
            identifier (str): The identifier of the node to be disabled.

        Returns:
            StatusResponse: The response indicating the success of disabling the node.
        """
        return DisableNodeAction(self, identifier).action

    def enable_node(self, identifier: str):
        """
        Enable a disabled node in the cluster by its identifier.

        Args:
            identifier (str): The identifier of the node to be enabled.

        Returns:
            StatusResponse: The response indicating the success of enabling the node.
        """
        return EnableNodeAction(self, identifier).action
