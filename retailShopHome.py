import sys
import connectDb
import getInfo
import getLists
import retrieveRegional
import subprocess
import os
import getpass
import hashlib
from PyQt4 import QtGui, QtCore
from MainWindow import Ui_MainWindow


def isNumber(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initialiseAllViews()

        #widgetPressed = self.ui.tabWidget.currentIndex()
        self.ui.viewall_products.clicked.connect(self.viewProducts)
        self.ui.searchbarcode_products.clicked.connect(self.viewProducts)
        self.ui.searchname_products.clicked.connect(self.viewProducts)

        self.ui.viewall_perishable.clicked.connect(self.viewPerishables)
        self.ui.searchbarcode_perishable.clicked.connect(self.viewPerishables)
        self.ui.searchname_perishable.clicked.connect(self.viewPerishables)

        self.ui.viewall_tran.clicked.connect(self.viewTran)
        self.ui.searchid_tran.clicked.connect(self.viewTran)
        self.ui.searchdate_tran.clicked.connect(self.viewTran)

        self.ui.viewall_units.clicked.connect(self.viewUnits)
        self.ui.searchbarcode_units.clicked.connect(self.viewUnits)
        self.ui.searchdev_units.clicked.connect(self.viewUnits)

        self.ui.viewall_promo.clicked.connect(self.viewPromo)
        self.ui.searchbarcode_promo.clicked.connect(self.viewPromo)
        self.ui.searchname_promo.clicked.connect(self.viewPromo)
        self.ui.searchpromo_promo.clicked.connect(self.viewPromo)

        self.ui.orderproducts.clicked.connect(self.orderProducts)
        self.ui.updatestock.clicked.connect(self.updateStockAndProduct)

    def initialiseAllViews(self):
        self.viewProducts()
        self.viewPerishables()
        self.viewTran()
        self.viewUnits()
        self.viewPromo()

    def viewProducts(self):
        self.ui.statusBar.showMessage("Loading Data, please wait...")
        flag = 1
        sender = self.sender()
        if sender is not None:
            senderEvent = sender.text()
            if senderEvent == "View All":
                self.ui.lineEdit_1_products.clear()
                self.ui.lineEdit_2_products.clear()
                count, rowProduct = getLists.getProductList(0)
            elif (senderEvent == "Barcode") & isNumber(self.ui.lineEdit_1_products.text()):
                self.ui.lineEdit_2_products.clear()
                barcodeSearch = int(self.ui.lineEdit_1_products.text())
                count, rowProduct = getLists.getProductList(1, barcodeSearch)
            elif senderEvent == "Name":
                self.ui.lineEdit_1_products.clear()
                nameSearch = str(self.ui.lineEdit_2_products.text())
                count, rowProduct = getLists.getProductList(2, nameSearch)
            else:
                self.ui.lineEdit_1_products.clear()
                self.ui.lineEdit_2_products.clear()
                self.ui.statusBar.clearMessage()
                flag = 0
        else:
            count, rowProduct = getLists.getProductList(0)
        if flag:
            self.arrayToTable(rowProduct, self.ui.tableWidget_products, count, count, 6)

    def viewPerishables(self):
        flag = 1
        self.ui.statusBar.showMessage("Loading Data, please wait...")
        sender = self.sender()
        if sender is not None:
            senderEvent = sender.text()
            if senderEvent == "View All":
                self.ui.lineEdit_1_perishable.clear()
                self.ui.lineEdit_2_perishable.clear()
                count, rowProduct = getLists.getPerishableList(0)
            elif (senderEvent == "Barcode") & isNumber(self.ui.lineEdit_1_perishable.text()):
                self.ui.lineEdit_2_perishable.clear()
                barcodeSearch = int(self.ui.lineEdit_1_perishable.text())
                count, rowProduct = getLists.getPerishableList(1, barcodeSearch)
            elif senderEvent == "Name":
                self.ui.lineEdit_1_perishable.clear()
                nameSearch = str(self.ui.lineEdit_2_perishable.text())
                count, rowProduct = getLists.getPerishableList(2, nameSearch)
            else:
                self.ui.lineEdit_1_perishable.clear()
                self.ui.lineEdit_2_perishable.clear()
                self.ui.statusBar.clearMessage()
                flag = 0
        else:
            count, rowProduct = getLists.getPerishableList(0)
        if flag:
            self.arrayToTable(rowProduct, self.ui.tableWidget_perishable, count, count, 6)

    def viewTran(self):
        self.ui.statusBar.showMessage("Loading Data, please wait...")
        sender = self.sender()
        if sender is not None:
            senderEvent = sender.text()
            if senderEvent == "View All":
                self.ui.lineEdit_1_tran.clear()
                self.ui.lineEdit_2_tran.clear()
                count, rowTran = getLists.getTranList(0)
                self.arrayToTable(rowTran, self.ui.tableWidget_tran, count, count, 4)
            elif (senderEvent == "Transaction ID") & isNumber(self.ui.lineEdit_1_tran.text()):
                self.ui.lineEdit_2_tran.clear()
                idSearch = int(self.ui.lineEdit_1_tran.text())
                count, rowTran = getLists.getTranList(1, idSearch)
                self.arrayToTable(rowTran, self.ui.tableWidget_tran, count, count, 5)
            elif senderEvent == "Date":
                self.ui.lineEdit_1_tran.clear()
                dateSearch = str(self.ui.lineEdit_2_tran.text())
                year = dateSearch[:4]
                month = dateSearch[5:7]
                day = dateSearch[8:]
                if isNumber(year) & isNumber(month) & isNumber(day):
                    dateInput = QtCore.QDate(int(year), int(month), int(day))
                    if dateInput:
                        count, rowTran = getLists.getTranList(2, dateSearch)
                        self.arrayToTable(rowTran, self.ui.tableWidget_tran, count, count, 4)
                    else:
                        self.ui.lineEdit_1_tran.clear()
                        self.ui.lineEdit_2_tran.clear()
                        self.ui.statusBar.clearMessage()
                else:
                    self.ui.lineEdit_1_tran.clear()
                    self.ui.lineEdit_2_tran.clear()
                    self.ui.statusBar.clearMessage()                
            else:
                self.ui.lineEdit_1_tran.clear()
                self.ui.lineEdit_2_tran.clear()
                self.ui.statusBar.clearMessage()
        else:
            count, rowTran = getLists.getTranList(0)
            self.arrayToTable(rowTran, self.ui.tableWidget_tran, count, count, 4)

    def viewUnits(self):
        flag = 1
        self.ui.statusBar.showMessage("Loading Data, please wait...")
        sender = self.sender()
        if sender is not None:
            senderEvent = sender.text()
            if senderEvent == "View All":
                self.ui.lineEdit_1_units.clear()
                self.ui.lineEdit_2_units.clear()
                countCashier, rowCashier = getLists.getCashierList(0)
                countPdu, rowPDUs = getLists.getPDUList(0)
            elif (senderEvent == "Barcode") & isNumber(self.ui.lineEdit_1_units.text()):
                self.ui.lineEdit_2_units.clear()
                barcodeSearch = int(self.ui.lineEdit_1_units.text())
                countCashier, rowCashier = getLists.getCashierList(0)
                countPdu, rowPDUs = getLists.getPDUList(1, barcodeSearch)
            elif (senderEvent == "Device ID") & isNumber(self.ui.lineEdit_2_units.text()):
                self.ui.lineEdit_1_units.clear()
                nameSearch = int(self.ui.lineEdit_2_units.text())
                countCashier, rowCashier = getLists.getCashierList(2, nameSearch)
                countPdu, rowPDUs = getLists.getPDUList(2, nameSearch)
            else:
                self.ui.lineEdit_1_units.clear()
                self.ui.lineEdit_2_units.clear()
                self.ui.statusBar.clearMessage()
                flag = 0
        else:
            countCashier, rowCashier = getLists.getCashierList(0)
            countPdu, rowPDUs = getLists.getPDUList(0)
        if flag:
            self.arrayToTable(rowCashier, self.ui.tableWidget_cashier, countCashier, countCashier, 1)
            self.arrayToTable(rowPDUs, self.ui.tableWidget_pdu, countPdu, countPdu, 2)

    def viewPromo(self):
        flag = 1
        self.ui.statusBar.showMessage("Loading Data, please wait...")
        sender = self.sender()
        if sender is not None:
            senderEvent = sender.text()
            if senderEvent == "View All":
                self.ui.lineEdit_1_promo.clear()
                self.ui.lineEdit_2_promo.clear()
                self.ui.lineEdit_3_promo.clear()
                count, rowPromo = getLists.getPromoList(0)
            elif (senderEvent == "Barcode") & isNumber(self.ui.lineEdit_1_promo.text()):
                self.ui.lineEdit_2_promo.clear()
                self.ui.lineEdit_3_promo.clear()
                barcodeSearch = int(self.ui.lineEdit_1_promo.text())
                count, rowPromo = getLists.getPromoList(1, barcodeSearch)
            elif (senderEvent == "Promo ID") & isNumber(self.ui.lineEdit_2_promo.text()):
                self.ui.lineEdit_1_promo.clear()
                self.ui.lineEdit_3_promo.clear()
                idSearch = int(self.ui.lineEdit_2_promo.text())
                count, rowPromo = getLists.getPromoList(2, idSearch)
            elif senderEvent == "Name":
                self.ui.lineEdit_1_promo.clear()
                self.ui.lineEdit_2_promo.clear()
                nameSearch = str(self.ui.lineEdit_3_promo.text())
                count, rowPromo = getLists.getPromoList(3, nameSearch)
            else:
                self.ui.lineEdit_1_promo.clear()
                self.ui.lineEdit_2_promo.clear()
                self.ui.lineEdit_3_promo.clear()
                self.ui.statusBar.clearMessage()
                flag = 0
        else:
            count, rowPromo = getLists.getPromoList(0)
        if flag:
            self.arrayToTable(rowPromo, self.ui.tableWidget_promo, count, count, 6)


    def updateStockAndProduct(self):
        self.ui.statusBar.showMessage("Checking for Data, please wait...")
    	data = retrieveRegional.downloadFileFromRegional(1, hashlib.md5("helloworld".encode()))
        self.ui.statusBar.clearMessage()
    	if data is None:
    		self.ui.statusBar.showMessage("Failed to download. Check internet connection", 5000)
    	else:
    		retrieveRegional.processJSON(data)
    		self.ui.statusBar.showMessage("Product List was successfully updated and re-stocked", 5000)

    def orderProducts(self):
        self.ui.statusBar.showMessage("Sending Data, please wait...")
    	proc = subprocess.Popen("php senddata.php", shell=True, stdout=subprocess.PIPE)
    	script_response = proc.stdout.read()
        self.ui.statusBar.clearMessage()
    	if "Sent!" in script_response:
            self.ui.statusBar.showMessage("Orders Sent!", 5000)
    	else:
    		self.ui.statusBar.showMessage("Sending Failed. Check internet connection", 5000)

    def arrayToTable(self, array, qtable, noOfRows, noOfRowsOnce, noOfColumns):
        qtable.setColumnCount(noOfColumns)
        qtable.setRowCount(noOfRowsOnce)
        for row in range(noOfRowsOnce):
            for column in range(noOfColumns):
                if array[row][column] is not None:
                    if type(array[row][column]) is long:
                        if len(str(array[row][column])) == 8: #if it is barcode, not to express in E notation
                            cellContent = array[row][column]
                        else:    
                            cellContent = float(array[row][column])
                    else:
                        cellContent = str(array[row][column])
                    qtable.setItem(row, column, QtGui.QTableWidgetItem(QtCore.QString("%1").arg(cellContent)))
                else:
                    qtable.setItem(row, column, QtGui.QTableWidgetItem(QtCore.QString("NULL")))
        self.ui.statusBar.clearMessage()


app = QtGui.QApplication(sys.argv) 
frame = MainWindow() 
frame.show() 
sys.exit(app.exec_())