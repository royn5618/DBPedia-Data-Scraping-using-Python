# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 23:03:34 2019
@author: NRoy
"""


# LATEST Working Query
def get_query(limit, offset):
    return f'''PREFIX foaf: <http://xmlns.com/foaf/0.1/>
    PREFIX dbo: <http://dbpedia.org/ontology/>
    PREFIX dbr: <http://dbpedia.org/resource/>
    PREFIX dbp: <http://dbpedia.org/property/>
    SELECT DISTINCT ?a, ?dob, ?ht, ?name, ?c, ?intro
    WHERE{{?a a dbo:Athlete; dbo:birthDate ?dob; dbo:height ?ht;
    foaf:name ?name; dbo:abstract ?intro.
    OPTIONAL{{?a  dbo:country ?c}}
    FILTER(LANG(?name) = "en").
    }} LIMIT {limit} OFFSET {offset}'''

# OLD Query: foaf:gender and ling:hypernym are removed. This query will not yield any results.
# def get_query(limit, offset):
#     return f'''PREFIX foaf: <http://xmlns.com/foaf/0.1/>
#     PREFIX dbo: <http://dbpedia.org/ontology/>
#     PREFIX dbr: <http://dbpedia.org/resource/>
#     PREFIX dbp: <http://dbpedia.org/property/>
#     PREFIX ling: <http://purl.org/linguistics/gold/>
#     SELECT DISTINCT ?a, ?dob, ?ht, ?hpn, ?g, ?name, ?c, ?intro
#     WHERE{{?a a dbo:Athlete; dbo:birthDate ?dob; dbo:height ?ht;
#     ling:hypernym ?hpn; foaf:gender ?g; foaf:name ?name; dbo:abstract ?intro.
#     OPTIONAL{{?a  dbo:country ?c}}
#     FILTER(LANG(?name) = "en").
#     }} LIMIT {limit} OFFSET {offset}'''
