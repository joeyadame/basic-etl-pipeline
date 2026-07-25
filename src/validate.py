# =====================
# VALIDATE (functioned)
# =====================

from exceptions import RowCountValidationError, DatabaseConectionError

def validate_record_count(metadata_total_records, paginated_response):
    if(len(paginated_response) == int(metadata_total_records)):
        return len(paginated_response)
    raise RowCountValidationError("Row counts do not match")

def validate_transformation_preload(df, verified_record_count):
    if(len(df) == verified_record_count):
        return True
    raise RowCountValidationError("Row counts do not match")
