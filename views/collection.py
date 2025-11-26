from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from controllers.menu import Menu
from controllers.navigation import Navigation

class Collection(QWidget):
  def __init__(self, stack):
    super().__init__()
    self.stack = stack

    layout = QVBoxLayout(self)
    layout.setContentsMargins(0, 0, 0, 0)

    self.menu = Menu(self, layout)
    self.nav = Navigation(self.menu.side_menu, self.stack)
    self.menu.hamburger_btn.clicked.connect(self.nav.toggle_menu)
    self.menu.close_btn.clicked.connect(self.nav.toggle_menu)
    self.menu.main_btn.clicked.connect(lambda: self.nav.show_page(self.stack.widget(0)))
    self.menu.dashboard_btn.clicked.connect(lambda: self.nav.show_page(self.stack.widget(1)))
    self.menu.collection_btn.clicked.connect(lambda: self.nav.show_page(self.stack.widget(2)))

    self.label = QLabel("Collection")
    self.label.setObjectName("label")
    layout.addWidget(self.label)