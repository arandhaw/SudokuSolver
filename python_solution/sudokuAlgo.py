
import numpy as np
import copy

# Most important method is findSolution

# return list of unfilled squares as (x, y) pairs
def getNodeList(problem):
    nodes = []
    for i in range(9):
        for j in range(9):
            if problem[i, j] == 0:
                nodes += [(i, j)]
    return nodes

# used to optimize order of nodelist
def optimizer(point, sudoku):
    cell = np.array(point)//3
    x = np.count_nonzero( sudoku[point[0],:] ) 
    y = np.count_nonzero( sudoku[:,point[1]] )
    z = np.count_nonzero( sudoku[3*cell[0]:3*cell[0]+3 , 3*cell[1]:3*cell[1]+3])
    return x + y + z

#returns true if a contradiction is found for a value being in a certain position
def contradiction(num, px, py, sudoku):
    for i in range(9):
        if num == sudoku[px][i]:
            return True
        if num == sudoku[i][py]:
            return True
        if num == sudoku[3*(px//3) + i//3][3*(py//3) + i%3]:
            return True
    return False

# recursive helper function
def recurse(state, nodelist, depth = 0):
    px, py = nodelist[depth]
    for i in range(1, 10):
        if contradiction(i, px, py, state):  # try something else if contradiction found
            continue
        elif depth == len(nodelist) - 1:    # if sudoku filled, end recursion
            state[px][py] = i
            return True
        else:
            state[px][py] = i
            if recurse(state, nodelist, depth = depth + 1):
                return True
            else:
                state[px][py] = 0       # backtrack if recursion fails
    return False    # no possible solution
        

def findSolution(problem):
    problem = copy.deepcopy(problem)
    nodelist = getNodeList(np.array(problem))
    nodelist = sorted(nodelist, key=lambda x: optimizer(x, np.array(problem)), reverse = True)
    foundSolution = recurse(problem, nodelist)
    if foundSolution == True:
        return problem
    else:
        return None