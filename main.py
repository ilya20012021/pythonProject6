import json
import webbrowser
import os
import pandas as pd
from tabulate import tabulate

import file
os.chdir("D:")
with open('D:\i.json','w') as json_file:
    json_file.truncate(0)

file.cwe()
a = []
with open('D:\i.json') as json_file:
    data = json.load(json_file)
    d = data["results"]
    d = list(d)
    for i in range(len(d)):
        c = d[i]
        r = c["issue_cwe"]
        k = r["id"]
        a.append(k)

b = set(a)
c = list(b)
num = [int(i) for i in range(len(c))]
site = []
for i in c:
    site.append(f"https://cwe.mitre.org/data/definitions/{i}.html")

counters = []
for i in c:
    x = a.count(i)
    counters.append(x)


df = pd.DataFrame({})
df["id"] = num
df["cwe"] = c
df["site"] = site
df["counters"] = counters
print(tabulate(df,headers="keys",tablefmt="psql"))