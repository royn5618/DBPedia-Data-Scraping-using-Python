# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 12:33:15 2018

@author: Owner
"""

#dbo:abstract
#dbo:birthDate (xsd:date)
#dbo:country
#dbo:height (xsd:double)
#dct:description
#http://purl.org/linguistics/gold/hypernym	dbr:Player
#foaf:gender
#foaf:name (en)
#dbo:Athlete

from pandas.io.json import json_normalize
from SPARQLWrapper import SPARQLWrapper, JSON
from pandas import ExcelWriter
import Settings
import pandas as pd

sparql = SPARQLWrapper(Settings.dbpedia_url)
athletes_df = pd.DataFrame()

def get_data_paginated(limit, offset):
#    import pdb
#    pdb.set_trace()
    query = Settings.get_query(limit, offset)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results=sparql.query().convert()
    results = json_normalize(results['results']['bindings'])
    athletes_df = athletes_df.append(results)
    #print(results)
    count = len(results)
    return count
    
def write_to_excel(df):
    writer = ExcelWriter('athletes_details' + '.xlsx')
    df.to_excel(writer)
    writer.save()
    print('done')

print("-------------START SCRAPING-------------")
count = 0
for i in range(100000):
    if i == 0:
        count = get_data_paginated(Settings.dbpedia_limit, i)
    else:
        print(count + 1)
        print(Settings.dbpedia_limit * i)
        count = get_data_paginated(Settings.dbpedia_limit , len(athletes_df) + 1)
    if count < 10000:
        break
print("-------------FINISHED SCRAPING-------------")

