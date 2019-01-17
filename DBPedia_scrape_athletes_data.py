# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 12:33:15 2018

@author: Owner
"""

from pandas.io.json import json_normalize
from SPARQLWrapper import SPARQLWrapper, JSON
import Settings
import pandas as pd
import Cleaning_dataset
#import pdb

sparql = SPARQLWrapper(Settings.dbpedia_url)
athletes_df = pd.DataFrame()

def get_data_paginated(limit, offset):
    global athletes_df
    query = Settings.get_query(limit, offset)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    results = json_normalize(results['results']['bindings'])
    athletes_df = athletes_df.append(results)
    print(len(athletes_df))
    count = len(results)
    return count

print("-------------START SCRAPING-------------")
count = 0
for i in range(100000):
    if i == 0:
        count = get_data_paginated(Settings.dbpedia_limit, i)
    else:
        print(count + 1)
        print(Settings.dbpedia_limit)
        count = get_data_paginated(Settings.dbpedia_limit, len(athletes_df) + 1)
    if count < 10000:
        print("-------------WRITING TO EXCEL-------------")
        Cleaning_dataset.remove_types_columns(athletes_df)
        #Helper.write_to_pickle(athletes_df)
        #Helper.write_to_excel(athletes_df)
        break
print("-------------FINISHED SCRAPING-------------")

