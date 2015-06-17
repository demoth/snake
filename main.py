import tkinter as tk
import logic

RUNNING = True

START = '1.0'

screen = [[' ' for x in range(logic.WIDTH)] for y in range(logic.HEIGHT)]

def screen_to_str(scr):
    return '\n'.join(''.join(line) for line in scr)

def draw(widget, screen):
    widget['state'] = 'normal'
    widget.delete('1.0', tk.END)
    widget.insert('1.0', screen_to_str(screen))
    widget['state'] = 'disabled'

root = tk.Tk()
field = tk.Text(root, width=logic.WIDTH, height=logic.HEIGHT, state='disabled', font='monospace')
field.pack()
draw(field, screen)

def loop():
    if RUNNING:
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
loop()
tk.mainloop()
RUNNING = False