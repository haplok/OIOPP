from datetime import datetime
from datetime import timedelta
from datetime import date





def calculationAge(birthDateISO):
	birthDate = datetime.fromisoformat(birthDateISO)
	today = datetime.today()
	age = today.year - birthDate.year - (
		(today.month, today.day) < 
		(birthDate.month, birthDate.day)) 
  
	return age 



def combineAdress(dic, key):
	if key == 'main':
		city = dic['lineEdit_CityMain'] 
		typeOfRoad = dic['comboBox_TypeOfRoadMain']
		road = dic['lineEdit_RoadMain'] 
		home = dic['lineEdit_HomeMain']
		building = dic['lineEdit_BuildingMain'] 
		apartment = dic['lineEdit_ApartmentNumberMain']
	elif key == 'reg':
		city = dic['lineEdit_CityReg']
		typeOfRoad = dic['comboBox_TypeOfRoadReg']
		road = dic['lineEdit_RoadReg']
		home = dic['lineEdit_HomeReg']
		building = dic['lineEdit_BuildingReg']
		apartment = dic['lineEdit_ApartmentNumberReg']
	buil = ''
	if building != '':
		buil = ', корпус/строение '


	adress = f"{city}, {typeOfRoad} {road}, дом {home}{buil}{building}, квартира {apartment}"
	return adress



def passportSnilsOmsGen(passport, snils, oms):

	if passport == '':
		passport = '\t\t\t'
	if snils == '':
		snils = '\t\t\t'
	if oms == '':
		oms = '\t\t\t'

	pso = (passport, snils, oms)
	return (pso) 

def editingDateTime (isoDate):

	dt = datetime.fromisoformat(isoDate)

	month = rusMonth(dt.month)

	hour = str(dt.hour).rjust(2,'0')
	minute = str(dt.minute).rjust(2,'0')

	editedDate = f'{dt.day} {month} {dt.year}г.'
	editedTime = f'{hour}:{minute}'

	editedDateTime = (editedDate, editedTime)
	# print (editedDateTime)
	return editedDateTime

def editDate (dateObj):
	dt = dateObj
	month = rusMonth(dt.month)

	hour = str(dt.hour).rjust(2,'0')
	minute = str(dt.minute).rjust(2,'0')

	editedDate = f'{dt.day} {month} {dt.year}г.'
	
	return editedDate

def rusMonth (monthNumber):
	
	if monthNumber == 1:
		month = 'января'
	elif monthNumber == 2:
		month = 'февраля'
	elif monthNumber == 3:
		month = 'марта'
	elif monthNumber == 4:
		month = 'апреля'
	elif monthNumber == 5:
		month = 'мая'
	elif monthNumber == 6:
		month = 'июня'
	elif monthNumber == 7:
		month = 'июля'
	elif monthNumber == 8:
		month = 'августа'
	elif monthNumber == 9:
		month = 'сентября'
	elif monthNumber == 10:
		month = 'октября'
	elif monthNumber == 11:
		month = 'ноября'
	elif monthNumber == 12:
		month = 'декабря'

	return month

def rusMonthIm (monthNumber):
	
	if monthNumber == 1:
		month = 'январь'
	elif monthNumber == 2:
		month = 'февраль'
	elif monthNumber == 3:
		month = 'март'
	elif monthNumber == 4:
		month = 'апрель'
	elif monthNumber == 5:
		month = 'май'
	elif monthNumber == 6:
		month = 'июнь'
	elif monthNumber == 7:
		month = 'июль'
	elif monthNumber == 8:
		month = 'август'
	elif monthNumber == 9:
		month = 'сентябрь'
	elif monthNumber == 10:
		month = 'октябрь'
	elif monthNumber == 11:
		month = 'ноябрь'
	elif monthNumber == 12:
		month = 'декабрь'

	return month

