import sys, os
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QStackedWidget, QLabel, QShortcut
from PyQt5.QtGui import QKeySequence
from views.dashboard import Dashboard
from views.collection import Collection
from controllers.navigation import Navigation
from controllers.menu import Menu

class Window(QWidget):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Zeviverse")
    self.layout = QVBoxLayout(self)
    self.stack = QStackedWidget()
    self.window_widget = QWidget()
    window_layout = QVBoxLayout(self.window_widget)
    self.layout.setContentsMargins(0, 0, 0, 0)
    window_layout.setContentsMargins(0, 0, 0, 0)
    self.layout.addWidget(self.stack)


    self.menu = Menu(self.window_widget, window_layout)
    self.dashboard_widget = Dashboard(self.stack)
    self.collection_widget = Collection(self.stack)
    self.stack.addWidget(self.window_widget)
    self.stack.addWidget(self.dashboard_widget)
    self.stack.addWidget(self.collection_widget)

    self.nav = Navigation(self.menu.side_menu, self.stack)
    self.menu.hamburger_btn.clicked.connect(lambda: self.nav.toggle_menu())
    self.menu.close_btn.clicked.connect(lambda: self.nav.toggle_menu())
    self.menu.main_btn.clicked.connect(lambda: self.nav.show_page(self.stack.widget(0)))
    self.menu.dashboard_btn.clicked.connect(lambda: self.nav.show_page(self.stack.widget(1)))
    self.menu.collection_btn.clicked.connect(lambda: self.nav.show_page(self.stack.widget(2)))

    self.label = QLabel("Main Page")
    self.label.setObjectName("label")
    window_layout.addWidget(self.label)

    shortcut = QShortcut(QKeySequence("Escape"), self)
    shortcut.activated.connect(QApplication.quit)

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
