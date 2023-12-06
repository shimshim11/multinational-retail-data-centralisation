# Multinational Retail Data Centralisation
You work for a multinational company that sells various goods across the globe.

Currently, their sales data is spread across many different data sources making it not easily accessible or analysable by current members of the team.

In an effort to become more data-driven, your organisation would like to make its sales data accessible from one centralised location.

The goal will be to produce a system that stores the current company data in a database so that it's accessed from one centralised location and acts as a single source of truth for sales data.

You will then query the database to get up-to-date metrics for the business.

## Installation Instructions:
### 1. Clone the repository:
```bash
git clone https://github.com/shimshim11/multinational-retail-data-centralisation.git
```
### 2. Install dependencies:
```bash
pip install -r requirements.txt
```
### 3. Execute the project:

Navigate to the main.py file. In here you will find all the functions needed to extract/clean/upload data to the local database. Simply choose which function you want to execute.
```bash
python data_cleaning.py
python data_extraction.py
python database_utils.py

#Or to run all the completed functions, use:
python main.py
```
Then choose the module you would like to run based on the Milestone and task.

## Project Aims:
In the following the project, data has been collected from a company regarding their sales. The data has been extracted from external sources, and then cleaned in order to uploaded to a local database, and use the new and cleaned data to provide the company with insights into their sales.

    - The data was extracted from the following sources: CSV, PDF, AWS S3, API and JSON.
    - The data was cleaned using pandas from NULL values, dupilicates, repeating data and formatting.
    - The data was uploaded to a local SQL postgres database.
    - The data was queried to add new columns and rows and foreign and primary keys.
    - The data was queried to generate insights about the company during specific time frames and conditions.

## File Structure:

- `data_cleaning.py` - Deals with cleaning the extracted data ready to be uploaded to the local database.
- `data_extraction.py` - Extracts the data from the various data sources, ready to be cleaned.
- `database_utils.py` - Establishes a connection between the pandas dataframe and the data source.
- `db.creds.yaml` - The credentials used to connect to the AWS data storage.
- `db_local_creds.yaml` - The credentials used to connect to the local SQL postgres database.
- `Milestone_3.sql` - The SQL queries for Milestone 3.
- `Milestone_4.sql` - The SQL queries for Milestone 4.


## License Information:
MIT License

Copyright (c) [2023] [Shimon Kocor]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.