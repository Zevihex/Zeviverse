from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from controllers.menu import Menu
from utils.table_maker import Table

class Wishlists(QWidget):
  def __init__(self, stack):
    super().__init__()
    self.stack = stack

    self.layout = QVBoxLayout(self)
    self.layout.setContentsMargins(0, 0, 0, 0)

    def make_table(fileName):
      table_widget = Table(f"./data/wishlists/{fileName}.json")
      layout = self.layout
      while layout.count() > 1:
        item = layout.takeAt(1)
        w = item.widget()
        if w:
          w.deleteLater()
      layout.addWidget(table_widget)
      
    self.menu = Menu(self, self.layout, self.stack, "Wishlists", make_table)
    self.nav = self.menu.nav
    self.nav.right_click_toggle(self)

    self.label = QLabel("Wishlists")
    self.label.setObjectName("label")
    self.layout.addWidget(self.label)
