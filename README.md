# SudokuSolver
Sudoku solver and GUI written in python. 

The algorithm is a depth first search written with recursion (see sudokuAlgo.py).
The GUI was made using Tkinter, and allows entry of numbers by clicking and typing.

My original solution used python, but ran into performance issues when solving difficult sudoku's.
My new solution has the algorithm implemented in C, and only the GUI in python. The ctypes library is used
to communicate between them. 

To try it out, run the file sudokuSolver.py in either folder.

<img width="371" alt="image" src="https://github.com/arandhaw/SudokuSolver/assets/72634664/b214edc4-3b37-4678-b1ef-0ad27f2929d9">
