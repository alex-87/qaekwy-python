# pylint: skip-file

import unittest
import json
# from unittest.mock import MagicMock

from qaekwy.core.response import (
    AbstractResponse, EchoResponse, StatusResponse, 
    SolutionResponse, ExplanationResponse, VersionResponse, 
    ClusterStatusResponse
)

class TestResponseClasses(unittest.TestCase):

    def test_abstract_response_default_ok(self):
        resp = AbstractResponse({"content": "data"})
        self.assertEqual(resp.get_status(), "Ok")
        self.assertTrue(resp.is_status_ok())
        self.assertEqual(resp.get_message(), "")

    def test_abstract_response_custom_status(self):
        resp = AbstractResponse({"status": "Error", "message": "Failed"})
        self.assertEqual(resp.get_status(), "Error")
        self.assertFalse(resp.is_status_ok())
        self.assertEqual(resp.get_message(), "Failed")

    def test_echo_response(self):
        content = "hello world"
        resp = EchoResponse(content)
        self.assertEqual(resp.get_status(), "")
        self.assertTrue(resp.is_status_ok())
        self.assertEqual(resp.get_message(), content)
        self.assertEqual(resp.get_content(), content)

    def test_status_response_fields(self):
        data = {
            "type": "info",
            "code": 200,
            "busy_node": True,
            "current_solution_found": 5
        }
        resp = StatusResponse(data)
        self.assertEqual(resp.get_type(), "info")
        self.assertEqual(resp.get_code(), 200)
        self.assertTrue(resp.is_busy())
        self.assertEqual(resp.get_number_of_solution_found(), 5)

    def test_status_response_defaults(self):
        resp = StatusResponse({})
        self.assertEqual(resp.get_type(), "")
        self.assertEqual(resp.get_code(), -1)
        self.assertFalse(resp.is_busy())
        self.assertEqual(resp.get_number_of_solution_found(), -1)

    def test_version_response(self):
        data = {
            "app": "OptiEngine",
            "author": "DevTeam",
            "version": "1.2.3",
            "version_major": 1,
            "version_minor": 2,
            "version_build": 3,
            "version_release": "stable"
        }
        resp = VersionResponse(data)
        self.assertEqual(resp.get_app(), "OptiEngine")
        self.assertEqual(resp.get_version_major(), 1)
        self.assertEqual(resp.get_release(), "stable")

    def test_cluster_status_parsing(self):
        node_data = [
            {
                "identifier": "node_01",
                "url": "http://node1",
                "enabled": True,
                "message": "Healthy",
                "busy_node": False,
                "current_solution_found": 10,
                "failure": False,
                "awake": True
            }
        ]
        resp = ClusterStatusResponse(json.dumps(node_data))
        nodes = resp.get_node_status_list()
        
        self.assertIsNotNone(nodes)
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0].identifier, "node_01")
        self.assertEqual(nodes[0].number_of_solutions, 10)
        self.assertTrue(nodes[0].is_enabled)

    def test_cluster_status_empty(self):
        resp = ClusterStatusResponse(None)
        self.assertIsNone(resp.get_node_status_list())

    def test_solution_response_error_status(self):
        resp = SolutionResponse({"status": "Error", "content": []})
        self.assertIsNone(resp.get_solutions())

    def test_explanation_response_error_status(self):
        resp = ExplanationResponse({"status": "Error", "content": {}})
        self.assertIsNone(resp.get_explanation())

if __name__ == "__main__":
    unittest.main()
