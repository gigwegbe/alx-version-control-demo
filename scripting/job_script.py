import requests
import pandas as pd


url = "https://countrycode.org/"


def get_url(url):
    response = requests.get(url).content
    return response


site_url = get_url(url)
table = pd.read_html(site_url)
table_df = pd.DataFrame(table[-2])


def country_code_head(df):
    return df.head()


def country_code_tail(df):
    return df.tail()


def country_code_sample(df):
    return df.sample(5)


# print(country_code_head(table_df))
# print(country_code_sample(table_df))
# print(country_code_tail(table_df))

# ---------------------
# - save to disk api
# -
