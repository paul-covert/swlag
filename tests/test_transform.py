import pandas as pd
import swlag as swl


def test_transform():
    """Does _transform_inlet_tracer() return a new column?"""
    path = "tests/data/example.csv"
    df = pd.read_csv(path)
    df["temp_inlet_prime"] = swl.calc._transform_inlet_tracer(df["temp_inlet"], 400., 0.3, 370.)
    assert isinstance(df["temp_inlet_prime"], pd.Series)
