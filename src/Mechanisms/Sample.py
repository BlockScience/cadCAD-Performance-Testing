update_mean_mechanism = {
    "name": "Update Mean Mechanism",
    "description": "Sets the mean",
    "constraints": [],
    "logic": """""",
    "domain": ["Mean Space"],
    "parameters_used": [],
    "updates": [
        ("Global", "Current Mean", False),
    ],
}
update_queue_mechanism = {
    "name": "Update Queue Mechanism",
    "description": "Sets the sample queue",
    "constraints": [],
    "logic": """""",
    "domain": ["Sample Space"],
    "parameters_used": [],
    "updates": [
        ("Global", "Sample Queue", False),
    ],
}


sample_mechanisms = [
    update_mean_mechanism,
    update_queue_mechanism,
]
