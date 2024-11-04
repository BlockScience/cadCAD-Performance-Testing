def update_mean_mechanism(state, params, spaces):
    state["Current Mean"] = spaces[0]["mean"]


def update_queue_mechanism(state, params, spaces):
    state["Sample Queue"] = spaces[0]["sample_queue"]


def log_simulation_data_mechanism(state, params, spaces):
    state["Simulation Log"].append(
        {
            "Rolling Mean": state["Current Mean"],
        }
    )
