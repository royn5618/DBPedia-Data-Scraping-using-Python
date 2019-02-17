# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 12:33:15 2018

@author: Owner
"""

from pandas import ExcelWriter
import pandas as pd

def write_to_excel(df):
    writer = ExcelWriter('athletes_details1.xlsx')
    df.to_excel(writer)
    writer.save()
    print('done')

def write_to_pickle(df):
    df.to_pickle('athletes_details1.pkl')
    print("-------------WRITING TO PICKLE COMPLETED-------------")

def read_from_pickle(file_name):
    df = pd.read_pickle(file_name)
    print("-------------READ FROM PICKLE COMPLETED-------------")
    return df