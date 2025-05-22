"""
Example script demonstrating how to use the n8n_utils visualization.
"""
import json
import os
import sys
from pathlib import Path

# Add the lib directory to the path so we can import n8n_utils
sys.path.insert(0, str(Path(__file__).parent.parent))

from n8n_utils.visualization import visualize_workflow

def create_sample_workflow():
    """Create a sample n8n workflow for demonstration."""
    return {
        "name": "Sample Workflow",
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
                "position": [450, 200],
                "parameters": {
                    "url": "https://api.example.com/data",
                    "method": "GET"
                }
            },
            {
                "id": "3",
                "name": "Process Data",
                "type": "n8n-nodes-base.function",
                "typeVersion": 1,
                "position": [650, 300],
                "parameters": {
                    "functionCode": "// Process the data here\nreturn items;"
                }
            },
            {
                "id": "4",
                "name": "Condition",
                "type": "n8n-nodes-base.if",
                "typeVersion": 1,
                "position": [850, 300],
                "parameters": {
                    "conditions": {
                        "string": [
                            {
                                "value1": "={{ $json.someField }}",
                                "operation": "exists"
                            }
                        ]
                    }
                }
            },
            {
                "id": "5",
                "name": "Send Email",
                "type": "n8n-nodes-base.emailSend",
                "typeVersion": 1,
                "position": [1050, 200],
                "parameters": {
                    "to": "user@example.com",
                    "subject": "Processing Complete",
                    "text": "The data has been processed successfully."
                }
            },
            {
                "id": "6",
                "name": "Log Error",
                "type": "n8n-nodes-base.function",
                "typeVersion": 1,
                "position": [1050, 400],
                "parameters": {
                    "functionCode": "console.log('Error processing data:', items);\nreturn items;"
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
            },
            "2": {
                "main": [
                    [
                        {
                            "node": "3",
                            "type": "main",
                            "index": 0
                        }
                    ]
                ]
            },
            "3": {
                "main": [
                    [
                        {
                            "node": "4",
                            "type": "main",
                            "index": 0
                        }
                    ]
                ]
            },
            "4": {
                "main": [
                    [
                        {
                            "node": "5",
                            "type": "main",
                            "index": 0
                        }
                    ]
                ]
            },
            "4-1": {
                "main": [
                    [
                        {
                            "node": "6",
                            "type": "main",
                            "index": 0
                        }
                    ]
                ]
            }
        }
    }

def main():
    """Run the example."""
    # Create output directory if it doesn't exist
    output_dir = Path(__file__).parent / "output"
    output_dir.mkdir(exist_ok=True)
    
    # Create a sample workflow
    workflow = create_sample_workflow()
    
    # Save the workflow as JSON
    workflow_file = output_dir / "sample_workflow.json"
    with open(workflow_file, 'w', encoding='utf-8') as f:
        json.dump(workflow, f, indent=2)
    
    print(f"Created sample workflow at: {workflow_file}")
    
    # Visualize the workflow
    output_image = output_dir / "workflow_visualization.png"
    from n8n_utils.visualization.visualizer import visualize_workflow
    visualize_workflow(workflow, output_file=str(output_image), show=True)
    print(f"Workflow visualization saved to: {output_image}")

if __name__ == "__main__":
    main()
