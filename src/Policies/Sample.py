update_rolling_mean_policy_option1 = {
    "name": "Update Rolling Mean Policy V1",
    "description": "",
    "logic": """""",
}

update_rolling_mean_policy = {
    "name": "Update Rolling Mean Policy",
    "description": "The policy which determines the new rolling mean.",
    "constraints": [],
    "policy_options": [update_rolling_mean_policy_option1],
    "domain": [
        "Sample Space",
    ],
    "codomain": ["Mean Space", "Sample Queue Space"],
    "parameters_used": ["Rolling Mean Window"],
    "metrics_used": [],
}

sample_policies = [update_rolling_mean_policy]
