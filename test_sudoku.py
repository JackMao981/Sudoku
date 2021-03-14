from solve_sudoku import *
import pytest

def assert_true(fills):
    result, solved = solve_sudoku(G,a,fills)
    try:
        assert check_sudoku(solved) == True
        print("It worked, this Sudoku is correctly solved")
    except AssertionError:
        print("It failed, this Sudoku is colored incorrectly")

def assert_false(fills):
    result, solved = solve_sudoku(G,a,fills)
    try:
        assert check_sudoku(solved) == False
        print("As expected, this Sudoku cannot be solved")
    except AssertionError:
        print("It failed, this Sudoku should not be solvable")

def test_full(a):
    '''
    Tests if a fully solved Sudoku will be True
    '''
    # fully filled -- true
    fills = [8,2,7,1,5,4,3,9,6,
            9,6,5,3,2,7,1,4,8,
            3,4,1,6,8,9,7,5,2,
            5,9,3,4,6,8,2,7,1,
            4,7,2,5,1,3,6,8,9,
            6,1,8,9,7,2,4,3,5,
            7,8,6,2,3,5,9,1,4,
            1,5,4,7,9,6,8,2,3,
            2,3,9,8,4,1,5,6,7]
    print("full:")
    assert_true(fills)

def test_partial(a):
    '''
    Tests if a partially filled Sudoku will return True
    '''
    # presets -- True
    fills = [0,0,0,4,0,0,0,0,0,
            4,0,9,0,0,6,8,7,0,
            0,0,0,9,0,0,1,0,0,
            5,0,4,0,2,0,0,0,9,
            0,7,0,8,0,4,0,6,0,
            6,0,0,0,3,0,5,0,2,
            0,0,1,0,0,7,0,0,0,
            0,4,3,2,0,0,6,0,5,
            0,0,0,0,0,5,0,0,0]
    print("partial:")
    assert_true(fills)

def test_empty(a):
    '''
    Tests if an empty one will be solved and return True
    '''
    # empty
    fills = [0] * 81
    print("empty:")
    assert_true(fills)

def test_not_feasible(a):
    '''
    Tests a partially filled one that will not have a feasible solution
    '''
    # presets -- that is not a soln
    fills = [0,0,0,4,4,0,0,0,0,
            4,0,9,0,0,6,8,7,0,
            0,0,0,9,0,0,1,0,0,
            5,0,4,0,2,0,0,0,9,
            0,7,0,8,0,4,0,6,0,
            6,0,0,0,3,0,5,0,2,
            0,0,1,0,0,7,0,0,0,
            0,4,3,2,0,0,6,0,5,
            0,0,0,0,0,5,0,0,0]
    print("not feasible:")
    assert_false(fills)

if __name__ == "__main__":
    a = 3.0
    G = create_sudoku(a)

    test_full(a)
    test_partial(a)
    test_empty(a)
    test_not_feasible(a)
    print("All tests finished")
