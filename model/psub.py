import numpy as np


def p_sample(_params, substep, state_history, state):
    sample = np.random.normal(
        _params["Sample Mean"], _params["Sample Standard Deviation"]
    )
    q = state["Sample Queue"]
    s = state["Current Mean"] * len(q)
    s += sample
    q.append(sample)
    if len(q) > _params["Rolling Mean Window"]:
        s -= q.pop(0)
    s = s / len(q)
    return {"Current Mean": s, "Sample Queue": q}


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
