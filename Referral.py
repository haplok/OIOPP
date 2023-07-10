from openpyxl import Workbook, load_workbook
import os
from datetime import datetime
import MyFunctions as functions



def createReferral (dictToFill):

	mainPath = os.getcwd()

	dateIn = datetime.fromisoformat(dictToFill['dateTimeEdit_MoveFromDateTime'])
	dateOut = datetime.fromisoformat(dictToFill['dateEdit_MoveToDate'])
	if dateOut < dateIn:
		return
	
	 
	loadWB = load_workbook('Referral.xlsx')
	wSheet = loadWB.active

	moveToOrganizationCell = wSheet ['C6']
	moveToDepartmentCell = wSheet ['C7']
	moveToDoctorCell = wSheet ['C8']
	patientLastNameCell = wSheet ['C9']
	patientFirstNameCell = wSheet ['C10']
	patientPatronymicCell = wSheet ['C11']
	patientBirthDateCell = wSheet ['C12']
	patientAdressCell = wSheet ['C13']
	patientTelephoneCell = wSheet ['C14']
	inOurDepartmentFromCell = wSheet ['E17']
	inOurDepartmentToCell = wSheet ['H17']
	diagnosisCell = wSheet ['C18']
	FIOCell = wSheet ['E25']
	dateOfGivingCell = wSheet ['E26']
	doctorCell = wSheet ['C28']

	moveToOrganizationCell.value = '   ' + str (dictToFill['comboBox_MoveToOrganization'])
	moveToDepartmentCell.value = str (dictToFill['lineEdit_MoveToDepatment'])
	moveToDoctorCell.value = str (dictToFill['lineEdit_MoveToDoctor'])
	patientLastNameCell.value = str (dictToFill['lineEdit_PatientLastName'])
	patientFirstNameCell.value = str (dictToFill['lineEdit_PatientFirstName'])
	patientPatronymicCell.value = str (dictToFill['lineEdit_PatientPatronymic'])
	birthDate = functions.editingDateTime(dictToFill['dateEdit_PatientBirthDate'])[0]
	age = functions.calculationAge(dictToFill['dateEdit_PatientBirthDate'])
	patientBirthDateCell.value = f'{birthDate} ({age})'
	if dictToFill['lineEdit_HomeReg'] != '':
		key = 'reg'
	else:
		key = 'main'
	adress = functions.combineAdress(dictToFill, key)
	patientAdressCell.value = adress
	telephone = functions.combineAllTelephone(dictToFill)
	patientTelephoneCell.value = telephone
	fromDate = functions.editingDateTime(dictToFill['dateTimeEdit_MoveFromDateTime'])[0]
	inOurDepartmentFromCell.value = fromDate

	toDate = functions.editingDateTime(dictToFill['dateEdit_MoveToDate'])[0]
	inOurDepartmentToCell.value = toDate
	diagnosisCell.value = str(dictToFill['lineEdit_FinalDiagnosis'])
	FIOCell.value = createFIO (dictToFill)
	dateOfGivingCell.value = toDate
	doctorCell.value = dictToFill['comboBox_CurrentDoctor']




	caseNumber = str(dictToFill['lineEdit_HistoryNumber']).rjust(3,'0')
	fullLastName = str(dictToFill['lineEdit_PatientLastName'])[:1].upper() + str(dictToFill['lineEdit_PatientLastName'])[1:]
	shortFirstName = str(dictToFill['lineEdit_PatientFirstName'])[:1].upper()
	shortPatronymic = str(dictToFill['lineEdit_PatientPatronymic'])[:1].upper()
	nameToSave = f'Ref_{caseNumber}_{fullLastName}{shortFirstName}{shortPatronymic}'
	# print (nameToSave)
	yearOfHistory = str(dictToFill['lineEdit_YearOfHistory'])
	path = f'documents/20{yearOfHistory}/referrals/'
	try:
		os.makedirs(path)
	except:
		pass

	loadWB.save(f'{path}{nameToSave}.xlsx')
	os.chdir(path)
	os.startfile(f'{nameToSave}.xlsx')
	os.chdir(mainPath)

	

def createFIO(dictToFill):

	fullLastName = dictToFill['lineEdit_PatientLastName']
	fullFirstName = dictToFill['lineEdit_PatientFirstName']
	fullPatronymic = dictToFill['lineEdit_PatientPatronymic']
	correctLastName = f'{fullLastName[:1].upper()}{fullLastName[1:]} '
	shortFirstName = fullFirstName[:1].upper()
	shortPatronymic = fullPatronymic[:1].upper()

	string = f"{correctLastName}{shortFirstName}.{shortPatronymic}."
		
	return string





# _cell.value = 1231255123

