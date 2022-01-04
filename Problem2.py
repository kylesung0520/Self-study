# leetcode problem
# Implement the class SubrectangleQueries which receives a rows x cols rectangle as a matrix of integers in the constructor and supports two methods:

# 1. updateSubrectangle(int row1, int col1, int row2, int col2, int newValue)
# Updates all values with newValue in the subrectangle whose upper left coordinate is (row1,col1) and bottom right coordinate is (row2,col2).

# 2. getValue(int row, int col)
# Returns the current value of the coordinate (row,col) from the rectangle.

class SubrectangleQueries:

    def __init__(self, rectangle):
        self.rec = rectangle

    def updateSubrectangle(self, row1, col1, row2, col2, newValue):
        # create new array which contains the "newValue" with the size based on the given col1 and col2
        tmp = [newValue] * (col2 - col1 + 1)

        # update given rectangle in range of given rows and cols by using "tmp" array
        for i in range(row1, row2 + 1):
            self.rec[i][col1:col2 + 1] = tmp

    def getValue(self, row, col):
        return self.rec[row][col]