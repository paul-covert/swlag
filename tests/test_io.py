import pandas as pd
import swlag as lag

fname = "tests/data/example.tob"
df = lag.read_tob(fname)

def test_read_tob():
    """Does read_tob() return a valid pandas DataFrame?"""
    assert isinstance(df, pd.DataFrame)

# test_read_tob()
