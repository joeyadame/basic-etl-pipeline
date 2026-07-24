from sqlalchemy import create_engine

from extract import extract_api_response, url
from transform import transform_dataframe
from load import load_dataframe
from validate import validate_record_count, validate_transformation_preload


metadata_total_records, paginated_response = extract_api_response(url)

true_record_count = validate_record_count(metadata_total_records, paginated_response)
engine = create_engine('postgresql+psycopg2://postgres@localhost:5432/eia_energy')
df = transform_dataframe(paginated_response)
validate_transformation_preload(df, true_record_count)
load_dataframe(df, engine)



