def p_sample(_params, substep, state_history, state):
    return {"Current Mean": 0, "Sample Queue": []}


psub_blocks = [
    {
        "policies": {
            "p_sample": p_sample,
        },
        "variables": {
            "Current Mean": lambda a, b, c, d, e: ("Current Mean", e["Current Mean"]),
            "Sample Queue": lambda a, b, c, d, e: ("Sample Queue", e["Sample Queue"]),
        },
    },
]
