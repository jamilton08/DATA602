#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 09:46:07 2024

@author: jonathancruz
"""

import pandas as pd

df = pd.read_csv("bronx_high_test.csv")


totals = df.groupby(["name", "district"], as_index=False)["salary"].sum()
sped = df[df["subject"].str.contains("special education".upper())]

sped_totals = sped.groupby(["name"], as_index = False)["salary"].sum()

merged = pd.merge(sped_totals, totals, on="name")

merged["sped_ratio"] = merged["salary_x"] / merged["salary_y"]

ax = merged.sped_ratio.plot.kde(bw_method=0.3)

mean = merged.sped_ratio.mean()
st = merged.sped_ratio.std()

merged["z_scores"] = (merged["sped_ratio"] - mean) / st

bx = merged.groupby(["district"], as_index=False).mean().plot.barh(x = "district", y = "z_scores", rot = 0)


print(mean, st)


