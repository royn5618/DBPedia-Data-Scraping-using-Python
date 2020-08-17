# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 23:03:34 2019
@author: NRoy
"""

import argparse
import sys
from datetime import datetime

import pandas as pd
from SPARQLWrapper import SPARQLWrapper, JSON
from pandas.io.json import json_normalize

from common.common_settings import CommonConfig
from common.helper import Helper
from queries import q_athletes


def clean_data_and_save(df, fname):
    """
    For basic cleaning and saving the dataset.

    :param df: Pandas DataFrame object
    :param fname: Pickle File Name to store contents of df
    :return: None
    """
    df = Helper.remove_type_columns(df)
    Helper.write_to_pickle(df, fname)


def get_paginated_data(limit, offset, query, sparql, df):
    """
    To get paginated data using the query and enforcing limits since
    DBpedia does not allow more that 10000 (CommonConfig.DBPEDIA_LIMIT) results

    :param limit: number of query results to retrieve
    :param offset: starting point of query results
    :param query: the query
    :param sparql: SPARQL Endpoint
    :param df: DataFrame to append every scrape (iterative)
    :return: DataFrame of <= 10000 results
    """
    print("Current limit value: " + str(limit))
    print("Current offset value: " + str(offset))
    formatted_query = query.get_query(limit, offset)
    sparql.setQuery(formatted_query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    results = json_normalize(results['results']['bindings'])
    df = df.append(results)
    return df


def scrape_dbpedia(query, sparql):
    """
    To scrape dbpedia iteratively since DBpedia does not allow more that 10000 results
    :param query: the query from queries/<your query file>
    :param sparql: sparql endpoint
    :return: completed DataFrame
    """
    print("------Begin Scraping DBpedia-------")
    print(datetime.now())

    df = pd.DataFrame()
    try:
        for i in range(100000):
            if i == 0:
                df = get_paginated_data(CommonConfig.DBPEDIA_LIMIT, i, query, sparql, df)
            else:
                print("Length of data frame now :" + str(len(df)))
                prev_len = len(df)
                df = get_paginated_data(CommonConfig.DBPEDIA_LIMIT, len(df) + 1, query, sparql, df)
                if prev_len == len(df):
                    break
    except Exception as e:
        print(e)
        print("Error in scraping DBpedia. Revise configurations.")
        sys.exit(1)
    return df


if __name__ == "__main__":
    # Inputs
    parser = argparse.ArgumentParser()
    parser.add_argument("-type", choices=["athlete"])
    args = parser.parse_args()
    q_type = args.type

    # Initialize SPARQLWrapper
    sparql = SPARQLWrapper(CommonConfig.DBPEDIA_URL)
    query = None

    # Generating Data Folder
    Helper.create_data_folder(CommonConfig.DATA_FOLDER_PATH)

    # Set Query based on input
    if q_type == "athlete":
        df = scrape_dbpedia(q_athletes, sparql)
    else:
        print("Not configured. Revise query type.")
        sys.exit(1)

    clean_data_and_save(df, q_type)
    print("Finished scraping DBpedia at: {}".format(datetime.now()))
