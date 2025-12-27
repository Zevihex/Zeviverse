import sys, os, shutil
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QStackedWidget, QLabel, QShortcut
from PyQt5.QtGui import QKeySequence, QFontDatabase, QFont
from views.collection import Collection
from views.dashboard import Dashboard
from views.goals import Goals
from views.links import Links
from views.schedule import Schedule
from views.tabs import Tabs
from views.todos import ToDos
from views.trackers import Trackers
from views.wishlists import Wishlists
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

    self.menu = Menu(self.window_widget, window_layout, self.stack)
    self.collection_widget = Collection(self.stack)
    self.dashboard_widget = Dashboard(self.stack)
    self.goals_widget = Goals(self.stack)
    self.links_widget = Links(self.stack)
    self.schedule_widget = Schedule(self.stack)
    self.tabs_widget = Tabs(self.stack)
    self.todos_widget = ToDos(self.stack)
    self.trackers_widget = Trackers(self.stack)
    self.wishlists_widget = Wishlists(self.stack)
    self.stack.addWidget(self.window_widget)
    self.stack.addWidget(self.collection_widget)
    self.stack.addWidget(self.dashboard_widget)
    self.stack.addWidget(self.goals_widget)
    self.stack.addWidget(self.links_widget)
    self.stack.addWidget(self.schedule_widget)
    self.stack.addWidget(self.tabs_widget)
    self.stack.addWidget(self.todos_widget)
    self.stack.addWidget(self.trackers_widget)
    self.stack.addWidget(self.wishlists_widget)
    self.nav = self.menu.nav
    self.nav.right_click_toggle(self) 

    self.label = QLabel("Main Page")
    self.label.setObjectName("label")
    window_layout.addWidget(self.label)

    shortcut = QShortcut(QKeySequence("Escape"), self)
    shortcut.activated.connect(QApplication.quit)

    font_id = QFontDatabase.addApplicationFont("./styles/fonts/science_gothic.ttf")
    if font_id == -1:
      print("Failed to load font")
    else:
      font_families = QFontDatabase.applicationFontFamilies(font_id)
      print("Loaded font families: ", font_families)


def main():
  app = QApplication(sys.argv)
  window = Window()
  window.showFullScreen()
  style_path = os.path.join("styles","style.qss")
  app.setFont(QFont("Science Gothic", 12))
  if os.path.exists(style_path):
    with open(style_path,"r") as f:
      app.setStyleSheet(f.read())
  sys.exit(app.exec_())
  if not os.path.exists("data/tabs.json"):
    shutil.copy("data/tabs.default.json", "data/tabs.json")

if __name__ == "__main__":
  main()
