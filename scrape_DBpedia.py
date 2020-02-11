# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 12:33:15 2018

@author: Naba
"""
import argparse

import pandas as pd
from SPARQLWrapper import SPARQLWrapper, JSON
from pandas.io.json import json_normalize

from Common import common_settings
from Common import helper
from Project1_Athletes import query as athletes_query
import pdb
from datetime import datetime
import sys
import os


def clean_data_and_save(df, file_name):
    df = helper.remove_type_columns(df)
    helper.write_to_pickle(df, file_name)


def get_paginated_data(limit, offset, query, sparql, df):
    print("Current limit value: " + str(limit))
    print("Current offset value: " + str(offset))
    formatted_query = query.get_query(limit, offset)
    sparql.setQuery(formatted_query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    results = json_normalize(results['results']['bindings'])
    df = df.append(results)
    return df


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-type", choices=["athletes"])

    args = parser.parse_args()
    q_type = args.type

    sparql = SPARQLWrapper(common_settings.dbpedia_url)
    query = None

    if q_type == "athletes":
        athletes_path = "Project1_Athletes/Data"
        query = athletes_query
        try:
            if not os.path.isdir(athletes_path):
                os.mkdir(athletes_path)
        except Exception as e:
            print(e)
            print("Working Directory: " + str(os.getcwd()))
        file_name = athletes_path + "/" + q_type
    else:
        print("Invalid type. Please Retry.")
        sys.exit(1)

    print("Begin Scraping DBpedia: ")
    print(datetime.now())

    df = pd.DataFrame()

    pdb.set_trace()
    try:
        for i in range(100000):
            if i == 0:
                df = get_paginated_data(common_settings.dbpedia_limit, i, query, sparql, df)
            else:
                print("Length of data frame now :" + str(len(df)))
                prev_len = len(df)
                df = get_paginated_data(common_settings.dbpedia_limit, len(df) + 1, query, sparql, df)
                if prev_len == len(df):
                    break
    except Exception as e:
        print(e)
        print("Error in scraping DBpedia.")
    pdb.set_trace()
    clean_data_and_save(df, file_name)
    print("Finished scraping DBpedia at: ")
    print(datetime.now())

