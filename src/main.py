from sqlalchemy import create_engine

from extract import extract_api_response, url
from transform import transform_dataframe
from load import load_dataframe
from validate import validate_record_count, validate_transformation_preload


metadata_total_records, paginated_response = extract_api_response(url)

if validate_record_count(metadata_total_records, paginated_response):
    engine = create_engine('postgresql+psycopg2://postgres@localhost:5432/eia_energy')
    df = transform_dataframe(paginated_response)
    if validate_transformation_preload(df, validate_record_count(metadata_total_records, paginated_response)):
        load_dataframe(df, engine)
    else:
        print('data transformation verification failed')
else:
    print('metadata verification failed, expected ', metadata_total_records, 
        ' request returned ', len(paginated_response), ' records')



