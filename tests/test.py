#! /usr/bin/env python3

import pyuwtc as uwtc

test_fname = "./data/2023-026-20230826.tob"
df = uwtc.read_tob(test_fname)
print(df)
