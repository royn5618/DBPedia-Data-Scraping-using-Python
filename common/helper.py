# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 23:03:34 2019
@author: NRoy
"""

from pandas import ExcelWriter
import pandas as pd
from datetime import datetime
import os
from common.common_settings import CommonConfig


class Helper:
    @staticmethod
    def generate_file_name(file_name):
        """ Generates a file name to store the results"""
        return file_name + '_' + str(datetime.now().strftime("%d_%m_%Y")) + '_' + str(datetime.now().strftime("%H_%M_%S"))

    @staticmethod
    def write_to_excel(df, file_name):
        """ Writes the results to an excel sheet """
        formatted_file_name = Helper.generate_file_name(file_name)
        writer = ExcelWriter(CommonConfig.DATA_FOLDER_PATH + '/' + formatted_file_name + '.xlsx')
        df.to_excel(writer)
        writer.save()
        print('Done.')

    @staticmethod
    def write_to_pickle(df, file_name):
        """ Writes the results to a pickle file"""
        formatted_file_name = Helper.generate_file_name(file_name)
        df.to_pickle(CommonConfig.DATA_FOLDER_PATH + '/' + formatted_file_name + '.pkl')
        print("-------------WRITING TO PICKLE COMPLETED-------------")

    @staticmethod
    def read_from_pickle(file_name):
        """ Reads from a pickle file"""
        df = pd.read_pickle(file_name)
        print("-------------READ FROM PICKLE COMPLETED-------------")
        return df

    @staticmethod
    def remove_type_columns(df):
        """ Removes all data type columns"""
        cols_to_remove = []
        for column in df.columns:
            if "type" in column:
                cols_to_remove.append(column)
        df_cleaned = df.drop(columns=cols_to_remove)
        return df_cleaned

    @staticmethod
    def create_data_folder(path):
        """ To create a new folder to store query results """
        try:
            if not os.path.isdir(path):
                os.mkdir(path)
        except Exception as e:
            print(e)
            print("Could not create folder at {}. Working Directory: {}".format(path, str(os.getcwd())))

