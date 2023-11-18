import pandas as pd
from data_cleaning import DataCleaning
from data_extraction import DataExtractor
from database_utils import DatabaseConnector

def upload_dim_users():
    extractor = DataExtractor()
    reader = DatabaseConnector()

    users = extractor.read_rds_table(table='legacy_users', engine = reader.engine)
    clean_df = DataCleaning.clean_user_data(users)
    reader.upload_to_db(clean_df, 'dim_users')

def upload_cards_details():
    extractor = DataExtractor()
    reader = DatabaseConnector()

    card_df = extractor.retrieve_pdf_data("https://data-handling-public.s3.eu-west-1.amazonaws.com/card_details.pdf")
    clean_card_df = DataCleaning.clean_card_data(card_df)
    reader.upload_to_db(clean_card_df, 'dim_card_details')

def upload_store_details():
    extractor = DataExtractor()
    reader = DatabaseConnector()

    headers={'x-api-key': 'yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX'}
    stores_data = "https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/store_details/{store_number}"
    store_data = extractor.retrieve_stores_data(stores_data, headers)
    cleaned_store_data = DataCleaning.clean_store_data(store_data)
    reader.upload_to_db(cleaned_store_data, 'dim_store_details')

def upload_products():
    extractor = DataExtractor()
    reader = DatabaseConnector()
    
    products_df = extractor.extract_from_s3("s3://data-handling-public/products.csv")
    converted_weights = DataCleaning.convert_product_weights(products_df)
    reader.upload_to_db(converted_weights, 'dim_products')

def upload_orders():
    extractor = DataExtractor()
    reader = DatabaseConnector()

    orders_df = extractor.read_rds_table(table="orders_table", engine=reader.engine)
    clean_orders = DataCleaning.clean_orders_data(orders_df)
    reader.upload_to_db(clean_orders, 'orders_table')

def upload_date_times():
    extractor = DataExtractor()
    reader = DatabaseConnector()

    s3 = "https://data-handling-public.s3.eu-west-1.amazonaws.com/date_details.json"
    date_times = extractor.extact_from_s3_json(s3)
    clean_date_df = DataCleaning.clean_date_times(date_times)
    reader.upload_to_db(clean_date_df, 'dim_date_times')

#if __name__ == '__main__':
#upload_dim_users()
#upload_card_details()
#upload_store_details()
#upload_products()
#upload_orders()
#upload_orders()
#upload_date_times()