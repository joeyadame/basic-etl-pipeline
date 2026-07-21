from sqlalchemy import create_engine

from extract import extract_api_response, url
from transform import transform_dataframe
from load import load_dataframe

from validate import validate_record_count


metadata_total_records, paginated_response = extract_api_response(url)

validate_record_count(metadata_total_records, paginated_response)

df = transform_dataframe(paginated_response)

engine = create_engine('postgresql+psycopg2://postgres@localhost:5432/eia_energy')

load_dataframe(df, engine)



