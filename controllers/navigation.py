from PyQt5.QtCore import QPropertyAnimation, QRect

class Navigation:
  def __init__(self, side_menu, stack):
    self.side = side_menu
    self.stack = stack
    self.menu_visible = False

    self.menu_anim = QPropertyAnimation(self.side, b"geometry")
    self.menu_anim.setDuration(250)

  def toggle_menu(self):
    parent_h = self.side.parent().height()

    if self.menu_visible:
      start = QRect(0, 0, 200, parent_h)
      end   = QRect(-200, 0, 200, parent_h)
    else:
      start = QRect(-200, 0, 200, parent_h)
      end   = QRect(0, 0, 200, parent_h)

    self.menu_visible = not self.menu_visible

    self.side.raise_()
    self.menu_anim.stop()
    self.menu_anim.setStartValue(start)
    self.menu_anim.setEndValue(end)
    self.menu_anim.start()

  def show_page(self, widget):
    self.stack.setCurrentWidget(widget)
    self.toggle_menu()

