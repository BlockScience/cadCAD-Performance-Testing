import pandas as pd


def post_processing_function(state, params):
    df = pd.DataFrame(state["Simulation Log"])
    return df
