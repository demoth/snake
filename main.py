import tkinter as tk
import logic

START = '1.0'

class Screen:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = {}

    def clear(self):
        self.cells = {}

    def to_widget(self):
        result = '\n'.join(''.join(self.cells.get((x, y), ' ')
                                   for x in range(self.width))
                           for y in range(self.height))
        return result

    def _boundary_check(self, point):
        if not 0 <= point[0] < self.width:
            raise ValueError()
        if not 0 <= point[1] < self.height:
            raise ValueError()

    def __setitem__(self, key, value):
        self._boundary_check(key)
        assert len(value) == 1
        self.cells[key] = value

    def __getitem__(self, item):
        self._boundary_check(item)
        return self.cells.get(item, ' ')

screen = Screen(logic.WIDTH, logic.HEIGHT)

def draw(widget, screen):
    widget['state'] = 'normal'
    widget.delete('1.0', tk.END)
    widget.insert('1.0', screen.to_widget())
    widget['state'] = 'disabled'

root = tk.Tk()
field = tk.Text(root, width=logic.WIDTH, height=logic.HEIGHT, state='disabled', font='Courier')
field.pack()
draw(field, screen)

def loop():
    root.after(logic.RATE, loop)
    logic.update(screen)
    draw(field, screen)

callback_mapping = {
    '<Left>': logic.left,
    '<Right>': logic.right,
    '<Up>': logic.up,
    '<Down>': logic.down,
}

def quit(e):
    root.destroy()

for key, func in callback_mapping.items():
    root.bind(key, func)

root.bind('<Escape>', quit)

if __name__ == '__main__':
    loop()
    tk.mainloop()
