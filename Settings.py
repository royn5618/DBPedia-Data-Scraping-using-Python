# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 23:03:34 2019

@author: NRoy
"""

dbpedia_url = "http://dbpedia.org/sparql"

#query = '''PREFIX foaf: <http://xmlns.com/foaf/0.1/>
#PREFIX dbo: <http://dbpedia.org/ontology/>
#PREFIX dbr: <http://dbpedia.org/resource/>
#PREFIX dbp: <http://dbpedia.org/property/>
#PREFIX ling: <http://purl.org/linguistics/gold/>
#SELECT DISTINCT ?a, ?b, ?d, ?e, ?g, ?h, ?i
#WHERE{?a a dbo:Athlete; dbo:birthDate ?b; dbo:country ?d ; dbo:height ?e; ling:hypernym ?g; foaf:gender ?h; foaf:name ?i.'''

#query = '''
#    PREFIX foaf: <http://xmlns.com/foaf/0.1/>
#    PREFIX dbo: <http://dbpedia.org/ontology/>
#    PREFIX dbr: <http://dbpedia.org/resource/>
#    PREFIX dbp: <http://dbpedia.org/property/>
#    PREFIX ling: <http://purl.org/linguistics/gold/>
#    SELECT DISTINCT ?a, ?b, ?c, ?d, ?e, ?f, ?g, ?h, ?i
#    WHERE{?a a dbo:Athlete; dbo:birthDate ?b; dbo:abstract ?c; 
#    dbo:country ?d ; dbo:height ?e; dct:description ?f;
#    ling:hypernym ?g; foaf:gender ?h;
#    foaf:name ?i.
#    FILTER(LANG(?c) = "en")}
#    '''
dbpedia_limit = 10000

def get_query(limit, offset):
    return f'''PREFIX foaf: <http://xmlns.com/foaf/0.1/>
    PREFIX dbo: <http://dbpedia.org/ontology/>
    PREFIX dbr: <http://dbpedia.org/resource/>
    PREFIX dbp: <http://dbpedia.org/property/>
    PREFIX ling: <http://purl.org/linguistics/gold/>
    SELECT DISTINCT ?a, ?dob, ?ht, ?hpn, ?g, ?name, ?c
    WHERE{{?a a dbo:Athlete; dbo:birthDate ?dob; dbo:height ?ht; ling:hypernym ?hpn; foaf:gender ?g; foaf:name ?name.
    OPTIONAL{{?a  dbo:country ?c}}
    FILTER(LANG(?name) = "en").
    }} ORDER BY ?name LIMIT {limit} OFFSET {offset}'''
