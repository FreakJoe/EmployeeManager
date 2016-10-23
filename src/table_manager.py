from PyQt5.QtWidgets import QTableWidgetItem, QTableWidget, QHeaderView


class table_manager():
	def __init__(self, table):
		self.table = table
		self.set_column_count(3)
		self.set_row_count(0)
		self.table.setHorizontalHeaderItem(0, QTableWidgetItem('Full name'))
		self.table.setHorizontalHeaderItem(1, QTableWidgetItem('Position'))
		self.table.setHorizontalHeaderItem(2, QTableWidgetItem('Hourly pay'))

		self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

	def set_column_count(self, count):
		self.table.setColumnCount(count)

	def set_row_count(self, count):
		self.table.setRowCount(count)

	def set_item(self, row, column, text):
		self.table.setItem(row - 1, column - 1, QTableWidgetItem(text))

	def row_count(self):
		return self.table.rowCount()

	def column_count(self):
		return self.table.columnCount()

	def add_row(self, row_content):
		self.set_row_count(self.row_count() + 1)
		self.set_item(self.row_count(), 1, row_content[0])
		self.set_item(self.row_count(), 2, row_content[1])
		self.set_item(self.row_count(), 3, row_content[2])