import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog, QWidget, QStackedWidget
from models import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from ui.main_window import Ui_MainWindow as Main_window
from ui.new_employee_window import Ui_MainWindow as New_employee_window
from table_manager import table_manager

class EmployeeManager:
	def __init__(self):
		self.engine = create_engine('sqlite:///employee_manager.db')
		Base.metadata.create_all(self.engine)
		DBSession = sessionmaker(bind=self.engine)
		self.session = DBSession()

		self.employees = {}
		for employee in self.session.query(Employee).all():
			self.employees[employee.id] = (employee.fullname, employee.position, employee.pay, str(employee.id))

		self.app = QApplication(sys.argv)
		self.window = QMainWindow()

		self.main_window = Main_window()
		self.new_employee_window = New_employee_window()

		self.focus_main()

		self.window.show()
		sys.exit(self.app.exec_())

	def add_employee(self):
		name = self.new_employee_window.fullName.text()
		position = self.new_employee_window.position.text()
		pay = self.new_employee_window.pay.text()

		if name != '' and position != '' and pay != '':
			new_employee = Employee(fullname=name, position=position, pay=pay)
			self.employees[str(new_employee.id)] = (new_employee.fullname, new_employee.position, new_employee.pay, str(new_employee.id))
			self.session.add(new_employee)
			self.session.commit()
			self.focus_main()

		else:
			pass

	def edit_employee(self):
		name = self.new_employee_window.fullName.text()
		position = self.new_employee_window.position.text()
		pay = self.new_employee_window.pay.text()

		if name != '' and position != '' and pay != '':
			employee = self.session.query(Employee).filter_by(id=self.info[3]).first()
			employee.fullname = name
			employee.position = position
			employee.pay = pay
			self.employees[employee.id] = (employee.fullname, employee.position, employee.pay, str(employee.id))
			self.session.commit()
			self.focus_main()

		else:
			pass

	def focus_new_employee(self):
		self.new_employee_window.setupUi(self.window)

		self.new_employee_window.cancel.clicked.connect(self.focus_main)
		self.new_employee_window.addEmployee.clicked.connect(self.add_employee)

	def focus_edit_employee(self):
		info = [i.text() for i in self.tm.table.selectedItems()]
		self.new_employee_window.setupUi(self.window)

		self.new_employee_window.fullName.setText(info[0])
		self.new_employee_window.position.setText(info[1])
		self.new_employee_window.pay.setText(info[2])
		self.info = info

		self.new_employee_window.cancel.clicked.connect(self.focus_main)
		self.new_employee_window.addEmployee.setText('Edit Employee')
		self.new_employee_window.addEmployee.clicked.connect(self.edit_employee)

	def focus_main(self):
		self.main_window.setupUi(self.window)

		self.tm = table_manager(self.main_window.employeeTables)

		for key, val in self.employees.items():
			self.tm.add_row(val)
			
		self.main_window.addEmployeeDialog.clicked.connect(self.focus_new_employee)
		self.tm.table.clicked.connect(self.focus_edit_employee)

EmployeeManager()