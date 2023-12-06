/* Task 1: How many stores does the business have and in which countries? */
SELECT 
    country_code AS country,
    COUNT(*) AS total_no_stores
FROM dim_store_details
GROUP BY country_code
ORDER BY total_no_stores DESC;

/* Task 2: Which locations currently have the most stores? */
SELECT
    locality,
    COUNT(*) AS total_no_stores
FROM dim_store_details
GROUP BY locality
ORDER BY total_no_stores DESC
LIMIT 7;

/* Task 3: Which months produced the largest amount of sales? */
SELECT 
    ROUND(TOTAL(p."product_price (£)" * o.product_quantity), 2) AS total_sales, d.month
FROM 
    orders_table AS o
JOIN
    dim_date_times as d ON o.date_uuid = d.date_uuid
JOIN
    dim_products as p ON o.product_code = p.product_code
GROUP BY
    d.month
ORDER BY 
    total_sales DESC
LIMIT 6;

/* Task 4: How many sales are coming from online? */
SELECT 
    COUNT(*) AS number_of_sales,
    SUM(product_quantity) AS product_quantity_count,
    CASE
        WHEN 'Web Portal' THEN ' Web'
        ELSE 'Offline'
    END AS location  
FROM
    orders_table
GROUP BY
    location
ORDER BY
    number_of_sales;
    
/* Task 5: What percentage of sales come through each type of store? */
SELECT
    dim_store_details.store_type AS store_type,
    ROUND(SUM(o.product_quantity * dp.product_price)::numeric, 2) AS total_sales,
    ROUND(SUM(o.product_quantity * dim_products.product_price) /
        (SELECT
            SUM(o.product_quantity * dp.product_price)
        FROM
            orders_table
        JOIN dim_products ON o.product_code = dp.product_code) * 100)::numeric, 2)
    AS "percentage_total(%)"
FROM
    orders_table AS o
JOIN
    dim_products AS dp 
ON
    o.product_code = dim_products.product_code
JOIN
    dim_store_details AS ds
ON 
    o.store_code = ds.store_code
GROUP BY
    store_type
ORDER BY
    "percentage_total(%)" DESC;

/* Task 6: Which month in each year produced the highest cost of sales? */
SELECT
    ROUND(SUM(product_price * product_quantity):: numeric, 2) as total_sales,
    year,
    month,
FROM
    orders_table AS o
JOIN
    dim_date_times AS dt 
ON 
    o.date_uuid = dt.date_uuid
JOIN
    dim_products AS dp
ON
    o.product_code = dp.product_code
GROUP BY
    year, month
ORDER BY
    total_sales DESC
LIMIT 10;


/* Task 7: What is our staff headcount? */
SELECT
    SUM(staff_numbers) AS total_staff_numbers,
    country_code
FROM
    dim_store_details
GROUP BY
    country_code
ORDER BY
    total_staff_numbers DESC;

/* Task 8: Which German store is selling the most? */
SELECT
    ROUND(SUM(product_price * product_quantity):: numeric, 2) AS total_sales,
    store_type
    country_code
FROM
    orders_table AS o
JOIN
    dim_store_details AS ds
ON
    o.store_code = ds.store_code
JOIN
    dim_products AS dp 
ON 
    o.product_code = dp.product_code
WHERE 
    country_code = 'DE'
GROUP BY
    country_code, store_type
ORDER BY
    total sales ASC;

/* Task 9: How quickly is the company making sales? */
WITH sales_date AS (
    SELECT 
        year,
        TO_TIMESTAMP(CONCAT(year, '-', month, '-', day, ' ', timestamp), 'YYYY-MM-DD HH24:MI:SS') AS sales_date_column,
        LAG(TO_TIMESTAMP(CONCAT(year, '-', month, '-', day, ' ', timestamp), 'YYYY-MM-DD HH24:MI:SS')) OVER (PARTITION BY year ORDER BY TO_TIMESTAMP(CONCAT(year, '-', month, '-', day, ' ', timestamp), 'YYYY-MM-DD HH24:MI:SS')) AS previous_sale_date
    FROM 
        dim_date_times
)
SELECT 
    year,
    '{"hours": ' || EXTRACT(HOUR FROM AVG(sales_date_column - previous_sale_date)) || ', "minutes": ' || EXTRACT(MINUTE FROM AVG(sales_date_column - previous_sale_date)) || ', "seconds": ' || EXTRACT(SECOND FROM AVG(sales_date_column - previous_sale_date)) || ', "milliseconds": ' || EXTRACT(MILLISECOND FROM AVG(sales_date_column - previous_sale_date)) || '}' AS actual_time_taken
FROM 
    sales_date
WHERE 
    previous_sale_date IS NOT NULL
GROUP BY 
    year
ORDER BY 
    AVG(sales_date_column - previous_sale_date) DESC
LIMIT 5;