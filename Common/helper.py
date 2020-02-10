# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 12:33:15 2018

@author: Nroy
"""

from pandas import ExcelWriter
import pandas as pd
from datetime import datetime


def get_file_name(file_name):
    return file_name + '_' + str(datetime.now().strftime("%d_%m_%Y")) + '_' + str(datetime.now().strftime("%H_%M_%S"))


def write_to_excel(df, file_name):
    formatted_file_name = get_file_name(file_name)
    writer = ExcelWriter(formatted_file_name + '.xlsx')
    df.to_excel(writer)
    writer.save()
    print('done')


def write_to_pickle(df, file_name):
    formatted_file_name = get_file_name(file_name)
    df.to_pickle(formatted_file_name + '.pkl')
    print("-------------WRITING TO PICKLE COMPLETED-------------")


def read_from_pickle(file_name):
    df = pd.read_pickle(file_name)
    print("-------------READ FROM PICKLE COMPLETED-------------")
    return df


def remove_type_columns(df):
    cols_to_remove = []
    for column in df.columns:
        if "type" in column:
            cols_to_remove.append(column)
    df_cleaned = df.drop(columns=cols_to_remove)
    return df_cleaned

