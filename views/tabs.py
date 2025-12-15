import json, os
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QComboBox, QLineEdit, QPushButton, QMessageBox
from controllers.menu import Menu
from utils.message_boxes import show_warning, show_success

class Tabs(QWidget):
  def __init__(self, stack):
    super().__init__()
    self.stack = stack

    layout = QVBoxLayout(self)
    layout.setContentsMargins(0, 0, 0, 0)

    self.menu = Menu(self, layout, self.stack)
    self.nav = self.menu.nav
    self.nav.right_click_toggle(self) 

    self.combo = QComboBox()
    self.combo.setParent(self)
    self.combo.addItems(["", "Goals", "ToDos", "Trackers", "Wishlists"])
    self.combo.setFixedSize(120, 30)
    self.combo.move(500, 100)

    self.line_edit = QLineEdit()
    self.line_edit.setParent(self)
    self.line_edit.setPlaceholderText("  Tab Name")
    self.line_edit.setFixedSize(120, 30)
    self.line_edit.move(500, 140)

    self.submit_btn = QPushButton("Submit")
    self.submit_btn.setParent(self)
    self.submit_btn.setObjectName("submit")
    self.submit_btn.clicked.connect(lambda: self.submit(self.combo.currentText(), self.line_edit.text()))
    self.submit_btn.setFixedSize(120, 30)
    self.submit_btn.move(500, 180)

    self.cat_combo = QComboBox()
    self.cat_combo.setParent(self)
    self.cat_combo.addItems(["", "Goals", "ToDos", "Trackers", "Wishlists"])
    self.cat_combo.setFixedSize(120, 30)
    self.cat_combo.move(700, 100)
    self.cat_combo.currentIndexChanged.connect(self.update_tab_combo)

    self.tab_combo = QComboBox()
    self.tab_combo.setParent(self)
    self.tab_combo.addItems([""])
    self.tab_combo.setFixedSize(120, 30)
    self.tab_combo.move(700, 140)

    self.delete_btn = QPushButton("Delete")
    self.delete_btn.setParent(self)
    self.delete_btn.setObjectName("delete")
    self.delete_btn.clicked.connect(lambda: self.delete(self.cat_combo.currentText(), self.tab_combo.currentText()))
    self.delete_btn.setFixedSize(120, 30)
    self.delete_btn.move(700, 180)

    
    self.label = QLabel("Tabs")
    self.label.setObjectName("label")
    layout.addWidget(self.label)
  
  def submit(self, category, name):
    name = name.lower()
    if not category or not name:
      show_warning("Both fields must be filled")
    else:
      self.combo.setCurrentIndex(0)
      self.line_edit.clear()
      with open("data/tabs.json", "r") as f:
        data = json.load(f)
      if category not in data:
        data[category] = []
      if name in data[category]:
        show_warning("Tab already exists!")
        return
      else:
        show_success("Submitted successfully")
      data[category].append(name)
      with open("data/tabs.json", "w") as f:
        json.dump(data, f, indent=2)
      category = category.lower()
      headers = []
      if category == "goals":
        headers = ["Goal", "Status", "Completed"]
      elif category == "todos":
        headers = ["Task", "Completed"]
      elif category == "trackers":
        headers = ["Game", "Completed"]
      elif category == "wishlists":
        headers = ["Item", "Completed"]
      with open(f"data/{category}/{name}.json", "w") as f:
        json.dump([headers], f, indent=2)


  def delete(self, category, name):
    if not category and not name:
      show_warning("Category must be filled")
    else:
      with open("data/tabs.json", "r") as f:
        content = f.read().strip()
        data = json.loads(content) if content else {}
      self.cat_combo.setCurrentIndex(0)
      self.tab_combo.setCurrentIndex(0)
      if(category in data and not name):
        del data[category]
        with open('data/tabs.json', "w") as f:
          json.dump(data, f, indent=2)
        for file in os.listdir(f"data/{category}"):
          os.remove(f"data/{category}/{file}")
        show_success("Deleted successfully")
      elif category in data and name in data[category]:
        data[category].remove(name)
        with open('data/tabs.json', "w") as f:
          json.dump(data, f, indent=2)     
        category = category.lower()
        name = name.lower()
        os.remove(f"data/{category}/{name}.json")
        show_success("Deleted successfully")
      else:
        show_warning("Deletion Unsuccessful")

  def update_tab_combo(self):
    text = self.cat_combo.currentText()
    self.tab_combo.clear()
    items = [""]
    with open("data/tabs.json", "r") as f:
      data = json.load(f)
    if not text:
      self.tab_combo.clear()
      return
    if data[text]:
      for item in data[text]:
        items.append(item)
      self.tab_combo.addItems(items)
  