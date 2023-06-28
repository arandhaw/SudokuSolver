import tkinter as tk
import numpy as np
import sudokuAlgo as alg


EXAMPLE0 = [[1,0,0,4,8,9,0,0,6], 
            [7,3,0,0,0,0,0,4,0], 
            [0,0,0,0,0,1,2,9,5], 
            [0,0,7,1,2,0,6,0,0],
            [5,0,0,7,0,3,0,0,8],
            [0,0,6,0,9,5,7,0,0],
            [9,1,4,6,0,0,0,0,0],
            [0,2,0,0,0,0,0,3,7], 
            [8,0,0,5,1,2,0,0,4]]

EXAMPLE1 = [[1,0,0,0,8,4,0,0,0], 
            [0,0,0,1,0,0,6,0,0], 
            [0,0,0,0,9,0,0,0,0], 
            [4,0,0,7,0,0,0,8,0],
            [3,0,0,4,0,0,0,6,0],
            [5,0,1,0,2,8,0,7,3],
            [0,0,0,6,0,0,0,0,5],
            [0,0,7,0,0,1,0,0,0], 
            [0,0,0,5,4,0,0,0,8]]

EXAMPLE2 = [[0,0,0,6,0,0,4,0,0], 
            [7,0,0,0,0,3,6,0,0], 
            [0,0,0,0,9,1,0,8,0],
            [0,0,0,0,0,0,0,0,0], 
            [0,5,0,1,8,0,0,0,3],
            [0,0,0,3,0,6,0,4,5],
            [0,4,0,2,0,0,0,6,0],
            [9,0,3,0,0,0,0,0,0],
            [0,2,0,0,0,0,1,0,0]]

MARGIN = 20  # Pixels around the board
SIDE = 50  # Width of every board cell.
WIDTH = HEIGHT = MARGIN * 2 + SIDE * 9  # Width and height of the whole board

