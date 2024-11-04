def update_rolling_mean_policy_v1(state, params, spaces):
    q = state["Sample Queue"]
    s = state["Current Mean"] * len(q)
    s += spaces[0]["sample"]
    q.append(spaces[0]["sample"])
    if len(q) > params["Rolling Mean Window"]:
        s -= q.pop(0)
    s = s / len(q)
    return [{"mean": s}, {"sample_queue": q}]
