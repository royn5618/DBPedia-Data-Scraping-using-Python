# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 12:33:15 2018

@author: Owner
"""
import Helper

def remove_types_columns(df):
    cols_to_remove = []
    for column in df.columns:
        if "type" in column:
            cols_to_remove.append(column)
    df_cleaned = df.drop(columns=cols_to_remove)
    Helper.write_to_pickle(df_cleaned)

