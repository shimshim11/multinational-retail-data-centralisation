import pandas as pd

class DataCleaning():

    def clean_user_data(table):
        '''
        The function cleans the user information.

        Args:
            table: The name of the table that will be cleaned.

        Returns: 
            df: The cleaned dataframe. 
        '''
        df = table

        df['country_code'] = df['country_code'].astype('category')
        df['date_of_birth'] = pd.to_datetime(df['date_of_birth'], infer_datetime_format=True, errors='coerce')
        df['join_date'] = pd.to_datetime(df['join_date'], infer_datetime_format=True, errors='coerce')
        df.dropna(how='all', inplace=True)
        pattern = r'^[a-zA-Z0-9]*$'
        mask = (df['date_of_birth'].isna()) | (df['date_of_birth'].astype(str).str.contains(pattern))
        df = df[~mask]

        pd.set_option('display.max_columns', None)
        
        return df

    def clean_card_data(table):
        '''
        The function cleans the card information.

        Args:
            table: The name of the table that will be cleaned.

        Returns: 
            card_df: The cleaned dataframe. 
        '''
        card_df = table

        card_df.dropna(how='all', inplace=True)
        card_df['date_payment_confirmed'] = pd.to_datetime(card_df['date_payment_confirmed'], infer_datetime_format=True, errors='coerce')
        pattern = pattern = r'^[a-zA-Z0-9]*$'
        mask = (card_df['date_payment_confirmed'].isna()) | (card_df['date_payment_confirmed'].astype(str).str.contains(pattern))
        card_df = card_df[~mask]
        pattern = r'[^0-9]'
        card_df['card_number'] = card_df['card_number'].replace(pattern, '', regex=True)
        
        return card_df

    def clean_store_data(table):
        '''
        The function cleans the store information.

        Args:
            table: The name of the table that will be cleaned.

        Returns: 
            store_df: The cleaned dataframe. 
        '''
        store_df = table

        store_df.drop(columns='lat',inplace=True)
        store_df.dropna(how='any', inplace=True)
        store_df['opening_date'] = pd.to_datetime(store_df['opening_date'], infer_datetime_format=True, errors='coerce')
        pattern = pattern = r'^[a-zA-Z0-9]*$'
        mask = (store_df['opening_date'].isna()) | (store_df['opening_date'].astype(str).str.contains(pattern))
        store_df = store_df[~mask]

        return store_df
    
    def convert_product_weights(table):
        '''
        The function cleans the user information.

        Args:
            table: The name of the table that will be cleaned.

        Returns: 
            products_df: The cleaned dataframe. 
        '''
        products_df = table

        products_df.dropna(how='all', inplace=True)
        products_df['date_added'] = pd.to_datetime(products_df['date_added'], infer_datetime_format=True, errors='coerce')
        pattern = r'^[a-zA-Z0-9]*$'
        mask = (products_df['date_added'].isna()) | (products_df['date_added'].astype(str).str.contains(pattern))
        products_df = products_df[~mask]

        units = []
        for i in products_df['weight']:
            #Removes any leading spaces, punctuation or numbers
            i = str(i).strip('.')
            i = str(i).strip('l')
            i = str(i).strip()
            if i.endswith('kg'):
                units.append(float(i[:-2]))
            elif 'x' in i:
                num, unit = i.split('x')
                units.append(float(num)*float(unit.rstrip('g'))/1000)
            elif i.endswith('g'):
                units.append(float(i[:-1])/1000)
            elif i.endswith('m'):
                units.append(float(i[:-1])/1000)
            elif i.endswith('oz'):
                units.append(float(i[:-2])*0.0283)
            else:
                units.append(float(i))

        products_df.loc[:, 'weight'] = units
        return products_df

    def clean_orders_data(table):
        '''
        The function cleans the orders table information.

        Args:
            table: The name of the table that will be cleaned.

        Returns: 
            clean_orders_df: The cleaned dataframe. 
        '''
        clean_orders_df = table

        clean_orders_df.drop(columns='1',inplace=True)
        clean_orders_df.drop(columns='first_name',inplace=True)
        clean_orders_df.drop(columns='last_name',inplace=True)
        del clean_orders_df['index']

        clean_orders_df.reset_index(drop=True)
        clean_orders_df.drop(columns='level_0',inplace=True)
        clean_orders_df.dropna(how='any')

        return clean_orders_df

    def clean_date_times(table):
        '''
        The function cleans the dates and time information from AWS S3 JSON.

        Args:
            table: The name of the table that will be cleaned.

        Returns: 
            clean_date_df: The cleaned dataframe. 
        '''
        clean_date_df = table
        clean_date_df.dropna(how='any',inplace= True)

        clean_date_df['day'] =  pd.to_numeric(clean_date_df['day'],errors='coerce', downcast="integer")
        clean_date_df['month'] =  pd.to_numeric(clean_date_df['month'], errors='coerce', downcast="integer")
        clean_date_df['year'] =  pd.to_numeric(clean_date_df['year'], errors='coerce', downcast="integer")

        clean_date_df['timestamp'] = pd.to_datetime(clean_date_df['timestamp'], format='%H:%M:%S', errors='coerce')

        return clean_date_df


