from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from controllers.menu import Menu

class Trackers(QWidget):
  def __init__(self, stack):
    super().__init__()
    self.stack = stack

    layout = QVBoxLayout(self)
    layout.setContentsMargins(0, 0, 0, 0)

    self.menu = Menu(self, layout, self.stack)
    self.nav = self.menu.nav

    self.label = QLabel("Trackers")
    self.label.setObjectName("label")
    layout.addWidget(self.label)