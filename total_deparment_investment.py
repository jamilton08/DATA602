#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 17:57:26 2024

@author: jonathancruz
"""

import pandas as pd

df = pd.read_csv("bronx_high_test.csv")

df.boxplot(column=['salary'], by='district', notch=True,  # notch shape
                     vert=True,  # vertical box alignment
                     patch_artist=True)



#grouped.boxplot(rot=45, fontsize=12, figsize=(8, 10)) 