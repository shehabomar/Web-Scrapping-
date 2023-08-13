import tkinter as tk
from random import randint


class RandomArtGenerator:
    def __init__(self):
        self.width = 500
        self.height = 500
        # setting 6 different colors in string py list
        self.colors = ['#FF0000', '#00FF00',
                       '#0000FF', '#845EC2', '#2C73D2', '#FFFF00', '#FF00FF', '#2F4858', '#7095B2', '#00FFFF']
        self.create_window()

    def create_window(self):
        # creatong the root window and set its baisc attributes
        self.root = tk.Tk()
        self.root.title('Art Generator')
        self.root.config(bg='red')
        self.root.geometry('{}x{}'.format(self.width, self.height))
        self.root.minsize(500, 500)

        # setting the canvas
        self.canvas = tk.Canvas(
            self.root, width=self.width, height=self.height)
        # expand = True to accept the resizing, too
        self.canvas.pack(fill='both', expand=1)
        self.draw_random_art()

        # binding the '<Configure>' event to the 'on_resize' method
        self.root.bind('<Configure>', self.on_resize)

    def draw_random_art(self):
        self.canvas.delete('all')
        for i in range(0, 70):
            # random in range
            x1 = randint(0, self.width)
            y1 = randint(0, self.height)
            x2 = randint(0, self.width)
            y2 = randint(0, self.height)
            # retrieving a randomly selected color string from the colors list, using the randint
            color = self.colors[randint(0, len(self.colors)-1)]
            # random thickness of range (1 to 4 pixels)
            thickness = randint(1, 2)
            self.canvas.create_line(
                x1, y1, x2, y2, fill=color, width=thickness)

    def on_resize(self, event):
        # simply update the width and height attributes and passed them by event (the current window's width, height)
        self.width = event.width
        self.height = event.height

        # update the canvas size
        self.canvas.config(width=self.width, height=self.height)

        # Redraw the random art with new canvas size
        self.draw_random_art()

    def run(self):
        self.root.mainloop()


app = RandomArtGenerator()
app.run()
# I just don't undertand why it applies the dunction when I change the position of the window