# -*- coding: utf-8 -*-
"""PyPool.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14xZduXP6nZVlVrqSQcrULmNb50Tqyy6h
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df= pd.read_csv("Resources/election_data.csv")
df.head()

#* The total number of votes cast
df["Ballot ID"].nunique()
print("Total Votes:", df["Ballot ID"].nunique())

#* A complete list of candidates who received votes
df["Candidate"].unique()

#* The percentage of votes each candidate won

zz=df.groupby("Candidate")["Ballot ID"].nunique()
zz

df_1=pd.DataFrame()
df_1["Candidate"]=zz.index
df_1["count_vote"]=zz.values
df_1

df_1['%'] = 100 * df_1['count_vote'] / df_1['count_vote'].sum()
df_1

#* The total number of votes each candidate won
zz=df.groupby("Candidate")["Ballot ID"].nunique()
zz

#* The winner of the election based on popular vote.
win=df_1[df_1['count_vote']==df_1['count_vote'].max()]

print("Winner: ",win["Candidate"].unique()[0])

