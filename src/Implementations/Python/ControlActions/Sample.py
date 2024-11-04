import numpy as np


def add_new_sample_control_action_v1(state, params, spaces):
    out = np.random.normal(params["Sample Mean"], params["Sample Standard Deviation"])
    space = {"sample": out}
    return [space]
