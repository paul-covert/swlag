#! /usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import pyuwtc as uwtc

test_fnames = [
    "./data/2023-026-20230825.tob",
    "./data/2023-026-20230826.tob",
    "./data/2023-026-20230827.tob",
    "./data/2023-026-20230828.tob",
    "./data/2023-026-20230829.tob"
]
df = pd.concat([uwtc.read_tob(test_fname) for test_fname in test_fnames])
df["temp_prime"] = df["temp_inlet"] + 0.1
fig, ax = uwtc.plot_tsg_flow(df)
fig2, ax2 = uwtc.plot_temp(df)
plt.show()
