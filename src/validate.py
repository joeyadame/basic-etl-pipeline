# =====================
# VALIDATE (functioned)
# =====================
import sys

def validate_record_count(metadata_total_records, paginated_response):
    if(len(paginated_response) == int(metadata_total_records)):
        return len(paginated_response)
    sys.exit("metatata record count validation failed, terminating extraction execution")

def validate_transformation_preload(df, verified_record_count):
    if(len(df) == verified_record_count):
        return True
    sys.exit("preload record count validation failed, terminating extraction execution")
