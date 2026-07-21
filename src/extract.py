import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("EIA_API_KEY")

url = f"https://api.eia.gov/v2/electricity/rto/daily-fuel-type-data/data/?api_key={API_KEY}&frequency=daily&data[0]=value&facets[respondent][]=ERCO&facets[timezone][]=Central&sort[0][column]=period&sort[0][direction]=desc"

# =====================
# EXTRACT (functioned)
# =====================

def extract_api_response(API_url):

    response = requests.get(API_url)
    response.raise_for_status()
    response_json = response.json()
    metadata_total_records = response_json.get('response', {}).get('total', '0')
    print(f"[EXTRACT] Metadata reports {metadata_total_records} total records.")

    paginated_response = []
    for i in range(-(-int(metadata_total_records)//5000)):
    	limit = 5000
    	offset = i*limit
    	pagination_parameters = {
    	"offset": offset,
    	}
    	print(f"[EXTRACT] Fetching page starting at offset {offset}.")
    	#append to list with results
    	temp_paginated_response = requests.get(API_url, params = pagination_parameters)
    	temp_paginated_response_json = temp_paginated_response.json()
    	#print(temp_paginated_response_json)
    	paginated_response.extend(temp_paginated_response_json["response"]["data"])

    return metadata_total_records, paginated_response
