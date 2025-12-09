import json
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QCheckBox, QHBoxLayout, QHeaderView, QLineEdit, QPushButton
from PyQt5.QtCore import Qt

class Table(QWidget):
  def __init__(self, filePath):
    super().__init__()
    self.filePath = filePath
    self.data = []
    print(filePath)
    with open(filePath, "r") as f:
      content = f.read().strip()
      data = json.loads(content) if content else []
    if not data:
      return
    self.table = QTableWidget()
    self.table.setAlternatingRowColors(True)
    self.table.verticalHeader().setDefaultSectionSize(28)
    self.table.verticalHeader().setMinimumWidth(30)
    self.table.verticalHeader().setStretchLastSection(False)
    self.table.verticalHeader().setDefaultAlignment(Qt.AlignCenter)
    self.table.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
    self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    layout = QVBoxLayout(self)
    layout.addWidget(self.table)
    self.table.blockSignals(True)
    self.load_data(data)
    self.table.blockSignals(False)
    self.table.itemChanged.connect(self.save_row)
    self.table.itemChanged.connect(self.on_item_changed)

    bar = QHBoxLayout()

    self.delete_input = QLineEdit()
    self.delete_input.setPlaceholderText("Enter row number")
    delete_btn = QPushButton("Delete Row")
    delete_btn.clicked.connect(self.delete_row)

    bar.addWidget(self.delete_input)
    bar.addWidget(delete_btn)

    layout.addLayout(bar)



    print(data)
  
  def load_data(self, data):
    if not data:
      self.table.setRowCount(0)
      self.table.setColumnCount(0)
      return

    headers = data[0]
    rows = data[1:]

    self.table.setColumnCount(len(headers))
    self.table.setHorizontalHeaderLabels(headers)
    self.table.setRowCount(len(rows))

    for row_index, row_data in enumerate(rows):
      for col_index, value in enumerate(row_data):
        if isinstance(value, bool):
          self.add_checkbox(row_index, col_index, value)
        else:
          cell = QTableWidgetItem(str(value))
          cell.setTextAlignment(Qt.AlignCenter)
          self.table.setItem(row_index, col_index, cell)
    self.add_blank_row()
    
  def add_blank_row(self):
    row_count = self.table.rowCount()
    self.table.insertRow(row_count)

    for col in range(self.table.columnCount() - 1):
      item = QTableWidgetItem("")
      item.setTextAlignment(Qt.AlignCenter)
      self.table.setItem(row_count, col, item)

  def check_last_row(self):
    row_index = self.table.rowCount() - 1
    for col in range(self.table.columnCount() - 1):
      item = self.table.item(row_index, col)
      if not item or not item.text().strip():
        return False
    return True

  def save_row(self):
    row_index = self.table.rowCount() - 1
    if not self.check_last_row():
      return
    row_data = []
    for col in range(self.table.columnCount() - 1):
      item = self.table.item(row_index, col)
      value = item.text().strip() if item else ""
      row_data.append(value)
    if not self.table.cellWidget(row_index, self.table.columnCount() - 1):
      self.add_checkbox(row_index, self.table.columnCount()-1, False)
    row_data.append(False)

    with open(self.filePath, "r") as f:
      content = f.read().strip()
      self.data = json.loads(content) if content else []
      self.data.append(row_data)
    with open(self.filePath, "w") as f: 
        json.dump(self.data, f, indent=2)
    self.add_blank_row()
  
  def add_checkbox(self, row, col, value):
    checkbox = QCheckBox()
    checkbox.setChecked(value)
    checkbox.stateChanged.connect(lambda state, r=row, c=col: self.on_checkbox_changed(r, c, state))
    container = QWidget()
    layout = QHBoxLayout(container)
    layout.addStretch()
    layout.addWidget(checkbox)
    layout.addStretch()
    layout.setContentsMargins(0, 0, 0, 0)
    container.setAttribute(Qt.WA_TranslucentBackground)
    container.setStyleSheet("background: transparent;")
    self.table.setCellWidget(row, col, container)

  def on_item_changed(self, item):
    row = item.row()

    if not self.check_last_row():
      return

    with open(self.filePath, "r") as f:
      jsonFile = json.load(f)

    row_data = []
    for c in range(self.table.columnCount() - 1):
      row_data.append(self.table.item(row, c).text().strip())

    checkbox_widget = self.table.cellWidget(row, self.table.columnCount() - 1)
    checkbox = checkbox_widget.findChild(QCheckBox) if checkbox_widget else None
    row_data.append(checkbox.isChecked() if checkbox else False)
    jsonFile.append(row_data)

    with open(self.filePath, "w") as f:
      json.dump(jsonFile, f, indent=2)

    self.table.blockSignals(True)
    self.add_blank_row()
    self.table.blockSignals(False)

  def on_checkbox_changed(self, r, c, state):
    print("CHECKBOX CHANGED")
    checked = state == 2
    with open(self.filePath, "r") as f:
      jsonFile = json.load(f)
    jsonFile[r+1][c] = checked
    with open(self.filePath, "w") as f:
      json.dump(jsonFile, f, indent=2)

  def delete_row(self):
    text = self.delete_input.text().strip()
    if not text.isdigit():
      return
    row = int(text) - 1

    if row < 0 or row >= self.table.rowCount() - 1:
      return

    self.table.removeRow(row)

    with open(self.filePath, "r") as f:
      jsonFile = json.load(f)

    if row < len(jsonFile):
      jsonFile.pop(row)

    with open(self.filePath, "w") as f:
      json.dump(jsonFile, f, indent=2)