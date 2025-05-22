"""
n8n Workflow Validator

This module provides functionality to validate n8n workflow JSON files
against a schema to ensure they are properly formatted.
"""
import json
import os
import sys
from pathlib import Path
from typing import Dict, List, Optional, Union

import jsonschema
from jsonschema import validate

# Define the n8n workflow JSON schema
N8N_WORKFLOW_SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "required": ["nodes", "connections"],
    "properties": {
        "name": {"type": "string"},
        "nodes": {
            "type": "array",
            "items": {
                "type": "object",
                "required": ["id", "name", "type", "typeVersion", "position", "parameters"],
                "properties": {
                    "id": {"type": "string"},
                    "name": {"type": "string"},
                    "type": {"type": "string"},
                    "typeVersion": {"type": ["number", "string"]},
                    "position": {
                        "type": "array",
                        "items": {"type": "number"},
                        "minItems": 2,
                        "maxItems": 2
                    },
                    "parameters": {"type": "object"},
                },
            },
        },
        "connections": {"type": "object"},
    },
}

class ValidationError(Exception):
    """Custom exception for validation errors."""
    pass

def validate_workflow(workflow_data: Dict) -> List[str]:
    """
    Validate an n8n workflow against the schema.
    
    Args:
        workflow_data: The parsed JSON data of the workflow
        
    Returns:
        List of error messages, empty if valid
    """
    try:
        validate(instance=workflow_data, schema=N8N_WORKFLOW_SCHEMA)
        return []
    except jsonschema.exceptions.ValidationError as e:
        return [f"Validation error: {e.message} at {'.'.join(map(str, e.path))}"]

def validate_workflow_file(file_path: Union[str, Path]) -> List[str]:
    """
    Validate an n8n workflow file.
    
    Args:
        file_path: Path to the JSON file to validate
        
    Returns:
        List of error messages, empty if valid
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            try:
                workflow_data = json.load(f)
            except json.JSONDecodeError as e:
                return [f"Invalid JSON in {file_path}: {str(e)}"]
            
            return validate_workflow(workflow_data)
    except Exception as e:
        return [f"Error reading {file_path}: {str(e)}"]

def find_workflow_files(directory: Union[str, Path]) -> List[Path]:
    """
    Recursively find all JSON files in a directory that might be n8n workflows.
    
    Args:
        directory: Directory to search in
        
    Returns:
        List of Path objects to potential workflow files
    """
    directory = Path(directory)
    return list(directory.glob("**/*.json"))

def validate_all_workflows(directory: Union[str, Path]) -> Dict[str, List[str]]:
    """
    Validate all JSON files in a directory and its subdirectories.
    
    Args:
        directory: Directory to search for workflow files
        
    Returns:
        Dictionary mapping file paths to lists of error messages
    """
    workflow_files = find_workflow_files(directory)
    results = {}
    
    for file_path in workflow_files:
        errors = validate_workflow_file(file_path)
        if errors:
            results[str(file_path)] = errors
    
    return results

def main():
    """Command-line interface for the validator."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Validate n8n workflow files.")
    parser.add_argument(
        "directory",
        nargs="?",
        default=".",
        help="Directory containing n8n workflow files (default: current directory)",
    )
    args = parser.parse_args()
    
    directory = Path(args.directory).resolve()
    if not directory.exists():
        print(f"Error: Directory '{directory}' does not exist")
        sys.exit(1)
    
    print(f"Validating n8n workflows in: {directory}")
    results = validate_all_workflows(directory)
    
    if not results:
        print("✅ All workflow files are valid!")
        sys.exit(0)
    
    # Print errors
    error_count = 0
    for file_path, errors in results.items():
        print(f"\n❌ {file_path}:")
        for error in errors:
            print(f"  - {error}")
            error_count += 1
    
    print(f"\nFound {error_count} error(s) in {len(results)} file(s)")
    sys.exit(1)

if __name__ == "__main__":
    main()
