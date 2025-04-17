import pandas as pd
import swlag as swl


def test_transform():
    """Does _transform_inlet_tracer() return a new column?"""
    path = "./data/example.csv"
    df = pd.read_csv(path)
    df["Tprime"] = swl.calc._transform_inlet_tracer(df["T"], 400., 0.3, 370.)
    assert isinstance(df["Tprime"], pd.Series)


test_transform()
