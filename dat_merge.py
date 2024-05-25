import pandas as pd
import csv
import numpy

df = pd.read_csv("brown_dwarf_scraped_data.csv")
ab = df.head(10)

df = df.dropna()
cd = df.info()

df.Mass = df.Mass.str.replace("[13.3 (Â± 1.7) Â MJ]", "").astype('float')
df["Mass"] = df["Mass"] * (0.000954588)
df["Radius"] = df["Radius"] * (0.102763)
df.to_csv("data_merge.csv")

