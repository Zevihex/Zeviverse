from PyQt5.QtWidgets import QMessageBox

def show_warning(message, parent=None):
  msg = QMessageBox(parent)
  msg.setIcon(QMessageBox.Warning)
  msg.setWindowTitle("Warning")
  msg.setText(message)
  msg.setStandardButtons(QMessageBox.Ok)
  msg.exec_()

def show_success(message, parent=None):
  msg = QMessageBox(parent)
  msg.setIcon(QMessageBox.Information)
  msg.setWindowTitle("Success")
  msg.setText(message)
  msg.setStandardButtons(QMessageBox.Ok)
  msg.exec_()