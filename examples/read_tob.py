import swlag as swl

path = "tests/data/2023-026-20230827.tob"
df = swl.read_tob(path)
print(df)