class GUI():
    def __init__(self):
        window = tk.Tk()
        window.title("Armaan's Sudoku Solver")
        self.problem = [[0]*9 for i in range(9)]
        self.canvas = tk.Canvas(window, bg="#ffffff", height=WIDTH, width=WIDTH)
        self.canvas.bind_all("<Key>", self.key_pressed)
        self.canvas.bind("<Button-1>", self.cell_clicked)
        self.x_cell = 0
        self.y_cell = 0
        self.previous = (0, 0)
        self.makeCanvas()
        self.fillNumbers()

        # define/bind buttons
        solve = tk.Button(window, text= "Solve", command=self.solve)
        clear = tk.Button(window, text= "Clear", command=self.clear)
        generate = tk.Frame(window)
        message = tk.Label(generate, text="    Generate Sodoku:    ")
        easy = tk.Button(generate, text= "Easy", width = 15, command=self.easy)
        medium = tk.Button(generate, text= "Medium", width = 15, command=self.medium)
        hard = tk.Button(generate, text= "Hard", width = 15, command=self.hard)
        message.pack(fill = tk.BOTH, side=tk.LEFT)
        hard.pack(fill = tk.BOTH, side=tk.RIGHT)
        medium.pack(fill = tk.BOTH, side=tk.RIGHT)
        easy.pack(fill = tk.BOTH, side=tk.RIGHT)

        # arrange buttons and canvas
        generate.pack(side=tk.TOP)
        self.canvas.pack(side=tk.TOP)
        clear.pack(fill = tk.BOTH, side=tk.TOP)
        solve.pack(fill = tk.BOTH, side=tk.TOP)
        
        #run the GUI
        window.mainloop()
    
    # Updates all numbers
    def fillNumbers(self):
        for i in range(9):
            for j in range(9):
                global canvas
                x_rect = MARGIN + j * SIDE
                y_rect = MARGIN + i * SIDE
                self.canvas.create_rectangle(x_rect + 1, y_rect + 1, x_rect + SIDE, y_rect + SIDE, 
                            width = 0, fill ="#81d4fa")
                if self.problem[i][j] != 0:
                    x = MARGIN + i * SIDE + SIDE / 2
                    y = MARGIN + j * SIDE + SIDE / 2
                    self.canvas.create_text(y, x, text=self.problem[i][j])

    # Update a single number
    def fillNum(self, j, i):
        if self.problem[i][j] != 0:
            x = MARGIN + i * SIDE + SIDE / 2
            y = MARGIN + j * SIDE + SIDE / 2
            self.canvas.create_text(y, x, text=self.problem[i][j])
    # draw lines for sodoku board
    def makeCanvas(self):
        for i in range(0, 10):
            color = "blue" if i%3 == 0 else "grey"
            x0 = MARGIN + i * SIDE
            y0 = MARGIN
            x1 = MARGIN + i * SIDE
            y1 = HEIGHT - MARGIN
            self.canvas.create_line(x0, y0, x1, y1, fill=color)
            
            x2 = MARGIN
            y2 = MARGIN + i*SIDE
            x3 = MARGIN + 9*SIDE
            y3 = MARGIN + i*SIDE
            self.canvas.create_line(x2, y2, x3, y3, fill=color)
    # callback when cell is clicked
    def cell_clicked(self, event):
        x, y = event.x, event.y
        if (MARGIN < x < WIDTH - MARGIN and MARGIN < y < HEIGHT - MARGIN):
            self.x_cell = int( (x - MARGIN)/SIDE )
            self.y_cell = int( (y - MARGIN)/SIDE )
            # unhighlight previous
            x_rect = MARGIN + self.previous[0] * SIDE
            y_rect = MARGIN + self.previous[1] * SIDE
            self.canvas.create_rectangle(x_rect + 1, y_rect + 1, x_rect + SIDE, y_rect + SIDE, 
                                        width = 0, fill ="#81d4fa")
            self.fillNum(self.previous[0], self.previous[1])

            # highlight cell
            x_rect = MARGIN + self.x_cell * SIDE
            y_rect = MARGIN + self.y_cell * SIDE
            self.canvas.create_rectangle(x_rect + 1, y_rect + 1, x_rect + SIDE, y_rect + SIDE, 
                                        width = 0, fill ="#ffffe0")
            # update state
            self.previous = (self.x_cell, self.y_cell)
            self.fillNum(self.x_cell, self.y_cell)
        else:
            # unhighlight previous
            x_rect = MARGIN + self.previous[0] * SIDE
            y_rect = MARGIN + self.previous[1] * SIDE
            self.canvas.create_rectangle(x_rect + 1, y_rect + 1, x_rect + SIDE, y_rect + SIDE, 
                                        width = 0, fill ="#81d4fa")
            self.fillNum(self.previous[0], self.previous[1])
            self.x_cell = 0
            self.y_cell = 0
            
    # callback when a key is pressed (only numbers, backspace do anything)
    def key_pressed(self, event):
        if self.x_cell >= 0 and self.y_cell >= 0 and event.char in "123456789\b":
            
            x_rect = MARGIN + self.previous[0] * SIDE
            y_rect = MARGIN + self.previous[1] * SIDE
            self.canvas.create_rectangle(x_rect + 1, y_rect + 1, x_rect + SIDE, y_rect + SIDE, 
                                        width = 0, fill ="#ffffe0")
            if event.char == '':
                pass
            elif event.char == '\b':    # delete number
                self.problem[self.y_cell][self.x_cell] = 0
            else:
                self.problem[self.y_cell][self.x_cell] = event.char
                self.fillNum(self.x_cell, self.y_cell)
    # solve the board
    def solve(self):
        try:
            ans = alg.findSolution(self.problem)
        except:
            self.popup()
        if ans is not None:
            self.problem = ans
            self.fillNumbers()
        else:
            self.popup()

    def popup(self):
        popup = tk.Tk()
        popup.title("Sudoku Error")
        tk.Label(popup, text= "No solution found", font=('Times', 24)).pack()
        popup.mainloop()
    # callback functions for buttons
    def easy(self):
        self.problem = EXAMPLE0.copy()
        self.fillNumbers()
    def medium(self):
        self.problem = EXAMPLE1.copy()
        self.fillNumbers()
    def hard(self):
        self.problem = EXAMPLE2.copy()
        self.fillNumbers()

    def clear(self):
        self.problem = [[0]*9 for i in range(9)]
        self.fillNumbers()

GUI()


