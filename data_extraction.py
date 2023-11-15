from database_utils import DatabaseConnector
from data_cleaning import DataCleaning
import pandas as pd
import requests


class DataExtractor():

    def __init__(self):
        pass

    def read_rds_table(self, engine, table):

        df = pd.read_sql_table(table, engine)

        return df

db_conn = DatabaseConnector()
db_ext = DataExtractor() 

users = db_ext.read_rds_table(table='legacy_users', engine = db_conn.engine)
clean_df = DataCleaning.clean_user_data(users)
db_conn.upload_to_db(clean_df, 'dim_users')