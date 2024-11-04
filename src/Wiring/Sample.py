sample_wiring = []

sample_wiring.append(
    {
        "name": "Sample Wiring",
        "components": [
            "Add New Sample Control Action",
            "Update Rolling Mean Policy",
            "Rolling Mean Mechanisms",
            "Log Simulation Data Mechanism",
        ],
        "description": "A block for sampling and updating a rolling mean",
        "constraints": [],
        "type": "Stack",
    }
)

sample_wiring.append(
    {
        "name": "Rolling Mean Mechanisms",
        "components": [
            "Update Mean Mechanism",
            "Update Queue Mechanism",
        ],
        "description": "Mechanisms for Rolling Mean Update",
        "constraints": [],
        "type": "Parallel",
        "optional_indices": [],
    }
)
