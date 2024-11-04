sample_parameter_set = {
    "name": "Sample Parameter Set",
    "notes": "A set of sampling parameters",
    "parameters": [
        {
            "variable_type": "Float Type",
            "name": "Sample Mean",
            "description": "The mean value of sample draws",
            "symbol": None,
            "domain": None,
            "parameter_class": "Behavioral",
        },
        {
            "variable_type": "Float Type",
            "name": "Sample Standard Deviation",
            "description": "The standard deviation of the value for sampling",
            "symbol": None,
            "domain": None,
            "parameter_class": "Behavioral",
        },
        {
            "variable_type": "Integer Type",
            "name": "Rolling Mean Window",
            "description": "The number of samples to use for the rolling window at maximum",
            "symbol": None,
            "domain": None,
            "parameter_class": "Functional",
        },
    ],
}


sample_parameter_sets = [sample_parameter_set]
