from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from controllers.menu import Menu

class Goals(QWidget):
  def __init__(self, stack):
    super().__init__()
    self.stack = stack

    self.layout = QVBoxLayout(self)
    self.layout.setContentsMargins(0, 0, 0, 0)

    self.menu = Menu(self, self.layout, self.stack, "Goals")
    self.nav = self.menu.nav
    self.nav.right_click_toggle(self)

    self.label = QLabel("Goals")
    self.label.setObjectName("label")
    self.layout.addWidget(self.label)

  def show_item_widget(self, name):
    print(f"Show widget for: {name}")
