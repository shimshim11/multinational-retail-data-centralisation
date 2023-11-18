/* Task 1: orders_table */
ALTER TABLE orders_table
    ALTER COLUMN date_uuid TYPE uuid USING date_uuid::uuid;
    ALTER COLUMN user_uuid TYPE uuid USING user_uuid::uuid;
    ALTER COLUMN card_number TYPE VARCHAR(30),
    ALTER COLUMN store_code TYPE VARCHAR(15),
    ALTER COLUMN product_code TYPE VARCHAR(15),
    ALTER COLUMN product_quantity TYPE SMALLINT;

/* Task 2: dim_users_table */
ALTER TABLE dim_users
    ALTER COLUMN first_name TYPE VARCHAR(255),
    ALTER COLUMN last_name TYPE VARCHAR(255),
    ALTER COLUMN date_of_birth TYPE DATE,
    ALTER COLUMN country_code TYPE VARCHAR(5),
    ALTER COLUMN user_uuid TYPE uuid USING user_uuid::uuid,
    ALTER COLUMN join_date TYPE DATE;

/* Task 3: dim_store_details */
ALTER TABLE dim_store_details
    ALTER COLUMN longitude TYPE FLOAT USING longitude::FLOAT,
    ALTER COLUMN locality TYPE VARCHAR(255),
    ALTER COLUMN store_code TYPE VARCHAR(15),
    ALTER COLUMN staff_numbers TYPE SMALLINT USING staff_numbers::SMALLINT,
    ALTER COLUMN opening_date TYPE DATE,
    ALTER COLUMN store_type TYPE VARCHAR(255),
    ALTER COLUMN store_type DROP NOT NULL,
    ALTER COLUMN latitude TYPE FLOAT USING latitude::FLOAT,
    ALTER COLUMN country_code TYPE VARCHAR(5),
    ALTER COLUMN continent TYPE VARCHAR(255);

/* Task 4: dim_products */
UPDATE dim_products
    SET product_price = REPLACE(product_price, '£', '');

ALTER TABLE dim_products
    ADD COLUMN weight_class VARCHAR(15);

UPDATE dim_products
    SET weight_class =
        CASE 
            WHEN weight < 2 THEN 'Light'
            WHEN weight > 2 AND weight <= 40 THEN 'Mid_Sized'
            WHEN weight > 40 AND weight <= 140 THEN 'Heavy'
            WHEN weight > 140 THEN 'Truck_Required'
        END;


/* Task 5: dim_products */
ALTER TABLE dim_products RENAME removed TO still_available;

ALTER TABLE dim_products
    ALTER COLUMN product_price TYPE FLOAT USING product_price::FLOAT,
    ALTER COLUMN weight TYPE FLOAT,
    ALTER COLUMN "EAN" TYPE VARCHAR(20),
    ALTER COLUMN product_code TYPE VARCHAR(15),
    ALTER COLUMN date_added TYPE DATE,
    ALTER COLUMN "uuid" TYPE uuid USING "uuid":uuid,
    ALTER COLUMN still_available TYPE bool USING still_available:bool
    ALTER COLUMN weight_class TYPE VARCHAR(25);

/* Task 6: dim_date_times */
ALTER TABLE dim_date_times
    ALTER COLUMN month TYPE VARCHAR(2),
    ALTER COLUMN year TYPE VARCHAR(4),
    ALTER COLUMN day TYPE VARCHAR(2),
    ALTER COLUMN time_period TYPE VARCHAR(10),
    ALTER COLUMN date_uuid TYPE uuid USING date_uuid::uuid;

/* Task 7: dim_card_details */
ALTER TABLE dim_card_details
    ALTER COLUMN card_number TYPE VARCHAR(20),
    ALTER COLUMN expiry_date TYPE VARCHAR(5),
    ALTER COLUMN date_payment_confirmed TYPE DATE;

/* Task 8: Add primary keys */
ALTER TABLE dim_users 
ADD PRIMARY KEY (user_uuid);

ALTER TABLE dim_store_details
ADD PRIMARY KEY (store_code);

ALTER TABLE dim_products 
ADD PRIMARY KEY (product_code);

ALTER TABLE dim_date_times 
ADD PRIMARY KEY (date_uuid);

ALTER TABLE dim_card_details 
ADD PRIMARY KEY (card_number);

/* Task 9: Add foreign keys */
ALTER TABLE orders_table
    ADD FOREIGN KEY (user_uuid) REFERENCES dim_users(user_uuid),
    ADD FOREIGN KEY (store_code) REFERENCES dim_store_details(store_code),
    ADD FOREIGN KEY (product_code) REFERENCES dim_products(product_code),
    ADD FOREIGN KEY (date_uuid) REFERENCES dim_date_times(date_uuid),
    ADD FOREIGN KEY (card_number) REFERENCES dim_card_details(card_number);