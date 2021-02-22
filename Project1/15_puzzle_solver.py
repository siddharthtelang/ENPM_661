#!/usr/bin/python3

# ========================================
# ENPM661 Spring 2021: Planning for Autonomous Robots
# Given a initial states of a 15 puzzle, reach the goal state
# Keep a track of parent nodes to back trace from goal to initial state
#
# Author: Siddharth Telang(stelang@umd.edu)
# ========================================
# Run as 'python3 15_puzzle_solver.py --case test5'
# To run other test cases, replace the argument of --case with the test case number

import argparse
import array
import copy
import numpy as np

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
    # child: array, its respective list/state, and generated by which move - left/right/up/down
    # parent: index, array and list/state form
    def __init__(self, arr, parent_index, parent_state):
        self.arr = arr # child array - store parent array for now ; it will be modified with movements of blank tile
        self.list = [] # child list
        self.parent_index = parent_index # parent index
        self.parent_arr = arr # parent array
        self.parent_state = parent_state # parent list/state form
        self.move = ''

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

# convert to string list
def convert2List(arr):
    a = (np.array(arr)).ravel()
    return [str(i) for i in a]

# define function to calculate path
def path(inital):

    toTest = convert2List(inital)

    # final goal state
    final = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','0']

    # convert final goal state and inital state to array
    final_arr = np.reshape(final, (4,4))
    toTest_arr = np.reshape(toTest, (4,4))

    # initialize queue which will store the nodes to be expanded. By default, store the test case state
    mainQueue = Queue()
    mainQueue.enque(toTest)

    # print the initial stage - list and array
    print('Initial Stage:')
    mainQueue.__print__()
    print(toTest_arr)
    print('\n')

    # define flag to set if goal reached and a count for number of expansions
    flag, count = 0, 0

    # define mainList which stores all the nodes expanded and append the test case
    mainList = []
    mainList.append(toTest)

    # define a list to back trace the goal state. This will hold all the object of nodes traversed
    backTrack = []

    print('Nodes derived from above parent till goal state:\n')
    # iterate till the main queue is not empty - till all nodes are traversed
    while(mainQueue.not_empty()):
        # deque top element
        list_node = mainQueue.deque()
        #print('\nDeque:')
        #print(list_node)
        arr = np.reshape(list_node, (4,4))
        # find the blank tile
        i, j = find_blank(arr)
        # create a parent node
        parent = Node(arr, count, list_node)
        # store the 1st parent node in back track list
        if count == 0:
            backTrack.append(parent)
        count += 1

        # fill in the parent node with blank tile coordinates for reference
        parent.set_blank_index(i,j)
        # find the moves that can be achieved from parent node
        moves = find_moves(i,j, parent)
        #print(moves)

        # iterate through each move and generate child array with actions - left, right, up, down
        for m in range(len(moves)):
            # child object stores array which will be modified with actions, count of parent index and parent list
            child = Node(arr, count, list_node)
            if (moves[m] == 'left'):
                child.arr = ActionMoveLeft(copy.deepcopy(parent))
            elif (moves[m] == 'right'):
                child.arr = ActionMoveRight(copy.deepcopy(parent))
            elif (moves[m] == 'up'):
                child.arr = ActionMoveUp(copy.deepcopy(parent))
            else:
                child.arr = ActionMoveDown(copy.deepcopy(parent))

            # create a list of child array
            child.make_list()

            # store the move
            child.move = moves[m]

            # if list is not in the main list add those details in main list and further add in database
            if (child.list not in mainList):
                child.print_list()
                # add object in back tracking list ; add child list in main list
                backTrack.append(child)
                mainList.append(child.list)

                # if child.list equals final list -> We have arrived at our solution
                if (child.list == final):
                    print('\nGot the final state\n')
                    print(child.list)
                    print(child.arr)
                    flag = 1
                    break

                # if goal is not reached, add child list to queue to be expanded
                mainQueue.enque(child.list)

        # if goal state is reached, display and break out
        if (flag == 1):
            #print('\n Main Node List = ')
            #print(mainList)
            print('\nLength of main node list = ' + str(len(mainList)))
            print('count of node expansions = ' + str(count))
            break

    # return the main node list and back track list
    return mainList, backTrack

# function to back trace the parent node from goal state
def backTrace(backTrack):
    track, parent_state, last_parent_index  = [], [], -1
    for i in reversed(range(len(backTrack))):
        if last_parent_index == backTrack[i].parent_index:
            continue
        if backTrack[i].list == final or backTrack[i].list == parent_state:
            last_parent_index = backTrack[i].parent_index
            parent_state = backTrack[i].parent_state
            track.insert(0,backTrack[i])

    # return the list of back tracked parents
    return track

if __name__ == '__main__':

    # initialize the cases
    test1 = [[1, 2, 3, 4],[ 5, 6,0, 8], [9, 10, 7, 12] , [13, 14, 11, 15]]
    test2 = [[1, 0, 3, 4],[ 5, 2, 7, 8], [9, 6, 10, 11] , [13, 14, 15, 12]]
    test3 = [[0, 2, 3, 4],[ 1,5, 7, 8], [9, 6, 11, 12] , [13, 10, 14, 15]]
    test4 = [[5, 1, 2, 3],[0,6, 7, 4], [9, 10, 11, 8] , [13, 14, 15, 12]]
    test5 = [[1, 6, 2, 3], [9,5, 7, 4], [0, 10, 11, 8] , [13, 14, 15, 12]]

    final = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','0']

    # parse the argument for test case
    parser = argparse.ArgumentParser()
    parser.add_argument('--case', type=str, default='test5', required=False)
    args = parser.parse_args()

    toTest = test5
    if args.case == 'test1': toTest = test1
    elif args.case == 'test2': toTest = test2
    elif args.case == 'test3':  toTest = test3
    elif args.case == 'test4':  toTest = test4

    # check if the test path is already at the goal state ; exit if this is the case
    if convert2List(toTest) == final:
        print('Already at goal state ; exit')
        exit()

    # find the path and get the traversed node list and back tracking list having details of all nodes
    mainList, backTrack = path(toTest)

    #back trace
    track = backTrace(backTrack)

    # print the trace and goal state ; save it in a file
    try:
        fout = open(args.case + '_back_trace_.txt', 'w')
    except:
        print('File can not be opened')
    print('\n')
    for i in range(len(track)):
        # print on terminal
        print(track[i].parent_arr)
        print('Move ',track[i].move, '\n')
        # write in a file
        fout.write('%s\n' %track[i].parent_arr)
        fout.write('Move %s\n\n' %track[i].move)
    print('Final: \n',track[-1].arr)
    fout.write('Final\n%s\n'%track[-1].arr)
    fout.close()

    # store all traversed nodes in file
    try:
        fout = open(args.case + '_nodes.txt', 'w')
    except:
        print('File can not be opened')
        exit()
    for line in mainList:
        fout.write('%s\n' %line)
    fout.close()
