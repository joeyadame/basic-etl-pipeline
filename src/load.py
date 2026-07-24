from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.types import TIMESTAMP, VARCHAR, BIGINT
from sqlalchemy import text
import pandas as pd  

# =====================
# LOAD
# =====================

def load_dataframe(df, engine):
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
         #Post load inspection
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
        df_output = pd.read_sql_query(query, con=engine)
        print(df_output)

    except SQLAlchemyError:
        raise

