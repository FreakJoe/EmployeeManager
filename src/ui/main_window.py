# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\Python\EmployeeManager\src\ui\main_window.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(582, 484)
        MainWindow.setStyleSheet("QMainWindow {\n"
"    background-color: #FFF;\n"
"    font: 13pt \"Roboto Condensed\";\n"
"}\n"
"\n"
"QLabel {\n"
"    font: 13pt \"Roboto Condensed\";\n"
"}\n"
"\n"
"QTableWidget {\n"
"    text-align: left;\n"
"    font: 13pt \"Roboto Condensed\";\n"
"    color: rgba(0, 0, 0, 0.84);\n"
"    border: 0;\n"
"}\n"
"\n"
"QTableView QTableCornerButton::section {\n"
"    background-color: #FFF;\n"
"    border: 0;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    text-align: left;\n"
"    font: 12pt \"Roboto Condensed\";\n"
"    font-style: normal;\n"
"    font-weight: normal;\n"
"    color: rgba(0, 0, 0, 0.54);\n"
"    background-color: #FFF;\n"
"    border: 0;\n"
"}\n"
"\n"
"QHeaderView::section:hover, QHeaderView::section:focus, QHeaderView::section:checked {\n"
"    text-align: left;\n"
"    font: 0;\n"
"    font: 12pt \"Roboto Condensed\";\n"
"    color: rgba(0, 0, 0, 0.94);\n"
"    font-style: normal;\n"
"    font-weight: normal;\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    border: #000 1px solid;\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background-color: #EEEEEE;\n"
"    color: rgba(0, 0, 0, 0.84);\n"
"    border: 0;\n"
"}\n"
"\n"
"QTableWidget::item:hover {\n"
"    background-color: #EEEEEE;\n"
"    color: rgba(0, 0, 0, 0.84);\n"
"}\n"
"\n"
"QPushButton {\n"
"    font: 14pt \"Roboto Condensed\";\n"
"    text-transform: uppercase;\n"
"    border-radius: 2px;\n"
"    height: 36px;\n"
"    padding-left: 16px;\n"
"    padding-right: 16px;\n"
"    min-width: 88px;\n"
"    background-color: #2196F3;\n"
"    color: #000000;\n"
"}\n"
"\n"
"QPushButton:Hover {\n"
"    background-color: #1E88E5;\n"
"}\n"
"\n"
"QPushButton:Pressed {\n"
"    background-color: #1976D2;\n"
"}\n"
"\n"
"QPushButton:Disabled {\n"
"    color: rgba(0, 0, 0, 0.4);\n"
"    background-color: rgba(0, 0, 0, 0.12);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.addEmployeeDialog = QtWidgets.QPushButton(self.centralwidget)
        self.addEmployeeDialog.setEnabled(True)
        self.addEmployeeDialog.setObjectName("addEmployeeDialog")
        self.gridLayout.addWidget(self.addEmployeeDialog, 3, 1, 1, 1)
        self.employeeTables = QtWidgets.QTableWidget(self.centralwidget)
        self.employeeTables.setRowCount(0)
        self.employeeTables.setColumnCount(0)
        self.employeeTables.setObjectName("employeeTables")
        self.gridLayout.addWidget(self.employeeTables, 1, 0, 1, 6)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 3, 4, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 3, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 4, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 582, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Employee manager"))
        self.addEmployeeDialog.setText(_translate("MainWindow", "Add Employee"))

