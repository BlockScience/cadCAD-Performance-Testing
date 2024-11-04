dummy_mechanism = {
    "name": "DUMMY Update Dummy Entity Mechanism",
    "description": "A mechanism which appends the word just added and also increments the total length",
    "constraints": [],
    "logic": """1. Append the string from DOMAIN[0] to the Words state variable for DUMMY entity
    2. Increment the Total Length state variable by the length from DOMAIN[0]""",
    "domain": [
        "DUMMY String Length Space",
    ],
    "parameters_used": [],
    "updates": [
        ("DUMMY Entity", "Words", False),
        ("DUMMY Entity", "Total Length", False),
    ],
}

dummy_increment_time_mechanism = {
    "name": "DUMMY Increment Time Mechanism",
    "description": "A mechanism which adds one to the clock time",
    "constraints": [],
    "logic": """1. Increment the global time by 1""",
    "domain": [],
    "parameters_used": [],
    "updates": [
        ("Global", "Time", False),
    ],
}

dummy_log_simulation_data_mechanism = {
    "name": "DUMMY Log Simulation Data Mechanism",
    "description": "A mechanism for logging simulation data",
    "constraints": [],
    "logic": """Append simulation data to the simulation log""",
    "domain": [],
    "parameters_used": [],
    "updates": [
        ("Global", "Simulation Log", False),
    ],
}


dummy_mechanisms = [
    dummy_mechanism,
    dummy_increment_time_mechanism,
    dummy_log_simulation_data_mechanism,
]
