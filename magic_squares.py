import math
import time

import numpy as np


class MagicSquare:
    def __init__(self, size):
        assert size > 0, "Number must be an odd positive integer"
        assert size % 2 > 0, "Number must be odd"
        self.size = size
        self.matrix = np.zeros(shape=(size, size))
        self.row = 0
        self.column = int((self.size - 1) / 2)
        self.counter = 1
        self.matrix[self.row][self.column] = self.counter
        self.total_sum = (math.pow(self.size, 3) + self.size) / 2

    def is_correct(self):
        """
        This method check if all the conditions sum are equals
        :return: boolean
        """

        # Sum the main diagonal
        main_diagonal_sum = np.sum(self.matrix.diagonal())

        # Sum the inverse diagonal
        inverse_diagonal_sum = np.sum(np.fliplr(self.matrix).diagonal())

        # Sum row axis items
        rows_axis_sum = self.matrix.sum(axis=0)
        # Sum column axis items
        columns_axis_sum = self.matrix.sum(axis=1)

        # Check if all sums are equal
        return main_diagonal_sum == inverse_diagonal_sum == self.total_sum \
               and np.all(rows_axis_sum == self.total_sum) and np.all(columns_axis_sum == self.total_sum)

    def mat_print(self):
        """
        Pretty print for the matrix
        """
        col_maxes = [max([len("{:g}".format(x)) for x in col]) for col in self.matrix.T]
        for x in self.matrix:
            for i, y in enumerate(x):
                print(("{:" + str(col_maxes[i]) + "g}").format(y), end=" ")
            print("")

    def build(self):
        """
        Build step by step the magic square
        :return:
        """
        if self.size == 1:
            self.mat_print()
            print('-' * 50)
            print("Correct: {}".format(self.is_correct()))
            return

        print('-' * 50)

        while np.count_nonzero(self.matrix) < (self.size * self.size):
            self.counter += 1
            # First condition, if the cell is upper of the matrix
            if (self.row - 1) == -1 and (self.column + 1) < self.size:
                self.row = self.row - 1 + self.size
                self.column = self.column + 1
            # Second condition, if the cell is right of the matrix
            elif (self.row - 1) >= 0 and (self.column + 1) == self.size:
                self.column = self.column + 1 - self.size
                self.row = self.row - 1
            # Third case, if the cell is busy or outside in the diagonal
            elif (self.row - 1) == -1 and (self.column + 1) == self.size or self.matrix[self.row - 1][self.column + 1]:
                self.row += 1
            else:
                self.row = self.row - 1
                self.column = self.column + 1

            self.matrix[self.row][self.column] = self.counter

            self.mat_print()

            print('-' * 50)

            time.sleep(1)

        print("Correct: {}".format(self.is_correct()))


if __name__ == "__main__":
    n = -1

    while n < 0 or (n % 2) == 0:
        n = input("Please insert and odd positive integer to build the magic square: ")

        try:
            n = int(n)
        except ValueError:
            print("Must be a number")
            n = -1
        else:
            if n < 0:
                print("Error, the number must be positive")

            elif n % 2 == 0:
                print("Error, the number must be odd")

    magic_square = MagicSquare(n)
    magic_square.build()
