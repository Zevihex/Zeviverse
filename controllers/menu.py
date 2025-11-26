from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QFrame
from PyQt5.QtCore import Qt, QPropertyAnimation

class Menu:
  def __init__(self, parent_widget, window_layout):
    self.parent = parent_widget

    top_bar = QHBoxLayout()
    window_layout.addLayout(top_bar)

    self.hamburger_btn = QPushButton("☰")
    self.hamburger_btn.setFixedSize(60, 60)
    top_bar.addWidget(self.hamburger_btn)
    top_bar.addStretch()
    window_layout.addStretch()

    self.side_menu = QFrame(self.parent)
    self.side_menu.setObjectName("side_menu")
    self.side_menu.setGeometry(-200, 0, 200, self.parent.height())

    self.side_menu_layout = QVBoxLayout(self.side_menu)
    self.side_menu_layout.setContentsMargins(0, 0, 0, 0)

    self.close_btn = QPushButton("✕")
    self.close_btn.setFixedSize(50, 50)

    self.side_menu_layout.addWidget(self.close_btn, alignment=Qt.AlignRight | Qt.AlignTop)

    self.main_btn = QPushButton("Home")
    self.dashboard_btn = QPushButton("Dashboard")
    self.collection_btn = QPushButton("Collection")
    self.side_menu_layout.addWidget(self.main_btn)
    self.side_menu_layout.addWidget(self.dashboard_btn)
    self.side_menu_layout.addWidget(self.collection_btn)

    self.menu_anim = QPropertyAnimation(self.side_menu, b"geometry")
    self.menu_anim.setDuration(250)

    self.menu_visible = False
