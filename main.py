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


class GameWindow:

    def __init__(self):
        self.field = None
        self.looper = None
        self.root = tk.Tk()
        self.game_selector = tk.Frame(self.root)
        self.game_selector.pack()
        self.buttons = []
        for game in logic.games:
            self.buttons.append(self.create_button(self.game_selector, game))
        self.root.mainloop()

    def create_button(self, widget, game):
        text = "{}\n{}".format(game.__name__, game.__doc__)

        def start_game():
            self.start_game(game)

        b = tk.Button(widget, text=text.strip(), command=start_game)
        b.game_class = game
        b.pack()
        return b

    def start_game(self, game):
        #self.game_selector.pack_forget()
        if self.field is not None:
            self.field.pack_forget()
        if self.looper is not None:
            self.root.after_cancel(self.looper)
        self.screen = Screen(game.WIDTH, game.HEIGHT)
        self.game = game(self.screen)
        self.field = tk.Text(self.root, width=self.game.WIDTH, height=self.game.HEIGHT, state='disabled', font='Courier')
        self.field.pack()
        self.draw()

        callback_mapping = {
            '<Left>': self.game.left,
            '<Right>': self.game.right,
            '<Up>': self.game.up,
            '<Down>': self.game.down,
        }

        for key, func in callback_mapping.items():
            self.root.bind(key, func)

        self.root.bind('<Escape>', self.close)
        self.loop()

    def draw(self):
        self.field['state'] = 'normal'
        self.field.delete('1.0', tk.END)
        self.field.insert('1.0', self.screen.to_widget())
        self.field['state'] = 'disabled'

    def loop(self):
        self.looper = self.root.after(self.game.RATE, self.loop)
        self.game.update()
        self.draw()

    def close(self, e):
        self.root.destroy()

if __name__ == '__main__':
    window = GameWindow()
