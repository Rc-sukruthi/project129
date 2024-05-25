import pandas as pd
import csv

data1 = "bright_stars.csv"
data2 = "unit_converted_stars.csv"

d1 = []
d2 = []
with open(data1, "r", encoding="utf8") as f:
    csv_reader= csv.reader(f)

    for i in csv_reader:
        d1.append(i)

with open(data2, "r", encoding="utf8") as f:
    csv_reader = csv.reader(f)

    for i in csv_reader:
        d2.append(i)

h1 = d1[0]
h2 = d2[0]
pd1 = d1[1:]
pd2 = d2[1:]

h = h1 + h2

p_d = []
for i in pd1:
    p_d.append(i)
for j in pd2:
    p_d.append(j)
print(p_d)

with open("all_stars.csv", "w", encoding="utf8") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(h)
    csv_writer.writerows(p_d)

da = pd.read_csv("all_stars.csv")
#print(da)