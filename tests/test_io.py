import pandas as pd
import swlag as lag

fname = "./data/2023-026-20230827.tob"
df = lag.read_tob(fname)

def test_read_tob():
    """Does read_tob() return a valid pandas DataFrame?"""
    assert isinstance(df, pd.DataFrame)

# test_read_tob()
