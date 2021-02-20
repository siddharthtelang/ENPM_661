import numpy as np
import array
import copy

# define a Queue class for storing the nodes to be expanded
class Queue:

    # init function
    def __init__(self):
        self.queue = []

    # insert in queue
    def enque(self, item):
        self.queue.insert(0, item)

    # pop node
    def deque(self):
        if self.queue:
            return self.queue.pop()
        return 'Empty'

    # check if queue is not empty
    def not_empty(self):
        return (len(self.queue) > 0)

    # check if the queue contains a specific list item
    def contains(self, item):
        return (item in self.queue)

    # print the queue
    def __print__(self):
        print(self.queue)

# define a class Node for storing all nodes generated in puzzle with parent node info
class Node:

    # init function to store info about:
    # child: array, its respective list/state
    # parent: index, array and list/state form
    def __init__(self, arr, parent_index, parent_state):
        self.arr = arr # child array
        self.list = [] # child list
        self.parent_index = parent_index # parent index
        self.parent_arr = arr # parent array
        self.parent_state = parent_state # parent list/state form

    # store the index of the blank / zero block to find the moves
    def set_blank_index(self, i, j):
        self.i = i
        self.j = j

    # make list of character values from current child array
    def make_list(self):
        if (len(self.arr) > 0):
            a = self.arr.ravel()
            for i in a:
                self.list.append(i)

    # print the child list
    def print_list(self):
        print(self.list)

# function to find the blank/zero in the array
def find_blank(arr):
    coordinates = np.where(arr == '0')
    coordinates = list(zip(coordinates[0], coordinates[1]))
    return coordinates[0][0], coordinates[0][1]

# function to find the moves from the parent node
def find_moves(i, j, parent):
    moves = ['up', 'down', 'left', 'right']
    boundary = parent.arr.shape[0]
    if (j == 0):
        moves.remove('left')
    if (j == boundary-1):
        moves.remove('right')
    if (i == 0):
        moves.remove('up')
    if (i == boundary-1):
        moves.remove('down')
    return moves

# function to move the blank element to left and return the array
def ActionMoveLeft(node):
    arr = node.arr
    i, j = node.i, node.j
    arr[i][j], arr[i][j-1]  = arr[i][j-1], arr[i][j]
    return arr

# function to move the blank element to right and return the array
def ActionMoveRight(node):
    i, j = node.i, node.j
    arr = node.arr
    arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
    return arr

# function to move the blank element up and return the array
def ActionMoveUp(node):
    i, j = node.i, node.j
    arr = node.arr
    arr[i][j], arr[i-1][j] = arr[i-1][j], arr[i][j]
    return arr

# function to move the blank element down and return the array
def ActionMoveDown(node):
    i, j = node.i, node.j
    arr = node.arr
    arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
    return arr

# define main class
def main():
    # initialize the cases
    test1 = ['1','2','3','4','5','6','0','8','9','10','7','12','13','14','11','15']
    test2 = ['1','0','3','4','5','2','7','8','9','6','10','11','13','14','15','12']
    test3 = ['0','2','3','4','1','5','7','8','9','6','11','12','13','10','14','15']
    test4 = ['5','1','2','3','0','6','7','4','9','10','11','8','13','14','15','12']
    test5 = ['1','6','2','3','9','5','7','4','0','10','11','8','13','14','15','12']

    # NOTE: below variable needs to be modified if test case changes, eg. toTest = test5 if test case 5 is to be checked
    toTest = test5

    # final goal
    final = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','0']

    # convert final goal state and inital state to array
    final_arr = np.reshape(final, (4,4))
    toTest_arr = np.reshape(toTest, (4,4))

    # initialize queue which will store the nodes to be expanded. By default, store the test case state
    mainQueue = Queue()
    mainQueue.enque(toTest)

    # print the initial stage
    mainQueue.__print__()
    print(toTest_arr)

    # define flag to set if goal reached and a count for number of expansions
    flag, count = 0, 0

    # define mainList which stores all the nodes expanded and append the test case
    mainList = []
    mainList.append(toTest)

    # define a list to back trace the goal state. This will hold all the object of nodes traversed
    backTrack = []
