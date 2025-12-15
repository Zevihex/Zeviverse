import json
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QPushButton, QFrame, QWidget
from PyQt5.QtCore import Qt, QPropertyAnimation
from controllers.navigation import Navigation
from controllers.tabMenu import TabMenu

class Menu:
  def __init__(self, parent_widget, window_layout, stack, category=None, get_name_for_table=None):
    self.parent = parent_widget
    self.stack = stack
    
    top_bar_widget = QWidget()
    top_bar_widget.setObjectName("top_bar")
    top_bar = QHBoxLayout(top_bar_widget)
    top_bar_widget.setContentsMargins(0, 0, 0, 0)
    top_bar.setContentsMargins(0, 0, 0, 0)
    top_bar.setSpacing(0)
    window_layout.addWidget(top_bar_widget)

    self.hamburger_btn = QPushButton("☰")
    self.hamburger_btn.setFixedSize(60, 60)
    self.tabs_layout = QHBoxLayout()
    self.tabs_layout.setSpacing(0)
    top_bar.addWidget(self.hamburger_btn)
    self.tab_menu = TabMenu(self.tabs_layout, category, get_name_for_table) #Refresh for different views? get_name_for_table = make_table

    if category and get_name_for_table:
      self.tab_menu.build_tabs()

    top_bar.addLayout(self.tabs_layout)

    top_bar.addStretch()
    window_layout.addStretch()

    self.side_menu = QFrame(self.parent)
    self.side_menu.setObjectName("side_menu")
    self.side_menu.setGeometry(-200, 0, 200, self.parent.height())

    self.side_menu_layout = QVBoxLayout(self.side_menu)
    self.side_menu_layout.setContentsMargins(0, 0, 0, 0)
    self.side_menu_layout.setAlignment(Qt.AlignTop)

    self.main_btn = QPushButton("Main")
    self.collection_btn = QPushButton("Collection")
    self.dashboard_btn = QPushButton("Dashboard")
    self.goals_btn = QPushButton("Goals")
    self.links_btn = QPushButton("Links")
    self.schedule_btn = QPushButton("Schedule")
    self.tabs_btn = QPushButton("Tabs")
    self.todos_btn = QPushButton("Todos")
    self.trackers_btn = QPushButton("Trackers")
    self.wishlists_btn = QPushButton("Wishlists")

    self.side_menu_layout.addWidget(self.main_btn)
    self.side_menu_layout.addWidget(self.collection_btn)
    self.side_menu_layout.addWidget(self.dashboard_btn)
    self.side_menu_layout.addWidget(self.goals_btn)
    self.side_menu_layout.addWidget(self.links_btn)
    self.side_menu_layout.addWidget(self.schedule_btn)
    self.side_menu_layout.addWidget(self.tabs_btn)
    self.side_menu_layout.addWidget(self.todos_btn)
    self.side_menu_layout.addWidget(self.trackers_btn)
    self.side_menu_layout.addWidget(self.wishlists_btn)

    self.menu_anim = QPropertyAnimation(self.side_menu, b"geometry")
    self.menu_anim.setDuration(250)
    self.menu_visible = False

    self.nav = Navigation(self.side_menu, self.stack)

    self.hamburger_btn.clicked.connect(self.nav.toggle_menu)
    self.main_btn.clicked.connect(lambda: self.nav.show_page(self.stack.widget(0)))
    self.collection_btn.clicked.connect(lambda: self.nav.show_page(self.stack.widget(1)))
    self.dashboard_btn.clicked.connect(lambda: self.nav.show_page(self.stack.widget(2)))
    self.goals_btn.clicked.connect(lambda: self.nav.show_page(self.stack.widget(3)))
    self.links_btn.clicked.connect(lambda: self.nav.show_page(self.stack.widget(4)))
    self.schedule_btn.clicked.connect(lambda: self.nav.show_page(self.stack.widget(5)))
    self.tabs_btn.clicked.connect(lambda: self.nav.show_page(self.stack.widget(6)))
    self.todos_btn.clicked.connect(lambda: self.nav.show_page(self.stack.widget(7)))
    self.trackers_btn.clicked.connect(lambda: self.nav.show_page(self.stack.widget(8)))
    self.wishlists_btn.clicked.connect(lambda: self.nav.show_page(self.stack.widget(9)))
