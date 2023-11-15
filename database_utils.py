from data_cleaning import DataCleaning
from sqlalchemy import create_engine, inspect
import pandas as pd
import yaml
import psycopg2
import requests
import sqlalchemy

    
class DatabaseConnector():    

    def __init__(self):

        self.creds = self.read_db_creds()
        self.engine = self.init_db_engine()

    

    def read_db_creds(self):
        
        with open('db_creds.yaml') as f:
            return yaml.safe_load(f)

    def init_db_engine(self):
    
        connector = f"postgresql://{self.creds['RDS_USER']}:{self.creds['RDS_PASSWORD']}@{self.creds['RDS_HOST']}:{self.creds['RDS_PORT']}/{self.creds['RDS_DATABASE']}"
        engine = create_engine(connector)
        return engine
    
    def list_db_tables(self):
        
        data = self.init_db_engine()
        data.connect()
        inspector = inspect(data)
        print(inspector.get_table_names())
    
    
    def upload_to_db(self, df, table_name):
    
        with open('db_local_creds.yaml') as f:
            creds = yaml.safe_load(f)

        engine = create_engine(f"{'postgresql'}+{'psycopg2'}://{creds['user']}:{creds['password']}@{creds['host']}:{creds['port']}/{creds['dbname']}")
        engine.connect()
        df.to_sql(table_name, engine, if_exists='replace')

db_conn = DatabaseConnector()
db_conn.list_db_tables()
