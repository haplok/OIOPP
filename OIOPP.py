
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QCompleter

import CaseHistory
import Password 
import Menu
import SQLQueries
import Cover
import PPB
import Summary
import MonthStatistic
import Referral
import MyFunctions as functions

import sys
# import yadisk

class MenuWindow(QtWidgets.QMainWindow, Menu.Ui_MainWindow):

    def __init__(self):
        super(MenuWindow, self).__init__()
        self.setupUi(self)

        self.historyNumber = None
        self.historyYear = None

        self.nameOfButton = []

        self.deleteWidget(self.pushButton_CaseHistory)

        listOfButton = SQLQueries.importShortListOfHistory()


        self.createButtomInLoop(listOfButton, 
            self.historySelection, self.editHistory, self.verticalLayout_3)
        
        # self.scrollArea.setVerticalScrollBar(QtWidgets.QAbstractScrollArea.QScrollBar)
        self.scrollArea.verticalScrollBar().setValue(self.scrollArea.verticalScrollBar().maximum())
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setVisible(True)

        self.lineEdit_SearchLine.textChanged.connect(self.updateDisplay)

        # self.completer = QCompleter(widget_names)
        # self.completer.setCaseSensitivity(Qt.CaseInsensitive)
        # self.lineEdit_SearchLine.setCompleter(self.completer)
       
        self.pushButton_CreateNextHistory.clicked.connect(
            self.nextCaseHistory)
        self.pushButton_EditingHistory.clicked.connect(self.editHistory)
        self.pushButton_Repeating.clicked.connect(self.repeatHistory)

        self.pushButton_Cover.clicked.connect(self.createCover)

        self.pushButton_FirstPPB.clicked.connect(self.createFirstPPB)
        self.pushButton_SecondPPB.clicked.connect(self.createSecondPPB)
        self.pushButton_Referral.clicked.connect(self.createReferral)

        self.pushButton_SummaryMoveFromTo.clicked.connect(self.createSummaryInOut)
        self.pushButton_StatisticMonth.clicked.connect(self.createMonthStatistic)
        self.pushButton_TablePPB.clicked.connect(self.createTablePPB)
        self.pushButton_DeleteHistory.clicked.connect(self.deleteHistory)

        
    def editHistory (self):
        if self.historyNumber and self.historyYear != None:
            getDict = SQLQueries.importDict(self.historyNumber, self.historyYear)
            self.CaseHistory = CaseHistoryWindow(getDict)
            self.CaseHistory.show()
            self.close()
        else:
            pass
    def repeatHistory (self):
        if self.historyNumber and self.historyYear !=None:
            getDict = SQLQueries.importDict(
                self.historyNumber, self.historyYear, 1)
            self.CaseHistory = CaseHistoryWindow(getDict,
                SQLQueries.nextNumberOfCaseHistory(),functions.getCurrentYear())
            self.CaseHistory.show()
            self.close()

    def deleteHistory (self):
        if self.historyNumber and self.historyYear != None:
            if self.checkBox_Protector.isChecked():
                print ('кнопка включена')
                getDict = SQLQueries.importDict(self.historyNumber, self.historyYear)
                SQLQueries.createTrashBin(getDict)
                SQLQueries.deleteHistory(self.historyNumber, self.historyYear)
                self.checkBox_Protector.setChecked(False)
                self.close()
       
                self.Menu = MenuWindow()
                self.Menu.show()

            else:
                print ('кнопка выключена')
        #     getDict = SQLQueries.importDict(self.historyNumber, self.historyYear)
        #     self.CaseHistory = CaseHistoryWindow(getDict)
        #     self.CaseHistory.show()
        #     self.close()
        # else:
        #     pass 

    def createCover (self):
        if self.historyNumber and self.historyYear != None:
            getDict = SQLQueries.importDict(self.historyNumber, self.historyYear)
            Cover.coverCaseHistory(getDict)
            
        else:
            pass
    def createReferral (self):
        if self.historyNumber and self.historyYear != None:
            getDict = SQLQueries.importDict(self.historyNumber, self.historyYear)
            Referral.createReferral(getDict)
            
        else:
            pass

    def createFirstPPB (self):
        if self.historyNumber and self.historyYear != None:
            getDict = SQLQueries.importDict(self.historyNumber, self.historyYear)
            PPB.pPBFirstEdition(getDict)
            
        else:
            pass

    def createSecondPPB (self):
        if self.historyNumber and self.historyYear != None:
            getDict = SQLQueries.importDict(self.historyNumber, self.historyYear)
            
            dateIn = functions.dateFromIso(getDict['dateTimeEdit_MoveFromDateTime'])
            dateOut = functions.dateFromIso(getDict['dateEdit_MoveToDate'])
            deltaDay = functions.timeDeltaInOut(dateIn, dateOut)
            print (deltaDay)

            if deltaDay < 0:
                pass
            else:
                PPB.pPBSecondEdition(getDict)
            
        else:
            pass
    def createTablePPB (self):
        calendarDate = self.calendarWidget.selectedDate()
        calendarDateISO = calendarDate.toString(QtCore.Qt.ISODate)
        daysInvolvement = functions.setOfDaysPPB(calendarDateISO)
        firstPPBList = SQLQueries.importPPB(daysInvolvement, 1)
        secondPPBList = SQLQueries.importPPB(daysInvolvement, 2)
        PPB.pPBTableEdition (daysInvolvement[-1], firstPPBList, secondPPBList)
               
        
    def nextCaseHistory (self):
        self.CaseHistory = CaseHistoryWindow(None,
            SQLQueries.nextNumberOfCaseHistory(),functions.getCurrentYear())
        self.CaseHistory.show()

        self.close()

    def createButtomInLoop(self, listOfVariables, eventOneClick, eventDoubleClick, layout):
        if listOfVariables == None:
            return
        _translate = QtCore.QCoreApplication.translate
        
        self.buttonGroup = QtWidgets.QButtonGroup(self)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.setExclusive(True)
             
        for i in range(len(listOfVariables)):
                        
            self.nameOfButton.append(QtWidgets.QPushButton(str(listOfVariables[i][0])))
            self.nameOfButton[i].setObjectName(str(self.nameOfButton)+ '_' + str(i))
            self.nameOfButton[i].setCheckable(True)
            self.nameOfButton[i].setFlat(True)
            self.nameOfButton[i].number = str(listOfVariables [i][0])
            self.nameOfButton[i].year = str(listOfVariables [i][1])
            self.nameOfButton[i].name = str(listOfVariables [i][2])
            self.nameOfButton[i].clicked.connect(eventOneClick)
            dayIn = functions.dateFromIso(listOfVariables[i][5])
            dayOut = functions.dateFromIso(listOfVariables[i][6])
                        
            if dayIn.date() <= dayOut.date():
                self.nameOfButton[i].setStyleSheet("color: grey")
            # self.nameOfButton[i].doubleClicked.connect(eventDoubleClick)

            self.buttonGroup.addButton(self.nameOfButton[i])

            
            layout.addWidget(self.nameOfButton[i])
            self.nameOfButton[i].setText(_translate(
                "MainWindow", self.createStringToPreviewHistory(listOfVariables[i])))
    
    def updateDisplay(self, text):

        for widget in self.nameOfButton:
            if text.lower() in widget.name.lower():
                widget.show()
            else:
                widget.hide()           

    def historySelection(self):
        self.historyNumber = self.sender().number
        self.historyYear = self.sender().year
        # print (f"{self.historyNumber} / {self.historyYear}")

    def createSummaryInOut(self):
        calendarDate = self.calendarWidget.selectedDate()
        calendarDateISO = calendarDate.toString(QtCore.Qt.ISODate)
        print(calendarDate.toString(QtCore.Qt.ISODate))
        summaryInNumber = SQLQueries.importSummaryIn(calendarDateISO)
        summaryOutNumber = SQLQueries.importSummaryOut(calendarDateISO)
        
        summaryInListFullDict = []
        summaryOutListFullDict = []
        for i in range(len(summaryInNumber)):
            summaryInListFullDict.append(SQLQueries.importDict(summaryInNumber[i][0], summaryInNumber[i][1]))
           
        for j in range(len(summaryOutNumber)):
            summaryOutListFullDict.append(SQLQueries.importDict(summaryOutNumber[j][0], summaryOutNumber[j][1]))
        
        Summary.createDaySummary(summaryInListFullDict,summaryOutListFullDict, calendarDateISO)

    def createMonthStatistic(self):
        calendarDate = self.calendarWidget.selectedDate()
        calendarDateISO = calendarDate.toString(QtCore.Qt.ISODate)
        countInOutByDate = (SQLQueries.importStatisticByMonthIn(calendarDateISO),
                           SQLQueries.importStatisticByMonthOut(calendarDateISO))
        listInOut = SQLQueries.inOutAllPatients()

        MonthStatistic.createMonthStatisticDocx(countInOutByDate, listInOut)


    def deleteWidget(self, objectToDelete):

        objectToDelete.setParent(None)
        objectToDelete.deleteLater()

    def createStringToPreviewHistory(self, nomFIO):
        historyNumber = f"{nomFIO[0]}/{nomFIO[1]}"
        fullLastName = f"{nomFIO[2][:1].upper()}{nomFIO[2][1:]} "
        shortFirstName = str(nomFIO[3][:1].upper())
        shortPatronymic = str(nomFIO[4][:1].upper())

        string = f"{historyNumber} \t {fullLastName}{shortFirstName}.{shortPatronymic}."
        
        return string

