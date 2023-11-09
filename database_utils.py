from sqlalchemy import create_engine, inspect
import pandas as pd
import yaml
import psycopg2
import requests
import sqlalchemy

    
class DatabaseConnector():    

    def read_db_creds(self):
        
        with open('db_creds.yaml') as f:
            return yaml.safe_load(f)

    def init_db_engine(self):
        creds = self.read_db_creds()
        return create_engine (f"postgresql://{creds['RDS_USER']}:{creds['RDS_PASSWORD']}@{creds['RDS_HOST']}:{creds['RDS_PORT']}/{creds['RDS_DATABASE']}")
    
    def list_db_tables(self, engine):
        
        data = self.init_db_engine()
        data.connect()
        inspector = inspect(data)
        print(inspector.get_table_names)
    
    
    def upload_to_db(self, df, table_name):
    
        creds = self.read_db_creds("db_local_creds.yaml")
        engine = self.init_db_engine(creds)
        conn = engine.connect()
        
        df.to_sql(table_name, engine, if_exists = "replace")

        conn.close()
