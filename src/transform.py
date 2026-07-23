import json
import pandas as pd

# =====================
# TRANSFORM
# =====================

def transform_dataframe (paginated_response):

	df = pd.json_normalize(paginated_response)

	df = df[['period', 'respondent', 'fueltype', 'value']]

	df["period"] = pd.to_datetime(df["period"])

	print(df.columns.tolist())
	print("[TRANSFORM] Preview of transformed data:")
	print(df.head())

	return df