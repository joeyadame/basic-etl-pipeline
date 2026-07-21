import json
import pandas as pd
from sqlalchemy.types import TIMESTAMP, VARCHAR, BIGINT

# =====================
# TRANSFORM
# =====================

def transform_dataframe (paginated_response):

	df = pd.json_normalize(paginated_response)

	df = df[['period', 'respondent', 'fueltype', 'value']]

	df["period"] = pd.to_datetime(df["period"])

	dtype_mapping = {
		'period': TIMESTAMP,
		'respondent': VARCHAR(4),
		'fueltype': VARCHAR(3),
		'value': BIGINT
	}

	print(df.columns.tolist())
	print("[TRANSFORM] Preview of transformed data:")
	print(df.head())

	return df