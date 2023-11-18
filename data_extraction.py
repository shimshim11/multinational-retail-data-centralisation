from database_utils import DatabaseConnector
from data_cleaning import DataCleaning
import pandas as pd
import requests
import tabula
import boto3


class DataExtractor():

    def __init__(self):
        pass

    def read_rds_table(self, engine, table):
        '''
        This function returns a pandas dataframe for the table name provided.

        Args:
            engine: An instance of the SQLAchemy engine.
            table: The name of the table that will be read from

        Returns:
            df: A dataframe with the data retrieved from the table.
        '''

        df = pd.read_sql_table(table, engine)

        return df

    def retrieve_pdf_data(self, pdf_path):
        '''
        This function retrieves a PDF file using the tabula import.

        Args:
            pdf_path: The URL of the pdf file.

        Returns:
            card_df: A dataframe with all the data from the PDF file.
        '''

        df = tabula.read_pdf(pdf_path, multiple_tables=False, pages='all', stream=True)
        card_df = df[0]
        return card_df

    def list_number_of_stores(stores_endpoint, headers):
        '''
        This function gets the total number of stores from an API endpoint.

        Args:
            stores_endpoint: The URL for the endpoint 
            headers: The header dictionary.
        
        Returns:
            int: The number of stores.
        '''
        response = requests.get(stores_endpoint, headers=headers)
        return int(response.text[37:40])

    def retrieve_stores_data(endpoint, headers):
        '''
        This function retrieves the store data by calling the API endpoint.

        Args:
            stores_endpoint: The URL for the endpoint 
            headers: The header dictionary.

        Returns:
            store_df: Dataframe containing the store data.
        '''
        data = []

        #The number of stores required is 451
        for store_number in range(0, 451):
            
            url = endpoint.format(store_number=store_number)
            response = requests.get(url, headers=headers)
            store_json = response.json()
            data.append(store_json)

        store_df = pd.DataFrame(data)

        return store_df
    
    def extract_from_s3(self, s3_address):
        '''
        This function extracts the CSV file from the S3 bucket called: "data-handling-public". 
        Using the boto3 import, it reads the CSV file from the S3 bucket.

        Args:
            s3_address: The URL for the CSV file in the S3 bucket.

        Returns:
            products_df = The dataframe with the contents from the CSV file.
        '''
        s3 = boto3.client('s3')

        # Removes the prefix for the URL and splits the address into the bucket name and access key.
        s3_bucket, s3_key = s3_address.split('/', 3)[-2:]
        obj = s3.get_object(Bucket=s3_bucket, Key=s3_key)

        products_df = pd.read_csv(obj['Body'], index_col=0)

        return products_df

    def extact_from_s3_json(self, s3_address):
        '''
        This function retrieves data from the S3 bucket which is a JSON file and store it in a dataframe.

        Args:
            s3_address: The URL for the JSON file in the S3 bucket.

        Returns:
            date_and_times: The dataframe with the contents from the JSON file.
        '''
        response = requests.get(s3_address)
        data = response.json()
        dates_and_times = pd.DataFrame(data)

        return dates_and_times
    