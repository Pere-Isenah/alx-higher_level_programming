#!/usr/bin/python3

def main():

    print_matrix_integer()


def print_matrix_integer(matrix=[[]]):
    # Iterate through each row in the matrix
    for row in matrix:
        # Print each cell in the row, separated by a space
        print(' '.join(['{:d}'.format(cell) for cell in row]))


if __name__ == "__main__":

    main()
