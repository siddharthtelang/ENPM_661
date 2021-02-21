#ENPM661 Project1

15 puzzle problem

Generate final state from given state

Test Case 1: [[1, 2, 3, 4],[ 5, 6,0, 8], [9, 10, 7, 12] , [13, 14, 11, 15]]

Test Case 2: [[1, 0, 3, 4],[ 5, 2, 7, 8], [9, 6, 10, 11] , [13, 14, 15, 12]]

Test Case 3: [[0, 2, 3, 4],[ 1,5, 7, 8], [9, 6, 11, 12] , [13, 10, 14, 15]]

Test Case 4: [[5, 1, 2, 3],[0,6, 7, 4], [9, 10, 11, 8] , [13, 14, 15, 12]]

Test Case 5: [[1, 6, 2, 3], [9,5, 7, 4], [0, 10, 11, 8] , [13, 14, 15, 12]]

Python version: 3
Libraries used: argparse, array, copy, numpy

Steps to run:

'python3 15_puzzle_solver.py --case <test_case_number>'

eg. To run test case 5:
python3 15_puzzle_solver.py --case test5

Same applies to other cases:
python3 15_puzzle_solver.py --case test1
python3 15_puzzle_solver.py --case test2
python3 15_puzzle_solver.py --case test3
python3 15_puzzle_solver.py --case test4

Output:

1) The Nodes traversed and Back tracking array would be printed directly on terminal

2) All the nodes traversed/expanded in a specific test case would be stored in a file of format:
<test case name>_nodes.txt
eg. test1_nodes.txt, test2_nodes.txt, test3_nodes.txt, test4_nodes.txt, test5_nodes.txt

3) The back trace list - initial point to goal state would be stored in a file of format:
<test case name>_back_trace_.txt
eg: test5_back_trace_.txt
