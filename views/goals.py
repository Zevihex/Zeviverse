from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from controllers.menu import Menu
from utils.table_maker import Table

class Goals(QWidget):
  def __init__(self, stack):
    super().__init__()
    self.stack = stack

    self.layout = QVBoxLayout(self)
    self.layout.setContentsMargins(0, 0, 0, 0)

    def make_table(fileName):
      table_widget = Table(f"./data/goals/{fileName}.json")
      layout = self.layout
      while layout.count() > 1:
        item = layout.takeAt(1)
        w = item.widget()
        if w:
          w.deleteLater()
      layout.addWidget(table_widget)
      
    self.menu = Menu(self, self.layout, self.stack, "Goals", make_table)
    self.nav = self.menu.nav
    self.nav.right_click_toggle(self)

    self.label = QLabel("Goals")
    self.label.setObjectName("label")
    self.layout.addWidget(self.label)
