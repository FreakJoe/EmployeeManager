import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog, QWidget
from ui.main_window import Ui_MainWindow
from table_manager import table_manager

app = QApplication(sys.argv)
window = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(window)

tm = table_manager(ui.employeeTables)
tm.set_column_count(3)
tm.set_row_count(0)

def add_employee_dialog():
	name, ok = QInputDialog.getText(QWidget(), 'Employee name', 'Please enter the employee\'s name.')
	position, ok = QInputDialog.getText(QWidget(), 'Employee position', 'Please enter the employee\'s position.')
	salary, ok = QInputDialog.getText(QWidget(), 'Employee salary', 'Please enter the employee\'s salary.')
	tm.add_row((name, position, salary))
	
ui.addEmployee.clicked.connect(add_employee_dialog)

window.show()
sys.exit(app.exec_())