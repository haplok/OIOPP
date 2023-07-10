import sqlite3
from collections import Counter
from datetime import date

database = 'caseHistory.db'
tableMain = 'tableCaseHistory'
tableTrashBin = 'tableTrashBin'

def exportToDatabase(dict_data, table = tableMain):
	conn = sqlite3.connect(database)
	
	
	cursor = conn.cursor()

	try:
		sql = f"CREATE TABLE {table} (id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE)"
		cursor.execute(sql)
		
	except:
		pass
	
	attrib_names = ", ".join(dict_data.keys())
	attrib_values = ", ".join("?"*len(dict_data.keys()))

	try:
		for column_name in dict_data.keys():
			if column_name == 'lineEdit_HistoryNumber' \
				or column_name == 'lineEdit_YearOfHistory':
				sql = f"ALTER TABLE {table} ADD COLUMN {column_name} INTEGER" 
				cursor.execute(sql)
			elif column_name == 'id':
				pass
			else:
				sql = f"ALTER TABLE {table} ADD COLUMN {column_name} TEXT"
				cursor.execute(sql)
						
			
			conn.commit()
	except:
		pass
	if table == tableMain:
		try:
			sql = f"CREATE UNIQUE INDEX id_x ON {table}(lineEdit_HistoryNumber)"
			cursor.execute(sql)
		except:
			pass

	try:
		sql = f"INSERT OR REPLACE INTO {table} ({attrib_names}) VALUES ({attrib_values}) "
		cursor.execute(sql, list(dict_data.values()))
	except:
		pass


	conn.commit()

def createTrashBin (dict_data):
	exportToDatabase (dict_data, tableTrashBin)
def deleteHistory (historyNumber, yearOfHistory):
	conn = sqlite3.connect(database)
	
	cursor = conn.cursor()
	try:
		sql = f"""DELETE FROM {tableMain} 
				  WHERE lineEdit_HistoryNumber == {historyNumber} AND
						lineEdit_YearOfHistory == {yearOfHistory}

		"""
		cursor.execute(sql)
		
	except:
		pass
	conn.commit()


def dict_factory(cursor, row):

	d = {}
	for idx, col in enumerate(cursor.description):
		d[col[0]] = row[idx]
	return d

def importDict(historyNumber, yearOfHistory, repeatHis = 0, table = tableMain):
	conn = sqlite3.connect(database)
	conn.row_factory = dict_factory
	cursor = conn.cursor()
	sql = f"""SELECT * FROM {table} 
		WHERE lineEdit_HistoryNumber == {historyNumber} AND
		lineEdit_YearOfHistory == {yearOfHistory} """

		
	cursor.execute(sql)
	d = cursor.fetchone()
	# if d == None:
	# 	d = {'lineEdit_HistoryNumber': historyNumber,
	# 		 'lineEdit_YearOfHistory': yearOfHistory}
	# print (type(d))
	if repeatHis == 1:
		# d['lineEdit_HistoryNumber'] = 
		# d['lineEdit_YearOfHistory']	= 
		d['comboBox_MoveFromOrganization'] = ''
		d['lineEdit_MoveFromDepartment'] = ''
		d['lineEdit_MoveFromDoctor'] = ''
		d['dateTimeEdit_MoveFromDateTime'] = '2000-01-01T09:25:00'	
		d['comboBox_CurrentDoctor'] = ''
		d['lineEdit_DaysInOIOPP'] = ''
		d['comboBox_MoveToOrganization'] = ''
		d['lineEdit_MoveToDepatment'] = ''
		d['lineEdit_MoveToDoctor'] = ''
		d['dateEdit_MoveToDate'] = '2000-01-01T00:00:00'
	else:
		pass
	return d


	
def importShortListOfHistory(table = tableMain):
	conn = sqlite3.connect(database)
	
	sql = f"""SELECT lineEdit_HistoryNumber,
					 lineEdit_YearOfHistory, 
					 lineEdit_PatientLastName, 
					 lineEdit_PatientFirstName,
					 lineEdit_PatientPatronymic,
					 dateTimeEdit_MoveFromDateTime, 
					 dateEdit_MoveToDate 
			FROM {table} ORDER BY lineEdit_YearOfHistory DESC,
								  lineEdit_HistoryNumber DESC;"""

	currentColumn = []
	try:
		cursor = conn.cursor()

		with conn:
			cursor.execute(sql)    
			column = cursor.fetchall()

			for i in column:
				currentColumn.append (i)
		
		
		conn.commit()
	except:
		currentColumn = None
	return currentColumn 

def importSummaryIn (currentDateISO, table = tableMain):
	conn = sqlite3.connect(database)
	currentDateISO = currentDateISO[:10] 
	
	sql = f"""SELECT lineEdit_HistoryNumber,
					 lineEdit_YearOfHistory
				FROM {table} 
				WHERE dateTimeEdit_MoveFromDateTime 
				LIKE '{currentDateISO}%' 
				ORDER by lineEdit_HistoryNumber

	""" 
	currentColumn = []
	try:
		cursor = conn.cursor()

		with conn:
			cursor.execute(sql)    
			column = cursor.fetchall()

			for i in column:
				currentColumn.append (i)
		
		
		conn.commit()
	except:
		currentColumn = None
	return currentColumn 

def inOutAllPatients (table = tableMain):
	conn = sqlite3.connect(database)
	

	sql = f"""SELECT dateTimeEdit_MoveFromDateTime, dateEdit_MoveToDate
			  FROM {table}
			  ORDER by lineEdit_HistoryNumber
	"""
	currentColumn = []
	try:
		cursor = conn.cursor()

		with conn:
			cursor.execute(sql)    
			column = cursor.fetchall()

			for i in column:
				currentColumn.append (i)
		
		
		conn.commit()
	except:
		currentColumn = None
	return currentColumn



