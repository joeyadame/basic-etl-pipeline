# =====================
# VALIDATE (functioned)
# =====================
class RowCountValidationError(Exception):
    #Exception for row count discrepencies between pipeline stages
    pass

def validate_extraction_records(metadata_total_records, paginated_response):
    if(len(paginated_response) == int(metadata_total_records)):
        return len(paginated_response)
    raise RowCountValidationError("Row counts do not match")

def validate_transformation_preload(df, verified_record_count):
    if(len(df) == verified_record_count):
        return len(df)
    raise RowCountValidationError("Row counts do not match")

def validate_database_postload(database_row_count, dataframe_row_count):
    if(database_row_count == dataframe_row_count):
        return True
    raise RowCountValidationError("Row counts do not match")