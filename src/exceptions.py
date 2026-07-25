# exceptions.py

class DatabaseConnectionError(Exception):
	#Exception for failed DB conection
	pass

class RowCountValidationError(Exception):
	#Exception for row count discrepencies between pipeline stages
	pass