class CaseHistoryWindow(QtWidgets.QMainWindow, CaseHistory.Ui_MainWindow):
    def __init__(self, dictOfHistory = None, number = None, year = None):
        self.Menu = None
        super(CaseHistoryWindow, self).__init__()
        self.setupUi(self)

        self.resize (500,500)
        self.move(200,0)

        self.lineEdit_HistoryNumber.setReadOnly(True)
        self.lineEdit_YearOfHistory.setReadOnly(True)
        self.lineEdit_DaysInOIOPP.setReadOnly(True)


        self.pushButton_GoBack.clicked.connect(self.goBack)
        self.pushButton_SaveChanges.clicked.connect(self.saveChanges)

        if dictOfHistory != None:
            
            self.editingCaseHistory (dictOfHistory)

        if number != None and year != None:
            self.createNextHistory(number, year)
        
        

    def closeEvent(self, event):
        self.goBack()

    def editingCaseHistory (self, dictionaryToFillForm):
        for widget in self.centralwidget.children():
                if isinstance (widget, QtWidgets.QLineEdit):
                # print (widget.objectName() + ' ' + dictionaryToFillForm[widget.objectName()])  
                    widget.setText(str(dictionaryToFillForm[widget.objectName()]))
                elif isinstance (widget, QtWidgets.QComboBox):
                    # print (widget.objectName(), dictionaryToFillForm[widget.objectName()])
                    widget.setCurrentText(str(dictionaryToFillForm[widget.objectName()]))
                elif isinstance (widget,QtWidgets.QDateTimeEdit):
                    # print(str(dictionaryToFillForm[widget.objectName()]))
                    widget.setDateTime(QtCore.QDateTime.fromString(
                      str(dictionaryToFillForm[widget.objectName()]), QtCore.Qt.ISODate))            
                elif isinstance (widget, QtWidgets.QRadioButton):
                    widget.setChecked(int(dictionaryToFillForm[widget.objectName()]))
                elif isinstance (widget, QtWidgets.QCheckBox):
                    widget.setChecked(int(dictionaryToFillForm[widget.objectName()]))
                    
    def createNextHistory(self, number, year):
        self.lineEdit_HistoryNumber.setText(str(number))
        self.lineEdit_YearOfHistory.setText(str(year))



        
    
    def saveChanges(self):
                
        Ddic = {} 
        for widget in self.centralwidget.children():
            if isinstance(widget, (\
            QtWidgets.QLineEdit, \
            QtWidgets.QComboBox, \
            QtWidgets.QDateTimeEdit, \
            QtWidgets.QRadioButton, \
            QtWidgets.QCheckBox)):
                Ddic.update(self.fillDictionary (widget))

                        
        days = Cover.functions.daysInOIOPP(Ddic)
        Ddic.update({'lineEdit_DaysInOIOPP': days})
        
        SQLQueries.exportToDatabase(Ddic)

        

        self.goBack()
        
    

    def fillDictionary (self, objectToPaste):
        if isinstance (objectToPaste, QtWidgets.QLineEdit):
            Vvariables = {objectToPaste.objectName(): objectToPaste.text()}
        elif isinstance (objectToPaste, QtWidgets.QComboBox):
            Vvariables = {objectToPaste.objectName(): objectToPaste.currentText()}
        elif isinstance (objectToPaste, QtWidgets.QDateTimeEdit):
            Vvariables = {objectToPaste.objectName(): objectToPaste.dateTime().toString(QtCore.Qt.ISODate)} 
        elif isinstance (objectToPaste, (QtWidgets.QRadioButton,QtWidgets.QCheckBox)):
            Vvariables = {objectToPaste.objectName(): objectToPaste.isChecked()}
        # print (Vvariables)    
        return Vvariables


    def goBack(self):
        self.close()
       
        self.Menu = MenuWindow()
        self.Menu.show()

        

