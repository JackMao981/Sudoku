# Sudoku
Advanced Algorithms: Sudoku Solver

This repo is for Lab 1 of the course Advanced Algorithms: Proving Sudoku is NP-complete. In our report, we walked through a proof where k-colorability is NP-complete, and that converting a n x n Sudoku board (where n represents a unit of the board) to a graph format, Sudoku can be colored in n colors, and therefore, is NP-complete.

Our code is the implementation of our proof and creates a graph representation of a 9 x 9 Sudoku board. By proving this graph is 9-colorable, this Sudoku game can be satisfied since each of the nine colors represent a number from 1 through 9.

### Prerequisites
We use the `networkx` function to set up the Sudoku graph and to easily retrieve the neighbors of each of the nodes.

### Running the code
To run the main program:
`python solve_sudoku.py`

To run the test cases:
`python test_sudoku.py`
