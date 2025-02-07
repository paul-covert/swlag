#! /usr/bin/env python3

import matplotlib.pyplot as plt
import pyuwtc as uwtc

test_fname = "./data/2023-026-20230826.tob"
df = uwtc.read_tob(test_fname)
df["temp_prime"] = df["temp_inlet"] + 0.1
fig, ax = uwtc.plot_tsg_flow(df)
fig2, ax2 = uwtc.plot_temp(df)
plt.show()
