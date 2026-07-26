from sqlalchemy.exc import DatabaseError
from sqlalchemy.types import TIMESTAMP, VARCHAR, BIGINT
from sqlalchemy import text
from validate import validate_database_postload, RowCountValidationError
import pandas as pd  

# =====================
# LOAD
# =====================

def load_dataframe(df, engine, true_record_count):
    dtype_mapping = {
        'period': TIMESTAMP,
        'respondent': VARCHAR(4),
        'fueltype': VARCHAR(3),
        'value': BIGINT
    }

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
            try:
                query = text("SELECT COUNT(*) FROM daily_generation")
                result: int = connection.execute(query).scalar()
                validate_database_postload(result, true_record_count)
            except RowCountValidationError:
                raise
    except DatabaseError:
        raise



