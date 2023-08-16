#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Create a new matrix to store squared values
    squared_matrix = []

    # Iterate through each row in the original matrix
    for row in matrix:
        squared_row = []
        # Iterate through each element in the row and square the value
        for num in row:
            squared_row.append(num * num)
            squared_matrix.append(squared_row)

            return (squared_matrix)