def importStatisticByMonthIn (currentDateISO, table = tableMain):
	conn = sqlite3.connect(database)
	currentMonthISO = currentDateISO[:7]

	sql = f"""SELECT dateTimeEdit_MoveFromDateTime									
							
			  FROM {table}
			  WHERE dateTimeEdit_MoveFromDateTime
			  LIKE '{currentMonthISO}%'
			  ORDER by dateTimeEdit_MoveFromDateTime

	"""
	currentColumn = []
	try:
		cursor = conn.cursor()

		with conn:
			cursor.execute(sql)    
			column = cursor.fetchall()

			for i in column:
				currentColumn.append (i)
		
		
		conn.commit()
		conn.close()
	
		shortColumn = []
		for i in range(len(currentColumn)):
			# currentColumn[i][0] = currentColumn[i][0][0:10]
			shortColumn.append(currentColumn[i][0][:10])
			countByDay = Counter(shortColumn)
	except:
		countByDay = None
	return countByDay 

def importStatisticByMonthOut (currentDateISO, table = tableMain):
	conn = sqlite3.connect(database)
	currentMonthISO = currentDateISO[:7]

	sql = f"""SELECT dateEdit_MoveToDate									
							
			  FROM {table}
			  WHERE dateEdit_MoveToDate
			  LIKE '{currentMonthISO}%'
			  ORDER by dateEdit_MoveToDate

	"""
	currentColumn = []
	try:
		cursor = conn.cursor()

		with conn:
			cursor.execute(sql)    
			column = cursor.fetchall()

			for i in column:
				currentColumn.append (i)
		
		
		conn.commit()
		conn.close()
	
		shortColumn = []
		for i in range(len(currentColumn)):
			# currentColumn[i][0] = currentColumn[i][0][0:10]
			shortColumn.append(currentColumn[i][0][:10])
			countByDay = Counter(shortColumn)
	except:
		countByDay = None
	return countByDay 


def importSummaryOut (currentDateISO, table = tableMain):
	conn = sqlite3.connect(database)
	currentDateISO = currentDateISO[:10] 
	
	sql = f"""SELECT lineEdit_HistoryNumber,
					 lineEdit_YearOfHistory
				FROM {table} 
				WHERE dateEdit_MoveToDate 
				LIKE '{currentDateISO}%' 
				ORDER by lineEdit_HistoryNumber

	""" 
	currentColumn = []
	try:
		cursor = conn.cursor()

		with conn:
			cursor.execute(sql)    
			column = cursor.fetchall()

			for i in column:
				currentColumn.append (i)
		
		
		conn.commit()
	except:
		currentColumn = None
	return currentColumn 

def importPPB (daysInvolvement, key, table = tableMain):
	conn = sqlite3.connect(database)
	subQuerie = ''
	if key == 1:
		field = 'dateTimeEdit_MoveFromDateTime'
	if key == 2:
		field = 'dateEdit_MoveToDate'
	for i in range (len(daysInvolvement)):
		shortDate = daysInvolvement[i].date().isoformat()
		if i == 0:
			subQuerie += f"{field} LIKE '{shortDate}%'"
		else:	
			subQuerie += f" OR {field} LIKE '{shortDate}%'"		
	
		
	sql =f"""SELECT lineEdit_HistoryNumber,
					lineEdit_YearOfHistory, 
					lineEdit_PatientLastName, 
					lineEdit_PatientFirstName,
					lineEdit_PatientPatronymic,
					dateTimeEdit_MoveFromDateTime, 
					dateEdit_MoveToDate,
					dateEdit_PatientBirthDate,
					lineEdit_MainDiagnosisAnotherDepartment,
					checkBox_ReabilitationEPI,
					checkBox_ReabilitationFamily,
					checkBox_ReabilitationIndividual,
					checkBox_ReabilitationPhychoStudy,
					checkBox_ReabilitationMotivation,
					checkBox_ReabilitationTBN,
					radioButton_GroupM1,
					radioButton_GroupM2,
					radioButton_GroupM3,
					radioButton_GroupM4,
					radioButton_GroupImmobile,
					comboBox_MoveToOrganization
			  FROM {table}
			  WHERE {subQuerie}
			  ORDER by lineEdit_HistoryNumber

	"""
	currentColumn = []
	try:
		cursor = conn.cursor()

		with conn:
			cursor.execute(sql)    
			column = cursor.fetchall()

			for i in column:
				currentColumn.append (i)
		
		
		conn.commit()
	except:
		currentColumn = None
	
	return currentColumn 

def nextNumberOfCaseHistory(table = tableMain):
	conn = sqlite3.connect(database)
	sql = f"""SELECT max(lineEdit_HistoryNumber) 
			  FROM {table} 
			  WHERE lineEdit_HistoryNumber != '' AND 
			         lineEdit_YearOfHistory = (
			         	SELECT max(lineEdit_YearOfHistory)
			        	FROM {table}
			        	)"""
	
	try:
		cursor = conn.cursor()
		with conn:
			cursor.execute(sql)
			nextNumber = int(cursor.fetchone()[0]) + 1 
	except:
		nextNumber = 1
	
	conn.commit()
	
	return nextNumber

def setDaysInOIOPP(days, table = tableMain):
	conn = sqlite3.connect(database)

	try:
		sql = f"INSERT OR REPLACE INTO {table} (lineEdit_DaysInOIOPP) VALUES ({days})"
		cursor.execute(sql)
	except:
		pass


	conn.commit()



