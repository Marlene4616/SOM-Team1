from tkinter import *

class GUI():
    canvas = None
    window = None #Tkinter root window
    canvas_width = None
    canvas_height = None
    status_text = None
    count = 0
    stop_count = False
    winning_text ='winner!!!!!!! winner!!!!!!!!!! chicken dinner!!!!!!!!'

    # function can be used without creating an object of the class
    @classmethod
    def setup(cls, width: int = 700, height: int = 500):
        """initializes the GUI variables

        :param width: set window width default = 700
        :param height: set window height default = 500
        """
        cls.window = Tk() #creates a window
        cls.window.title('Towers of Hanoi')
        cls.canvas = Canvas()  #creates the Canvas
        cls.status_text = Label()
        cls.canvas_width = width
        cls.canvas_height = height

    @classmethod
    def update_state(cls, tower_a: [], tower_b: [], tower_c: [], num_discs: int):
        """updates the GUI-window depending on the actual state for all towers and discs

        :param tower_a: list containing disc numbers in tower_a
        :param tower_b: list containing disc numbers in tower_b
        :param tower_c: list containing disc numbers in tower_c
        :param num_discs:  total number of discs
        """
        # variable reset
        cls.canvas.destroy()
        cls.status_text.destroy()

        cls.canvas = Canvas(cls.window, width=cls.canvas_width, height=cls.canvas_height)
        # calculates the x-coordinates for all 3 pegs
        peg_x = [
            cls.canvas_width / 3 - cls.canvas_width/8,
            cls.canvas_width / 2,
            cls.canvas_width * 2 / 3 + cls.canvas_width / 8
            ]
        # creates 3 black rectangles for each peg in the GUI
        peg1 = cls.canvas.create_rectangle(peg_x[0]-5, cls.canvas_height/20, peg_x[0]+5, cls.canvas_height, fill="black")
        peg2 = cls.canvas.create_rectangle(peg_x[1]-5,cls.canvas_height/20, peg_x[1]+5, cls.canvas_height, fill="black")
        peg3 = cls.canvas.create_rectangle(peg_x[2]-5, cls.canvas_height/20, peg_x[2]+5, cls.canvas_height, fill="black")
        # calculates the height of the ground
        ground_y = cls.canvas_height-cls.canvas_height/30
        # creates the ground
        ground = cls.canvas.create_rectangle(0, cls.canvas_height, cls.canvas_width, ground_y, fill="black")
        # calculates the disc height
        disc_height = cls.canvas_height/8
        # calculates the gap between the discs
        disc_gap = disc_height/10
        # calculates the max disc width, depending on the number of discs n
        max_disc_width = peg_x[1] - peg_x[0]
        disc_w_multi = max_disc_width/(num_discs*2)
        # List of colours for the discs
        colours = ['light blue', 'teal', 'dark green', 'light green', 'light yellow', 'orange', 'red', 'purple', 'dark blue', 'gray']
        # creates a message in the GUI about the current move
        cls.status_text = Label(cls.window,
                                text=(f'Move {cls.count} \n' + cls.winning_text if cls.stop_count else f'Move {cls.count}'),
                                # font typ and size
                                font=('Arial', 18))
        # shows the status text in the GUI window
        cls.status_text.pack()
        # move counter
        if not cls.stop_count:
            cls.count += 1
        #
        for i, tower in enumerate([tower_a, tower_b, tower_c]):

            # gives the disc width depending on
            for j, disc_width in enumerate(tower):
                x0 = peg_x[i] - disc_width * disc_w_multi
                x1 = peg_x[i] + disc_width * disc_w_multi
                y0 = ground_y - disc_height - disc_height * j
                y1 = ground_y - disc_gap - disc_height * j
                disc = cls.canvas.create_rectangle(x0, y0, x1, y1, fill=colours[disc_width - 1])
        # shows the pegs, ground and discs in the GUI window
        cls.canvas.pack()
        # opens the GUI window
        cls.window.update()
