"""Tests for n8n workflow validation."""
import json
import os
import tempfile
import unittest
from pathlib import Path

from n8n_utils.ci.validator import validate_workflow, ValidationError

class TestWorkflowValidation(unittest.TestCase):
    """Test cases for workflow validation."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.valid_workflow = {
            "name": "Test Workflow",
            "nodes": [
                {
                    "id": "1",
                    "name": "Start",
                    "type": "n8n-nodes-base.start",
                    "typeVersion": 1,
                    "position": [250, 300],
                    "parameters": {}
                },
                {
                    "id": "2",
                    "name": "HTTP Request",
                    "type": "n8n-nodes-base.httpRequest",
                    "typeVersion": 1,
                    "position": [450, 300],
                    "parameters": {
                        "url": "https://example.com",
                        "method": "GET"
                    }
                }
            ],
            "connections": {
                "1": {
                    "main": [
                        [
                            {
                                "node": "2",
                                "type": "main",
                                "index": 0
                            }
                        ]
                    ]
                }
            }
        }
    
    def test_valid_workflow(self):
        """Test validation of a valid workflow."""
        errors = validate_workflow(self.valid_workflow)
        self.assertEqual(len(errors), 0)
    
    def test_missing_required_field(self):
        """Test validation of a workflow with a missing required field."""
        # Remove a required field
        invalid_workflow = self.valid_workflow.copy()
        del invalid_workflow["nodes"][0]["id"]
        
        errors = validate_workflow(invalid_workflow)
        self.assertGreater(len(errors), 0)
        self.assertIn("id", errors[0])
    
    def test_invalid_node_structure(self):
        """Test validation of a workflow with invalid node structure."""
        invalid_workflow = self.valid_workflow.copy()
        # Make position an invalid type
        invalid_workflow["nodes"][0]["position"] = "not an array"
        
        errors = validate_workflow(invalid_workflow)
        self.assertGreater(len(errors), 0)
        self.assertIn("position", errors[0])

if __name__ == "__main__":
    unittest.main()
