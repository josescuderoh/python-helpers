

def to_dict(df):
	"""Generic function to convert data frame into formatted dictionary to send registers to database"""
	# Extract the names
	names = list(df.columns.values)
	# Create sequence
	df_list = []
	#Iterate over rows of data frame
	for index, row in df.iterrows():
		# Create temporary object
		temp_dict = {}
		#Iterate over key names and add values
		for name in names:
			temp_dict[name] = row[name]
		# Append object to dictionary
		df_list.append(temp_dict.copy())
	
	return df_list

def to_tuple(df):
	"""Generic function to convert data frame into a formatted list of tuples to send registers to database"""
	# Extract the names
	names = list(df.columns.values)
	# Create sequence
	df_list = []
	#Iterate over rows of data frame
	for index, row in df.iterrows():
		# Create temporary object
		temp_list = []
		#Iterate over key names and add values
		for name in names:
			temp_list.append(row[name])
		# Append object to dictionary
		df_list.append(tuple(temp_list.copy()))
	
	return df_list

	
# Iterate over dataframes and send to dbs with sqlalchemy
params = urllib.parse.quote(conn_str)
engine = sqlalchemy.create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)
for idx in range(len(files)):
	string = df_names[idx] + ".to_sql('" + file_names[idx] + "', engine, index = None, if_exists = 'append')"
	exec(string)

