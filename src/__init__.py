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

		self.employees = []
		for employee in self.session.query(Employee).all():
			self.employees.append((employee.fullname, employee.position, employee.pay))

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
			self.employees.append((name, position, pay))
			self.session.add(Employee(
				fullname=name,
				position=position,
				pay=pay))
			self.session.commit()
			self.focus_main()

		else:
			pass

	def focus_new_employee(self):
		self.new_employee_window.setupUi(self.window)

		self.new_employee_window.cancel.clicked.connect(self.focus_main)
		self.new_employee_window.addEmployee.clicked.connect(self.add_employee)

	def focus_main(self):
		self.main_window.setupUi(self.window)

		self.tm = table_manager(self.main_window.employeeTables)

		for employee in self.employees:
			self.tm.add_row(employee)
			
		self.main_window.addEmployeeDialog.clicked.connect(self.focus_new_employee)

EmployeeManager()