add_new_sample_control_action_option1 = {
    "name": "Add New Sample Control Action V1",
    "description": "Return the sample drawing from a normal random distribution with PARAMS['Sample Mean'], PARAMS['Standard Deviation']",
    "logic": "Return the sample drawing from a normal random distribution with PARAMS['Sample Mean'], PARAMS['Standard Deviation']",
}

add_new_sample_control_action = {
    "name": "Add New Sample Control Action",
    "description": "Adds a new sample",
    "constraints": [],
    "control_action_options": [add_new_sample_control_action_option1],
    "codomain": [
        "Sample Space",
    ],
    "parameters_used": ["Sample Mean", "Sample Standard Deviation"],
}

sample_control_actions = [add_new_sample_control_action]
