# Python3 program to print given matrix in spiral form


def spiralMatrix(m, n, mat):
    k = 0
    l = 0

    ''' k - starting row index 
        m - ending row index 
        l - starting column index 
        n - ending column index 
    '''

    while k < m and l < n:

        # Print the first row from the remaining rows
        for i in range(l, n):
            print(mat[k][i], end=" ")

        k += 1

        # Print the last column from the remaining columns
        for i in range(k, m):
            print(mat[i][n - 1], end=" ")

        n -= 1

        # Print the last row from the remaining rows
        if k < m:

            for i in range(n - 1, l - 1, -1):
                print(mat[m - 1][i], end=" ")

            m -= 1

        # Print the first column from the remaining columns
        if l < n:
            for i in range(m - 1, k - 1, -1):
                print(mat[i][l], end=" ")

            l += 1


# Matrix
a = [[1, 2, 3, 4, 5, 6],
     [7, 8, 9, 10, 11, 12],
     [13, 14, 15, 16, 17, 18],
     [19, 20, 21, 22, 23, 24]]

row = 4
column = 6
spiralMatrix(row, column, a)
