# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddUnit.ui'
#
# Created: Sat Dec 07 01:48:38 2013
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_NewUnit(object):
    def setupUi(self, NewUnit):
        NewUnit.setObjectName(_fromUtf8("NewUnit"))
        NewUnit.resize(359, 226)
        NewUnit.setStyleSheet(_fromUtf8(""))
        self.tabWidget = QtGui.QTabWidget(NewUnit)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 341, 211))
        self.tabWidget.setStyleSheet(_fromUtf8("\n"
""))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.addCashier = QtGui.QWidget()
        self.addCashier.setObjectName(_fromUtf8("addCashier"))
        self.add_cashier = QtGui.QPushButton(self.addCashier)
        self.add_cashier.setGeometry(QtCore.QRect(80, 140, 81, 23))
        self.add_cashier.setStyleSheet(_fromUtf8(""))
        self.add_cashier.setObjectName(_fromUtf8("add_cashier"))
        self.cancel = QtGui.QPushButton(self.addCashier)
        self.cancel.setGeometry(QtCore.QRect(170, 140, 81, 23))
        self.cancel.setStyleSheet(_fromUtf8(""))
        self.cancel.setObjectName(_fromUtf8("cancel"))
        self.gridLayoutWidget = QtGui.QWidget(self.addCashier)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 20, 271, 91))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setVerticalSpacing(15)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.gridLayoutWidget)
        self.label.setStyleSheet(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.person_id = QtGui.QLineEdit(self.gridLayoutWidget)
        self.person_id.setStyleSheet(_fromUtf8(""))
        self.person_id.setObjectName(_fromUtf8("person_id"))
        self.gridLayout.addWidget(self.person_id, 0, 1, 1, 1)
        self.person_password = QtGui.QLineEdit(self.gridLayoutWidget)
        self.person_password.setStyleSheet(_fromUtf8(""))
        self.person_password.setInputMask(_fromUtf8(""))
        self.person_password.setEchoMode(QtGui.QLineEdit.Password)
        self.person_password.setObjectName(_fromUtf8("person_password"))
        self.gridLayout.addWidget(self.person_password, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_2.setStyleSheet(_fromUtf8(""))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.error_Id = QtGui.QLabel(self.gridLayoutWidget)
        self.error_Id.setText(_fromUtf8(""))
        self.error_Id.setObjectName(_fromUtf8("error_Id"))
        self.gridLayout.addWidget(self.error_Id, 0, 2, 1, 1)
        self.error_Pwd = QtGui.QLabel(self.gridLayoutWidget)
        self.error_Pwd.setText(_fromUtf8(""))
        self.error_Pwd.setObjectName(_fromUtf8("error_Pwd"))
        self.gridLayout.addWidget(self.error_Pwd, 1, 2, 1, 1)
        self.gridLayout.setColumnStretch(0, 50)
        self.gridLayout.setColumnStretch(1, 100)
        self.gridLayout.setColumnStretch(2, 50)
        self.tabWidget.addTab(self.addCashier, _fromUtf8(""))
        self.addPdu = QtGui.QWidget()
        self.addPdu.setObjectName(_fromUtf8("addPdu"))
        self.add_pdu = QtGui.QPushButton(self.addPdu)
        self.add_pdu.setGeometry(QtCore.QRect(80, 140, 81, 23))
        self.add_pdu.setStyleSheet(_fromUtf8(""))
        self.add_pdu.setObjectName(_fromUtf8("add_pdu"))
        self.pdu_cancel = QtGui.QPushButton(self.addPdu)
        self.pdu_cancel.setGeometry(QtCore.QRect(170, 140, 81, 23))
        self.pdu_cancel.setStyleSheet(_fromUtf8(""))
        self.pdu_cancel.setObjectName(_fromUtf8("pdu_cancel"))
        self.gridLayoutWidget_2 = QtGui.QWidget(self.addPdu)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(30, 20, 271, 91))
        self.gridLayoutWidget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setHorizontalSpacing(20)
        self.gridLayout_2.setVerticalSpacing(15)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_5 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_5.setStyleSheet(_fromUtf8(""))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)
        self.error_Dev = QtGui.QLabel(self.gridLayoutWidget_2)
        self.error_Dev.setText(_fromUtf8(""))
        self.error_Dev.setObjectName(_fromUtf8("error_Dev"))
        self.gridLayout_2.addWidget(self.error_Dev, 0, 2, 1, 1)
        self.label_6 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_6.setStyleSheet(_fromUtf8(""))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_2.addWidget(self.label_6, 1, 0, 1, 1)
        self.error_Bar = QtGui.QLabel(self.gridLayoutWidget_2)
        self.error_Bar.setText(_fromUtf8(""))
        self.error_Bar.setObjectName(_fromUtf8("error_Bar"))
        self.gridLayout_2.addWidget(self.error_Bar, 1, 2, 1, 1)
        self.device_barcode = QtGui.QLineEdit(self.gridLayoutWidget_2)
        self.device_barcode.setStyleSheet(_fromUtf8(""))
        self.device_barcode.setObjectName(_fromUtf8("device_barcode"))
        self.gridLayout_2.addWidget(self.device_barcode, 1, 1, 1, 1)
        self.device_id = QtGui.QLineEdit(self.gridLayoutWidget_2)
        self.device_id.setStyleSheet(_fromUtf8(""))
        self.device_id.setObjectName(_fromUtf8("device_id"))
        self.gridLayout_2.addWidget(self.device_id, 0, 1, 1, 1)
        self.gridLayout_2.setColumnStretch(0, 50)
        self.gridLayout_2.setColumnStretch(1, 100)
        self.gridLayout_2.setColumnStretch(2, 50)
        self.tabWidget.addTab(self.addPdu, _fromUtf8(""))

        self.retranslateUi(NewUnit)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.cancel, QtCore.SIGNAL(_fromUtf8("clicked()")), NewUnit.close)
        QtCore.QObject.connect(self.pdu_cancel, QtCore.SIGNAL(_fromUtf8("clicked()")), NewUnit.close)
        QtCore.QMetaObject.connectSlotsByName(NewUnit)

    def retranslateUi(self, NewUnit):
        NewUnit.setWindowTitle(_translate("NewUnit", "Add new unit", None))
        self.add_cashier.setText(_translate("NewUnit", "Add Cashier", None))
        self.cancel.setText(_translate("NewUnit", "Cancel", None))
        self.label.setText(_translate("NewUnit", "Person ID", None))
        self.label_2.setText(_translate("NewUnit", "Password", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.addCashier), _translate("NewUnit", "Add Cashier", None))
        self.add_pdu.setText(_translate("NewUnit", "Add PDU", None))
        self.pdu_cancel.setText(_translate("NewUnit", "Cancel", None))
        self.label_5.setText(_translate("NewUnit", "Device ID", None))
        self.label_6.setText(_translate("NewUnit", "Barcode", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.addPdu), _translate("NewUnit", "Add Price Display Unit", None))

