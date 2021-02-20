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
