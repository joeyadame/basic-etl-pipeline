from sqlalchemy import create_engine
from sqlalchemy.exc import DatabaseError
from extract import extract_api_response, url
from transform import transform_dataframe
from load import load_dataframe
from validate import validate_extraction_records, validate_transformation_preload, RowCountValidationError
import sys

metadata_total_records, paginated_response = extract_api_response(url)

try:
    true_record_count = validate_extraction_records(metadata_total_records, paginated_response)
except RowCountValidationError as e:
    print(f"API does not match metadata: {e}")
    sys.exit(1)

engine = create_engine('postgresql+psycopg2://postgres@localhost:5432/eia_energy')

transformed_df = transform_dataframe(paginated_response)

try:
    true_record_count = validate_transformation_preload(transformed_df, true_record_count)
except RowCountValidationError as e:
    print(f"transformed data does not match API response: {e}")
    sys.exit(1)

try:
    load_dataframe(transformed_df, engine, true_record_count)
except DatabaseError as e:
    print(f"Pipeline failed during load: {e}")
    sys.exit(1)
except RowCountValidationError as e:
    print(f"Loaded data does not match transformed load_dataframe: {e}")
    sys.exit(1)




