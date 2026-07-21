# =====================
# VALIDATE (functioned)
# =====================

def validate_record_count(metadata_total_records, paginated_response):
    if(len(paginated_response) == int(metadata_total_records)):
        print('metadata matches total records witin request', 
            '\nmetadata returned ', metadata_total_records, 'records, \npaginated response contains',
            len(paginated_response), 'records')
    else:
        print('discrepency between metadata containing total records and amount of records returned by the request,\n',
            'please verify the following:')
        #I must specify the most likely causes of this issue as I dive further into this project
