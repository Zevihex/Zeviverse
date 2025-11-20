import sys, os
from PyQt5.QtWidgets import (
  QApplication, QWidget, QVBoxLayout, QHBoxLayout, QStackedWidget,
  QPushButton, QFrame, QLabel, QShortcut
)
from PyQt5.QtCore import Qt, QPropertyAnimation, QRect
from PyQt5.QtGui import QKeySequence
from views.dashboard import Dashboard
from views.collection import Collection

class Window(QWidget):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Zeviverse")
    self.layout = QVBoxLayout(self)
    self.layout.setContentsMargins(0, 0, 0, 0)

    self.stack = QStackedWidget()
    self.layout.addWidget(self.stack)

    self.window_widget = QWidget()
    window_layout = QVBoxLayout(self.window_widget)
    window_layout.setContentsMargins(0,0,0,0)

    top_bar = QHBoxLayout()
    window_layout.addLayout(top_bar)
    self.hamburger_btn = QPushButton("☰")
    self.hamburger_btn.setFixedSize(60,60)
    top_bar.addWidget(self.hamburger_btn)
    top_bar.addStretch()
    window_layout.addStretch()
    self.label = QLabel("Main Page")
    self.label.setObjectName("label")
    window_layout.addWidget(self.label)

    self.side_menu = QFrame(self.window_widget)
    self.side_menu.setObjectName("side_menu")
    self.side_menu.setGeometry(-200,0,200,self.window_widget.height())
    self.side_menu_layout = QVBoxLayout(self.side_menu)
    self.side_menu_layout.setContentsMargins(0,0,0,0)
    self.close_btn = QPushButton("✕")
    self.close_btn.setFixedSize(50,50)
    self.side_menu_layout.addWidget(self.close_btn, alignment=Qt.AlignRight|Qt.AlignTop)
    self.dashboard_btn = QPushButton("Dashboard")
    self.collection_btn = QPushButton("Collection")
    self.side_menu_layout.addWidget(self.dashboard_btn)
    self.side_menu_layout.addWidget(self.collection_btn)
    self.menu_anim = QPropertyAnimation(self.side_menu, b"geometry")
    self.menu_anim.setDuration(250)
    self.menu_visible = False

    self.hamburger_btn.clicked.connect(self.toggle_menu)
    self.close_btn.clicked.connect(self.toggle_menu)
    self.dashboard_btn.clicked.connect(self.show_dashboard)
    self.collection_btn.clicked.connect(self.show_collection)

    self.dashboard_widget = Dashboard(self.stack)
    self.collection_widget = Collection(self.stack)
    self.stack.addWidget(self.window_widget)
    self.stack.addWidget(self.dashboard_widget)
    self.stack.addWidget(self.collection_widget)


    shortcut = QShortcut(QKeySequence("Escape"), self)
    shortcut.activated.connect(QApplication.quit)

  def toggle_menu(self):
    start_x, end_x = (0, -200) if self.menu_visible else (-200, 0)
    self.menu_visible = not self.menu_visible
    self.side_menu.raise_()
    self.menu_anim.stop()
    self.menu_anim.setStartValue(QRect(start_x, 0, 200, self.window_widget.height()))
    self.menu_anim.setEndValue(QRect(end_x, 0, 200, self.window_widget.height()))
    self.menu_anim.start()

  def show_dashboard(self):
    self.stack.setCurrentWidget(self.dashboard_widget)
    self.toggle_menu()
  
  def show_collection(self):
    self.stack.setCurrentWidget(self.collection_widget)
    self.toggle_menu()

  def resizeEvent(self, event):
    x = 0 if self.menu_visible else -200
    self.side_menu.setGeometry(x,0,200,self.window_widget.height())
    super().resizeEvent(event)

def main():
  app = QApplication(sys.argv)
  window = Window()
  window.showFullScreen()
  style_path = os.path.join("styles","style.qss")
  if os.path.exists(style_path):
    with open(style_path,"r") as f:
      app.setStyleSheet(f.read())
  sys.exit(app.exec_())

if __name__ == "__main__":
  main()
