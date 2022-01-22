import pandas as pd
import pandasql as pdsql


def read_files():
    countries = pd.read_csv("app/db/data/countries.csv", sep=";")
    states = pd.read_csv("app/db/data/states.csv", sep=";")
    cities = pd.read_csv("app/db/data/cities.csv", sep=";")

    return countries, cities, states


def exec_query(countries, cities, states, query):
    return pdsql.sqldf(query, locals())
