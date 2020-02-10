# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 12:33:15 2018

@author: Naba
"""

from pandas.io.json import json_normalize
from SPARQLWrapper import SPARQLWrapper, JSON
from Project1_Athletes import query
import pandas as pd
from Common import helper

#import pdb

sparql = SPARQLWrapper(query.dbpedia_url)
athletes_df = pd.DataFrame()


def get_paginated_data(limit, offset,  df):
    formatted_query = query.get_query(limit, offset)
    sparql.setQuery(formatted_query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    results = json_normalize(results['results']['bindings'])
    df = df.append(results)
    print(len(df))
    count = len(results)
    return count


if __name__ == "__main__":
    print("-------------START SCRAPING-------------")
    count = 0
    for i in range(100000):
        if i == 0:
            count = get_paginated_data(query.dbpedia_limit, i)
        else:
            print(count + 1)
            print(query.dbpedia_limit)
            count = get_paginated_data(query.dbpedia_limit, len(athletes_df) + 1)
        if count < 10000:
            print("-------------WRITING TO PKL-------------")
            helper.remove_types_columns()
            # Helper.write_to_pickle(athletes_df)
            # Helper.write_to_excel(athletes_df)
            break
    print("-------------FINISHED SCRAPING-------------")

