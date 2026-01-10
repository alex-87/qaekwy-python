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
    DirectEngine: Class representing the Cloud instance optimization engine.
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
    # Create a DirectEngine client instance to connect to the cloud endpoint
    engine = DirectEngine()

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
    if solution_response and solution_response.get_solutions():
        for sol in solution_response.get_solutions():
            print(sol)

Note:
    The classes and utilities provided by this module are designed to facilitate
    communication and interaction with the optimization engine. They abstract away
    the details of request creation and response handling, allowing developers to
    focus on utilizing the engine's capabilities without dealing with low-level HTTP
    operations.

"""

import json
from abc import ABC, abstractmethod
from typing import Any, Optional

import requests

from ..__metadata__ import __software__, __version__
from .model import DIRECTENGINE_API_ENDPOINT
from .model.modeller import Modeller
from .response import (
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
    """Base abstract class for defining actions on the optimization engine.

    This class provides a common interface for all actions that can be performed
    on the optimization engine. It handles the communication with the engine's
    endpoint and provides a method for executing the action.

    Subclasses must implement the `action` method to perform the specific
    action.

    Attributes:
        endpoint (str): The endpoint URL of the optimization engine.
        command (str): The command to be executed on the engine.
        body (Optional[Any]): The optional body of the request.
        timeout (Optional[int]): The timeout for the request in seconds.
        ssl_verify (Optional[bool]): Whether to verify SSL certificates.
    """

    def __init__(
        self,
        endpoint: str,
        command: str,
        body: Optional[Any] = None,
        timeout: Optional[int] = 3600,
        ssl_verify: Optional[bool] = True,
    ) -> None:
        """Initializes an AbstractAction instance.

        Args:
            endpoint: The endpoint URL of the optimization engine.
            command: The command to be executed on the engine.
            body: The optional body of the request (default is None).
            timeout: The timeout for the request in seconds.
            ssl_verify: Whether to verify SSL certificates.
        """
        super().__init__()
        self.endpoint = endpoint
        self.command = command
        self.body = body
        self.timeout = timeout
        self.ssl_verify = ssl_verify

    def execute(self) -> requests.Response:
        """Executes the action on the optimization engine and returns the response.

        Returns:
            The response from the optimization engine.

        Raises:
            requests.HTTPError: If the response status code is 401 (Unauthorized),
                or if another HTTP error occurs.
            requests.RequestException: For network-related issues such as
                timeouts or connection errors.
        """
        headers = {
            "User-Agent": f"{__software__}/{__version__}",
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Accept-Encoding": "gzip, deflate",
            "Cache-Control": "no-cache",
        }

        request_line = f"{self.endpoint.rstrip('/')}/{self.command}"

        # Execute the request
        res: Optional[requests.Response] = None

        try:
            if self.body is None:
                res = requests.get(
                    request_line,
                    timeout=self.timeout,
                    headers=headers,
                    verify=self.ssl_verify,
                )
            else:
                res = requests.post(
                    request_line,
                    json=self.body,
                    timeout=self.timeout,
                    headers=headers,
                    verify=self.ssl_verify,
                )

            res.raise_for_status()

        except requests.HTTPError as e:
            raise requests.HTTPError(
                f"HTTP error occurred: {e.response.status_code} - {e.response.text}"
            ) from e

        except requests.RequestException as e:
            raise requests.RequestException(f"Request error occurred: {e}") from e

        return res

    @abstractmethod
    def action(self) -> Optional[AbstractResponse]:
        """Abstract method to be implemented by concrete action classes.

        This method should execute the specific action and return a response
        object.

        Returns:
            The response from the optimization engine.
        """


class EchoAction(AbstractAction):
    """Action class to perform an 'echo' request on the optimization engine.

    This class defines an action to send an 'echo' request to the optimization
    engine and retrieve an echo response.
    """

    def __init__(
        self,
        endpoint: str,
        timeout: Optional[int] = 3600,
        ssl_verify: Optional[bool] = True,
    ) -> None:
        """Initializes an EchoAction instance.

        Args:
            endpoint: The endpoint URL of the optimization engine.
            timeout: The timeout for the request in seconds.
            ssl_verify: Whether to verify SSL certificates.
        """
        super().__init__(
            endpoint, "echo", "ECHO", timeout=timeout, ssl_verify=ssl_verify
        )

    def action(self) -> Optional[EchoResponse]:
        """Executes the 'echo' action on the optimization engine.

        Returns:
            The echo response from the optimization engine.

        Raises:
            requests.HTTPError: If an HTTP error occurs.
            requests.RequestException: For network-related issues.
        """
        res = self.execute()

        return EchoResponse(str(res.content))


class VersionAction(AbstractAction):
    """Action class to perform a 'version' request on the optimization engine.

    This class defines an action to request the version information of the
    optimization engine.
    """

    def __init__(
        self,
        endpoint: str,
        timeout: Optional[int] = 3600,
        ssl_verify: Optional[bool] = True,
    ) -> None:
        """Initializes a VersionAction instance.

        Args:
            endpoint: The endpoint URL of the optimization engine.
            timeout: The timeout for the request in seconds.
            ssl_verify: Whether to verify SSL certificates.
        """
        super().__init__(endpoint, "version", timeout=timeout, ssl_verify=ssl_verify)

    def action(self) -> Optional[VersionResponse]:
        """Executes the 'version' action on the optimization engine.

        Returns:
            The version response from the optimization engine.

        Raises:
            requests.HTTPError: If an HTTP error occurs.
            requests.RequestException: For network-related issues.
        """
        res = self.execute()

        return VersionResponse(res.json())


class ResetAction(AbstractAction):
    """Action class to perform a 'reset' request on the optimization engine.

    This class defines an action to reset the optimization engine.
    """

    def __init__(self, endpoint: str) -> None:
        """Initializes a ResetAction instance.

        Args:
            endpoint: The endpoint URL of the optimization engine.
        """
        super().__init__(endpoint, "reset")

    def action(self) -> Optional[StatusResponse]:
        """Executes the 'reset' action on the optimization engine.

        Returns:
            The status response from the optimization engine.

        Raises:
            requests.HTTPError: If an HTTP error occurs.
            requests.RequestException: For network-related issues.
        """
        res = self.execute()

        return StatusResponse(res.json())


class StopAction(AbstractAction):
    """Action class to perform a 'stop' request on the optimization engine.

    This class defines an action to stop the optimization engine.
    """

    def __init__(self, endpoint: str) -> None:
        """Initializes a StopAction instance.

        Args:
            endpoint: The endpoint URL of the optimization engine.
        """
        super().__init__(endpoint, "stop")

    def action(self) -> Optional[StatusResponse]:
        """Executes the 'stop' action on the optimization engine.

        Returns:
            The status response from the optimization engine.

        Raises:
            requests.HTTPError: If an HTTP error occurs.
            requests.RequestException: For network-related issues.
        """
        res = self.execute()

        return StatusResponse(res.json())


class StatusAction(AbstractAction):
    """Action class to perform a 'status' request on the optimization engine.

    This class defines an action to request the status of the optimization
    engine.
    """

    def __init__(self, endpoint: str) -> None:
        """Initializes a StatusAction instance.

        Args:
            endpoint: The endpoint URL of the optimization engine.
        """
        super().__init__(endpoint, "status")

    def action(self) -> Optional[StatusResponse]:
        """Executes the 'status' action on the optimization engine.

        Returns:
            The status response from the optimization engine.

        Raises:
            requests.HTTPError: If an HTTP error occurs.
            requests.RequestException: For network-related issues.
        """
        res = self.execute()

        return StatusResponse(res.json())


class ModelAction(AbstractAction):
    """Action class to perform a 'model' request on the optimization engine.

    This class defines an action to submit a model to the optimization engine.
    """

    def __init__(self, endpoint: str, model: Modeller) -> None:
        """Initializes a ModelAction instance.

        Args:
            endpoint: The endpoint URL of the optimization engine.
            model: The model to be submitted.
        """
        super().__init__(endpoint, "model", model.to_json())

    def action(self) -> Optional[StatusResponse]:
        """Executes the 'model' action on the optimization engine.

        Returns:
            The status response from the optimization engine.

        Raises:
            requests.HTTPError: If an HTTP error occurs.
            requests.RequestException: For network-related issues.
        """
        res = self.execute()

        return StatusResponse(res.json())


class DirectModelAction(AbstractAction):
    """Action class to submit a model and get a solution back directly.

    This class is similar to `ModelAction`, but it is designed to work with
    endpoints that directly return a solution instead of a status.
    """

    def __init__(
        self,
        endpoint: str,
        model: Modeller,
        timeout: Optional[int] = 3600,
        ssl_verify: Optional[bool] = True,
    ) -> None:
        """Initializes a DirectModelAction instance.

        Args:
            endpoint: The endpoint URL of the optimization engine.
            model: The model to be submitted.
            timeout: The timeout for the request in seconds.
            ssl_verify: Whether to verify SSL certificates.
        """
        super().__init__(
            endpoint=endpoint,
            command="model",
            body=model.to_json(),
            timeout=timeout,
            ssl_verify=ssl_verify,
        )

        self.body = model.to_json()

    def action(self) -> Optional[SolutionResponse]:
        """Executes the 'model' action and returns a solution response.

        Returns:
            The solution response from the optimization engine.

        Raises:
            requests.HTTPError: If an HTTP error occurs.
            requests.RequestException: For network-related issues.
        """
        res = self.execute()

        return SolutionResponse(res.json())


class CurrentModelAction(AbstractAction):
    """Action class to request the current model from the optimization engine.

    This class defines an action to request the current model from the
    optimization engine.
    """

    def __init__(self, endpoint: str) -> None:
        """Initializes a CurrentModelAction instance.

        Args:
            endpoint: The endpoint URL of the optimization engine.
        """
        super().__init__(endpoint, "current")

    def action(self) -> Optional[ModelJSonResponse]:
        """Executes the 'current' action on the optimization engine.

        Returns:
            The current model response from the optimization engine.

        Raises:
            requests.HTTPError: If an HTTP error occurs.
            requests.RequestException: For network-related issues.
        """
        res = self.execute()

        return ModelJSonResponse(res.json())


class SolutionAction(AbstractAction):
    """Action class to request the solution from the optimization engine.

    This class defines an action to request the solution from the optimization
    engine.
    """

    def __init__(self, endpoint: str) -> None:
        """Initializes a SolutionAction instance.

        Args:
            endpoint: The endpoint URL of the optimization engine.
        """
        super().__init__(endpoint, "result")

    def action(self) -> Optional[SolutionResponse]:
        """Executes the 'result' action on the optimization engine.

        Returns:
            The solution response from the optimization engine.

        Raises:
            requests.HTTPError: If an HTTP error occurs.
            requests.RequestException: For network-related issues.
        """
        res = self.execute()

        return SolutionResponse(res.json())


class Engine:
    """Represents the optimization engine and provides methods for interaction.

    This class serves as an interface for interacting with the optimization engine.
    It provides methods to perform various actions such as requesting version
    information, submitting a model, retrieving solutions, and more.

    Attributes:
        endpoint (str): The endpoint URL of the optimization engine.
    """

    def __init__(self, endpoint: str) -> None:
        """Initializes an Engine instance.

        Args:
            endpoint: The endpoint URL of the optimization engine.
        """
        self.endpoint = endpoint

    def echo(self) -> Optional[EchoResponse]:
        """Sends an 'echo' request to the engine.

        Returns:
            The echo response from the optimization engine.
        """

    def version(self) -> Optional[VersionResponse]:
        """Requests the version information of the engine.

        Returns:
            The version response from the optimization engine.
        """
        return VersionAction(self.endpoint).action()

    def reset(self) -> Optional[StatusResponse]:
        """Resets the engine's state.

        Returns:
            The status response from the optimization engine.
        """
        return ResetAction(self.endpoint).action()

    def stop(self) -> Optional[StatusResponse]:
        """Stops the engine.

        Returns:
            The status response from the optimization engine.
        """
        return StopAction(self.endpoint).action()

    def status(self) -> Optional[StatusResponse]:
        """Checks the status of the engine.

        Returns:
            The status response from the optimization engine.
        """
        return StatusAction(self.endpoint).action()

    def model(self, model: Modeller) -> Optional[StatusResponse]:
        """Submits a model to the engine for optimization.

        Args:
            model: The model to be submitted.

        Returns:
            The model submission response from the optimization engine.
        """
        return ModelAction(self.endpoint, model).action()

    def current_model(self) -> Optional[ModelJSonResponse]:
        """Retrieves the current model from the engine.

        Returns:
            The current model response from the optimization engine.
        """
        return CurrentModelAction(self.endpoint).action()

    def solution(self) -> Optional[SolutionResponse]:
        """Retrieves the solution from the engine.

        Returns:
            The solution response from the optimization engine.
        """
        return SolutionAction(self.endpoint).action()


class DirectEngine:
    """Represents the Cloud optimization engine and provides methods for interaction.

    This engine is designed for demonstration purposes and handles small models
    by directly returning a solution upon model submission.

    Attributes:
        endpoint (str): The endpoint URL of the optimization engine.
        timeout (Optional[int]): The timeout for the request in seconds.
        ssl_verify (Optional[bool]): Whether to verify SSL certificates.
    """

    def __init__(
        self,
        endpoint: str = DIRECTENGINE_API_ENDPOINT,
        timeout: Optional[int] = 3600,
        ssl_verify: Optional[bool] = True,
    ) -> None:
        """Initializes a DirectEngine instance.

        Args:
            endpoint: The endpoint URL of the optimization engine.
            timeout: The timeout for the request in seconds.
            ssl_verify: Whether to verify SSL certificates.
        """
        self.endpoint = endpoint
        self.timeout = timeout
        self.ssl_verify = ssl_verify

    def echo(self):
        """
        Send an 'echo' request to the engine and retrieve the echo response.

        Note:
            only the 4 firsts characters are sent back.

        Returns:
            EchoResponse: The echo response from the optimization engine.
        """
        return EchoAction(
            self.endpoint, timeout=self.timeout, ssl_verify=self.ssl_verify
        ).action()

    def version(self):
        """
        Request the version information of the engine.

        Returns:
            VersionResponse: The version response from the optimization engine.
        """
        return VersionAction(
            self.endpoint, timeout=self.timeout, ssl_verify=self.ssl_verify
        ).action()

    def model(self, model: Modeller):
        """
        Submit a model to the engine for optimization.

        Args:
            model (Modeller): The model to be submitted.

        Returns:
            SolutionResponse: The model submission response from the optimization engine.
        """
        return DirectModelAction(
            endpoint=self.endpoint,
            model=model,
            timeout=self.timeout,
            ssl_verify=self.ssl_verify,
        ).action()


###
# Cluster
###


###
# Actions
###


class CurrentExplainAction(AbstractAction):
    """
    Represents an action to retrieve the current explanation.
    """

    def __init__(self, endpoint: str) -> None:
        super().__init__(endpoint=endpoint, command="explain")

    def action(self) -> Optional[ExplanationResponse]:
        """
        Execute the action and returns a response.

        Raises:
            requests.HTTPError: If an HTTP error occurs.
            requests.RequestException: For network-related issues.
        """

        ret = self.execute()

        return ExplanationResponse(json.loads(str(ret.content)))


class ExplainAction(AbstractAction):
    """
    Represents an action to request an explanation for a model.
    """

    def __init__(self, endpoint: str, model: Modeller) -> None:
        super().__init__(endpoint=endpoint, command="explain", body=model.to_json())

    def action(self) -> Optional[ExplanationResponse]:
        """
        Execute the action and returns a response.

        Raises:
            requests.HTTPError: If an HTTP error occurs.
            requests.RequestException: For network-related issues.
        """
        res = self.execute()

        return ExplanationResponse(res.json())


class CleanAction(AbstractAction):
    """
    Represents an action to clean the engine's environment.
    """

    def __init__(self, endpoint: str) -> None:
        super().__init__(endpoint=endpoint, command="clean")

    def action(self) -> Optional[StatusResponse]:
        """
        Execute the action and returns a response.

        Raises:
            requests.HTTPError: If an HTTP error occurs.
            requests.RequestException: For network-related issues.
        """
        res = self.execute()

        return StatusResponse(res.json())


class ClusterStatusAction(AbstractAction):
    """
    Represents an action to check the cluster's health status.
    """

    def __init__(self, endpoint: str) -> None:
        super().__init__(endpoint=endpoint, command="healthcheck")

    def action(self) -> Optional[ClusterStatusResponse]:
        """
        Execute the action and returns a response.

        Raises:
            requests.HTTPError: If an HTTP error occurs.
            requests.RequestException: For network-related issues.
        """
        res = self.execute()

        return ClusterStatusResponse(res.json())


class RemoveNodeAction(AbstractAction):
    """
    Represents an action to remove a node from the cluster.
    """

    def __init__(self, endpoint: str, identifier: str) -> None:
        super().__init__(
            endpoint=endpoint,
            command="remove",
            body={"identifier": identifier},
        )

    def action(self) -> Optional[StatusResponse]:
        """
        Execute the action and returns a response.

        Raises:
            requests.HTTPError: If an HTTP error occurs.
            requests.RequestException: For network-related issues.
        """
        res = self.execute()

        return StatusResponse(res.json())


class EnableNodeAction(AbstractAction):
    """
    Represents an action to enable a disabled node in the cluster.
    """

    def __init__(self, endpoint: str, identifier: str) -> None:
        super().__init__(
            endpoint=endpoint,
            command="enable",
            body={"identifier": identifier},
        )

    def action(self) -> Optional[StatusResponse]:
        """
        Execute the action and returns a response.

        Raises:
            requests.HTTPError: If an HTTP error occurs.
            requests.RequestException: For network-related issues.
        """
        res = self.execute()

        return StatusResponse(res.json())


class DisableNodeAction(AbstractAction):
    """
    Represents an action to disable a node in the cluster.
    """

    def __init__(self, endpoint: str, identifier: str) -> None:
        super().__init__(
            endpoint=endpoint,
            command="disable",
            body={"identifier": identifier},
        )

    def action(self) -> Optional[StatusResponse]:
        """
        Execute the action and returns a response.

        Raises:
            requests.HTTPError: If an HTTP error occurs.
            requests.RequestException: For network-related issues.
        """
        res = self.execute()

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

    def __init__(self, endpoint: str) -> None:
        """
        Initialize a ClusterEngine instance.

        Args:
            endpoint (str): The endpoint URL of the optimization engine.
        """
        super().__init__(endpoint=endpoint)

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

    def remove_node(self, identifier: str) -> Optional[StatusResponse]:
        """
        Remove a node from the cluster by its identifier.

        Args:
            identifier (str): The identifier of the node to be removed.

        Returns:
            StatusResponse: The response indicating the success of the node removal.
        """
        return RemoveNodeAction(endpoint=self.endpoint, identifier=identifier).action()

    def disable_node(self, identifier: str) -> Optional[StatusResponse]:
        """
        Disable a node in the cluster by its identifier.

        Args:
            identifier (str): The identifier of the node to be disabled.

        Returns:
            StatusResponse: The response indicating the success of disabling the node.
        """
        return DisableNodeAction(endpoint=self.endpoint, identifier=identifier).action()

    def enable_node(self, identifier: str) -> Optional[StatusResponse]:
        """
        Enable a disabled node in the cluster by its identifier.

        Args:
            identifier (str): The identifier of the node to be enabled.

        Returns:
            StatusResponse: The response indicating the success of enabling the node.
        """
        return EnableNodeAction(endpoint=self.endpoint, identifier=identifier).action()
