#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 08:30:44 2024

@author: jonathancruz
"""

import requests
from bs4 import BeautifulSoup
import math
import pandas as pd
import re


target_url='https://www.nycenet.edu/offices/d_chanc_oper/budget/dbor/galaxy/galaxybudgetsummaryto/default.aspx?DDBSSS_INPUT={}'
save_list = list()
for code  in range(600):
    parse_code = "x" + str(code)
    res = requests.get(target_url.format(parse_code))
    soup=BeautifulSoup(res.text,'html.parser')
    h = soup.find(text=re.compile('High School Departments'))
    if h is None:
        continue
    det = soup.find("div", {"class" : "School_Heading"}).find("a").get_text().split("-")
    print(det)
    name = det[1][1:]
    dis_s = det[0].split("X")
    print(dis_s)
    district = dis_s[0]
    school_code = dis_s[1]
    print(name)
    b = h.parent.next_sibling.find_all("tr", {"class" : "section_table"})
    for subject_rows in b:
        row_content = subject_rows.find_all("td")
        subject = row_content[0].get_text()
        amount = int(float(row_content[2].get_text()))
        salary = int(row_content[3].get_text().replace("$ ", "").replace(",",""))
        for i in range(amount):
            print(name, subject, salary)
            save_list.append([district, school_code, name, subject, salary])
    
df = pd.DataFrame(save_list, columns=["district", "code", "name", "subject", "salary"])
df.to_csv("bronx_high_test.csv",  encoding='utf-8', index=False)