class PasswordWindow(QtWidgets.QMainWindow, Password.Ui_MainWindow):
    def __init__(self):

        super(PasswordWindow, self).__init__()
        self.setupUi(self)
        self.CaseHistory = None
        self.Menu = None

        self.pushButton_Enter.clicked.connect(self.checkPassword)
        self.textEdit_Changelog.setReadOnly(True)
        self.textEdit_Changelog.setText(
            f'что нового в версии 0.6.3: \
            \n1.Добавлена температура тела;\
            \n2.Изменены бланки согласий на новые. \
            ')

    def keyPressEvent(self, event):
        key = event.key()
        if key == QtCore.Qt.Key_Enter or key == QtCore.Qt.Key_Return:
            self.checkPassword()

    def checkPassword(self):
        if self.lineEdit_Password.text() == '123':
            
            self.close()
            self.Menu = MenuWindow()
            self.Menu.show()
            # myYadisk = yadisk.YaDisk(token="AgAAAAA4V89hAADLWzMSPg0cGkYSn2y4bA5MuJs")
            # myYadisk.upload('caseHistory.db', '/OIOPP Database/caseHistory.db', overwrite = True)
        else: 
            self.lineEdit_Password.setText('')
            self.lineEdit_Password.setFocus()

            

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = PasswordWindow()
    window.show()
    sys.exit(app.exec_())

    

if __name__ == "__main__":
    main()



 
        

        


