import pandas as pd
import swlag as swl


def test_transform():
    """Does transform_inlet_temp() return a new temperature column?"""
    path = "./data/example.tob"
    df = swl.read_tob(path)
    df["Tprime"] = swl.transform_inlet_temp(df["T"], 400., 0.3, 370.)
    assert isinstance(df["Tprime"], pd.Series)


test_transform()
