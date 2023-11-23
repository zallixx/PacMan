import pyray

class Button:
    def __init__(self, x, y, width, height, text):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.color = pyray.WHITE

    def draw(self):
        pyray.draw_rectangle(self.x, self.y, self.width, self.height, self.color)
        pyray.draw_text(self.text, self.x + 10, self.y + 10, 20, pyray.BLACK)

    def is_mouse_on_button(self):
        mouse_x, mouse_y = pyray.get_mouse_x(), pyray.get_mouse_y()
        return self.x <= mouse_x <= self.x + self.width and self.y <= mouse_y <= self.y + self.height
