import random


def reverse_list(l:list):

    """

    TODO: Reverse a list without using any built in functions

 

    The function should return a sorted list.

    Input l is a list which can contain any type of data.

    """

    n = len(l)
    for i in range(n//2):
        l[i], l[n-i-1] = l[n-i-1], l[i]
        # print(i,l)
    return l


 

def solve_sudoku(matrix):

    """

    TODO: Write a programme to solve 9x9 Sudoku board.

 

    Sudoku is one of the most popular puzzle games of all time. The goal of Sudoku is to fill a 9×9 grid with numbers so that each row, column and 3×3 section contain all of the digits between 1 and 9. As a logic puzzle, Sudoku is also an excellent brain game.

 

    The input matrix is a 9x9 matrix. You need to write a program to solve it.

    """
    def is_valid(matrix, row, col, num):
        for i in range(9):
            if matrix[row][i] == num or matrix[i][col] == num:
                return False
        start_row, start_col = row // 3 * 3, col // 3 * 3
        for i in range(3):
            for j in range(3):
                if matrix[start_row + i][start_col + j] == num:
                    return False
        return True

    def backtrack(matrix, row, col):
        if col == 9:
            return backtrack(matrix, row + 1, 0)
        if row == 9:
            return True
        if matrix[row][col] != 0:
            return backtrack(matrix, row, col + 1)
        for num in range(1, 10):
            if is_valid(matrix, row, col, num):
                matrix[row][col] = num
                if backtrack(matrix, row, col + 1):
                    return True
                matrix[row][col] = 0
        return False

    if not matrix:
        return None
    backtrack(matrix, 0, 0)
    return matrix

   
if __name__ == '__main__':
    print('#reverse_list')
    print(reverse_list(["1",2,3,4,5]))

    print()
    
    print('#solve_sudoku')
    #solve_sudoku
    matrix = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    for a in solve_sudoku(matrix):
        print(a)
   