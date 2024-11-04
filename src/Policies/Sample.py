update_rolling_mean_policy_option1 = {
    "name": "Update Rolling Mean Policy V1",
    "description": "Simple policy which computes the rolling mean based on a maximum rolling mean window",
    "logic": """1. Compute sum as the state variable of current mean times the length of the sample queue state variable
2. Add the sample from DOMAIN[0] to this value and append it to the sample queue
3. If the sample queue length is greater than PARAMS['Rolling Mean Window'] then pop the first element in the queue and subtract it from the sum
4. Divide the sum by the legnth of samples and return the two spaces""",
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
