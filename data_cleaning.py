#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 11:01:23 2020

@author: sandylee
"""


import pandas as pd

df = pd.read_csv("/Users/sandylee/git/flatiron_school_mod_4_group_project/analytic_data2019.csv")

df_update = df[df.columns.drop(list(df.filter(regex= 'denominator|numerator|CI|Black|White|Hispanic|FIPS', axis = 1)))]

total = df_update.isnull().sum().sort_values(ascending=False)
percent = (df_update.isnull().sum()/df_update.isnull().count()).sort_values(ascending=False)
missing_data = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
print(missing_data.head(60))




#df_update.loc[df_update['County Ranked (Yes=1/No=0)'] == 0]

#dropping numberator and demoninator columns

#dropping confidence interal columns

#dropping race



