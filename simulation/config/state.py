from copy import deepcopy

state_base = {
    "Dummy": {"Words": "", "Total Length": None},
    "Time": 0,
    "Simulation Log": [],
    "Current Mean": 0,
    "Sample Queue": [],
}

state_test1 = deepcopy(state_base)
state_test1["Time"] = 100
