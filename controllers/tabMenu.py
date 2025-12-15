import json
from PyQt5.QtWidgets import QPushButton

class TabMenu:
  def __init__(self, tabs_layout, category, get_name_for_table):
    self.tabs_layout = tabs_layout
    self.category = category
    self.get_name_for_table = get_name_for_table

  def build_tabs(self, category=None):
    if category is None:
      category = self.category
    while self.tabs_layout.count() > 0:
      item = self.tabs_layout.takeAt(0)
      widget = item.widget()
      if widget:
        widget.deleteLater()

    with open("data/tabs.json", "r") as f:
      data = json.load(f)

    for name in data[category]:
      btn = QPushButton(name)
      btn.setFixedHeight(60)
      btn.setObjectName("tab")
      btn.clicked.connect(lambda _, n=name: self.get_name_for_table(n.lower()))
      self.tabs_layout.addWidget(btn)
