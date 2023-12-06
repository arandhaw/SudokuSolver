import ctypes
import os
import numpy as np

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

path = os.path.dirname(__file__) + "\\clibrary.so"   # filepath to c shared library
# open library
clibrary = ctypes.CDLL(path)   
# gcc -fPIC -shared -o clibrary.so sudoku.c to compile

def C_sudoku_solver(sudoku):
    # use command 
         
    # Define the function signature
    clibrary.solveSudoku.argtypes = [np.ctypeslib.ndpointer(dtype=np.int32, ndim=2, flags='C_CONTIGUOUS')]
    clibrary.solveSudoku.restype = ctypes.c_int
    # Create a NumPy array
    arr = np.array(sudoku, dtype=np.int32)
    # Call the C function with the NumPy array
    solved = clibrary.solveSudoku(arr)
    if solved == 0:
        return None
    return arr.tolist()

print(__file__)
print(os.path.dirname(__file__))