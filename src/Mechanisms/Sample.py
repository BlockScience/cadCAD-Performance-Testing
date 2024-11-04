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
    "domain": ["Sample Queue Space"],
    "parameters_used": [],
    "updates": [
        ("Global", "Sample Queue", False),
    ],
}

log_simulation_data_mechanism = {
    "name": "Log Simulation Data Mechanism",
    "description": "Logs simulation data",
    "constraints": [],
    "logic": """""",
    "domain": [],
    "parameters_used": [],
    "updates": [
        ("Global", "Simulation Log", False),
    ],
}


sample_mechanisms = [
    update_mean_mechanism,
    update_queue_mechanism,
    log_simulation_data_mechanism,
]
