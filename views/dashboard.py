from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QFrame
from PyQt5.QtCore import Qt, QRect, QPropertyAnimation

class Dashboard(QWidget):
  def __init__(self, stack):
    super().__init__()
    self.stack = stack

    layout = QVBoxLayout(self)
    layout.setContentsMargins(0,0,0,0)

    top_bar = QHBoxLayout()
    layout.addLayout(top_bar)
    self.hamburger_btn = QPushButton("☰")
    self.hamburger_btn.setFixedSize(60,60)
    top_bar.addWidget(self.hamburger_btn)
    top_bar.addStretch()

    self.label = QLabel("Dashboard")
    self.label.setObjectName("label")
    layout.addWidget(self.label)
    layout.addStretch()

    self.side_menu = QFrame(self)
    self.side_menu.setObjectName("side_menu")
    self.side_menu.setGeometry(-200,0,200,self.height())
    self.side_menu_layout = QVBoxLayout(self.side_menu)
    self.side_menu_layout.setContentsMargins(0,0,0,0)
    self.close_btn = QPushButton("✕")
    self.close_btn.setFixedSize(50,50)
    self.side_menu_layout.addWidget(self.close_btn, alignment=Qt.AlignRight|Qt.AlignTop)
    self.main_btn = QPushButton("Main")
    self.side_menu_layout.addWidget(self.main_btn)
    self.menu_anim = QPropertyAnimation(self.side_menu, b"geometry")
    self.menu_anim.setDuration(250)
    self.menu_visible = False

    # Connections
    self.hamburger_btn.clicked.connect(self.toggle_menu)
    self.close_btn.clicked.connect(self.toggle_menu)
    self.main_btn.clicked.connect(self.show_main)

  def toggle_menu(self):
    start_x, end_x = (0,-200) if self.menu_visible else (-200,0)
    self.menu_visible = not self.menu_visible
    self.side_menu.raise_()
    self.menu_anim.stop()
    self.menu_anim.setStartValue(QRect(start_x,0,200,self.height()))
    self.menu_anim.setEndValue(QRect(end_x,0,200,self.height()))
    self.menu_anim.start()

  def show_main(self):
    self.stack.setCurrentIndex(0)
    self.toggle_menu()

  def resizeEvent(self, event):
    x = 0 if self.menu_visible else -200
    self.side_menu.setGeometry(x,0,200,self.height())
    super().resizeEvent(event)
