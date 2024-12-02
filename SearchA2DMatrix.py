# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.

# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true


matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3

def BinarySearchMatrix(matrix, target):
    rowRight = len(matrix) - 1
    rowLeft = 0

    colRight = len(matrix[0]) - 1
    colLeft = 1

    while rowLeft <= rowRight:
        rowMid = (rowRight + rowLeft) // 2

        if matrix[rowMid][0] == target:
            return [rowMid,0]
        
        elif matrix[rowMid][0] > target:
            rowRight = rowMid - 1

        else: 
            rowLeft = rowMid + 1

    while colLeft <= colRight:

        colMid = (colRight + colLeft) // 2

        if matrix[rowRight][colMid] == target:
            return [rowRight, colMid]
        
        elif matrix[rowRight][colMid] > target:
            colRight = colMid - 1

        else:
            colLeft = colMid + 1
    
    return False


y = BinarySearchMatrix(matrix,target)        

print(y)


