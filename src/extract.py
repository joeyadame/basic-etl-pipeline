import requests
import json
import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.types import TIMESTAMP, VARCHAR, BIGINT
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("EIA_API_KEY")

url = f"https://api.eia.gov/v2/electricity/rto/daily-fuel-type-data/data/?api_key={API_KEY}&frequency=daily&data[0]=value&facets[respondent][]=ERCO&facets[timezone][]=Central&sort[0][column]=period&sort[0][direction]=desc"

response = requests.get(url)
response.raise_for_status()
response_json = response.json()
metadata_total_records = response_json.get('response', {}).get('total', '0')
print(metadata_total_records)

paginated_response = []
for i in range(-(-int(metadata_total_records)//5000)):
	limit = 5000
	offset = i*limit
	pagination_parameters = {
	"offset": offset,
	}
	print(offset)
	#append to list with results
	temp_paginated_response = requests.get(url, params = pagination_parameters)
	temp_paginated_response_json = temp_paginated_response.json()
	#print(temp_paginated_response_json)
	paginated_response.extend(temp_paginated_response_json["response"]["data"])

df = pd.json_normalize(paginated_response)

if(len(paginated_response) == int(metadata_total_records)):
    print('metadata matches total records witin request', 
        '\nmetadata returned ', metadata_total_records, 'records, \npaginated response contains',
        len(paginated_response), 'records')
else:
    print('discrepency between metadata containing total records and amount of records returned by the request,\n',
        'please verify the following:')
    #I must specify the most likely causes of this issue as I dive further into this project


df = df[['period', 'respondent', 'fueltype', 'value']]

df["period"] = pd.to_datetime(df["period"])

dtype_mapping = {
	'period': TIMESTAMP,
	'respondent': VARCHAR(4),
	'fueltype': VARCHAR(3),
	'value': BIGINT
}

print(df.columns.tolist())
print(df.head())

engine = create_engine('postgresql+psycopg2://postgres@localhost:5432/eia_energy')

try:
    # Attempt to actually connect to the database
    with engine.connect() as connection:
        df.to_sql(
            name='daily_generation',
            con=connection,      # Pass the live connection instead of the engine
            if_exists='replace',
            index=False,
            dtype=dtype_mapping
        )
    print("Data exported successfully.")
except OperationalError as e:
    print(f"Database connection failed: {e}")

query = text("""
SELECT 
    column_name,
    data_type,
    is_nullable,
    character_maximum_length
FROM
    information_schema.columns
WHERE
    table_schema = 'public'
    AND table_name = 'daily_generation';
    """)

try:
    df_output = pd.read_sql_query(query, con=engine)
    print(df_output)
except Exception as e:
    print(f"Query failed: {e}")




