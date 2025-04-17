import pandas as pd
import swlag as swl


def test_read_tob_local():
    """Does read_tob() return a valid pandas DataFrame?"""
    path = "tests/data/example.tob"
    df = swl.read_tob(path)
    assert isinstance(df, pd.DataFrame)

def test_read_tob_remote():
    """Does read_tob() from a valid URL return a pandas DataFrame?"""
    url = "https://www.waterproperties.ca/osd_data_archive/Cruise_Data/2023/2023-026/Underway/TSG/2023-026-20230827.tob"
    df = swl.read_tob(url)
    assert isinstance(df, pd.DataFrame)
    
    
#test_read_tob_local()
test_read_tob_remote()