def dateOfBothPPB(dictionaryToFill):
	inISO = str(dictionaryToFill['dateTimeEdit_MoveFromDateTime'])
	outISO = str(dictionaryToFill['dateEdit_MoveToDate'])
	dtPPBIn = None
	dtPPBOut = None

	dtIn = datetime.fromisoformat(inISO)
	dtOut = datetime.fromisoformat(outISO)
	dtPPBIn = editDayPPB(dtIn)
	dtPPBOut = editDayPPB(dtOut)

	return (dtPPBIn, dtPPBOut)

def editDayPPB (day):

	if day.weekday() == 0:
		corrDay = day + timedelta(days=1)
	elif day.weekday() == 1:
		corrDay = day
	elif day.weekday() == 2:
		corrDay = day	+ timedelta(days=2)
	elif day.weekday() == 3:
		corrDay = day	+ timedelta(days=1)
	elif day.weekday() == 4:
		corrDay = day	
	elif day.weekday() == 5:
		corrDay = day 	+ timedelta(days=3)
	elif day.weekday() == 6:
		corrDay = day 	+ timedelta(days=2)


	return (corrDay)

def setOfDaysPPB (dayISO):
	listOfDaysPPB = []
	day = datetime.fromisoformat(dayISO)
	editDay = editDayPPB (day)
	if editDay.weekday() == 1:
		
		listOfDaysPPB = (editDay - timedelta(days=3),
						 editDay - timedelta(days=2),
						 editDay - timedelta(days=1),
						 editDay)
	elif editDay.weekday() == 4:
		listOfDaysPPB = (editDay - timedelta(days=2),
						 editDay - timedelta(days=1),
						 editDay)  


	return listOfDaysPPB


def radioButtonCheck(dic):
	corrDict = {}
	corrDict.update({'B_BallotBox':'\u2610'})
	for element in dic:
		if element.split('_')[0] == 'checkBox' or element.split('_')[0] == 'radioButton':
			# editElement = 'RC_'+ element.split('_')[1]
			morphCheck = setChecked(dic[element])
			corrDict.update({element:morphCheck})
		else:
			pass
	
	return corrDict

def setChecked (isChecked):
	if isChecked == '1':
		return '\u2611'
	elif isChecked == '0':
		return '\u2610'

def dateFromIso (dateIso):
	date1 = datetime.fromisoformat(dateIso)
	return date1

def timeDeltaInOut (dateIn, dateOut):
	deltaDay = dateOut - dateIn 
	return deltaDay.days

def daysInOIOPP (dictionaryToFill):
	inISO = str(dictionaryToFill['dateTimeEdit_MoveFromDateTime'])
	outISO = str(dictionaryToFill['dateEdit_MoveToDate'])


	dtIn = datetime.fromisoformat(inISO)
	dtOut = datetime.fromisoformat(outISO)

	dt = dtOut-dtIn
	if dt.days > 0:
		return (dt.days + 2)
	else:
		return ''

def combineAllTelephone (dictionaryToFill):
	telHome = dictionaryToFill['lineEdit_HomeTelephoneNumberMain']
	telMob = '  ' + dictionaryToFill['lineEdit_MobilePhoneNumberMain']
	proxy = ' ' + dictionaryToFill['comboBox_ProxyType']
	proxyLastName = '  ' + dictionaryToFill['lineEdit_ProxyLastName']
	proxyFirstName = ' ' + dictionaryToFill['lineEdit_ProxyFirstName']
	proxyPatronynic = ' ' + dictionaryToFill['lineEdit_ProxyPatronymic']
	proxyTel1 = '  ' + dictionaryToFill['lineEdit_ProxyTelephoneNumber1']
	proxyTel2 = '  ' + dictionaryToFill['lineEdit_ProxyTelephoneNumber2']
	proxyTel3 = '  ' + dictionaryToFill['lineEdit_ProxyTelephoneNumber3']
	comboTelephone = f'{telHome}{telMob}{proxy}{proxyLastName}\
{proxyFirstName}{proxyPatronynic}{proxyTel1}{proxyTel2}{proxyTel3}'

	return comboTelephone

def getCurrentYear ():
	currYear = datetime.today().year
	return str(currYear)[2:]



