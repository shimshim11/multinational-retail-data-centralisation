import pandas as pd

class DataCleaning():

    def clean_user_data(table):

        df = table
        df.info()

        df['country_code'] = df['country_code'].astype('category')
        df['date_of_birth'] = pd.to_datetime(df['date_of_birth'], infer_datetime_format=True, errors='coerce')
        df['join_date'] = pd.to_datetime(df['join_date'], infer_datetime_format=True, errors='coerce')
        df.dropna(how='all', inplace=True)
        pattern = r'^[a-zA-Z0-0]*$'
        mask = (df['date_of_birth'].isna()) | (df['date_of_birth'].astype(str).str.contains(pattern))
        df = df[~mask]

        pd.set_option('display.max_columns', None)
        
        return df
