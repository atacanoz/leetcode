# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.

# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true


matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3

def SearchMatrix(matrix, target):

    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] == target:
                return True
    return False    


res = SearchMatrix(matrix, target)

print(res)
