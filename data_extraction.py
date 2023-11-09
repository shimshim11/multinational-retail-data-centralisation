from database_utils import DatabaseConnector
from data_cleaning import DataCleaning
import pandas as pd
import requests


class DataExtractor():

    def __init__(self):
        pass

    def read_rds_table(self, engine, table_name):

        df = pd.read_sql_table(table_name, engine)
        return df
    