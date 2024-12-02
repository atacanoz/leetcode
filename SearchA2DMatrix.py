class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowRight = len(matrix) - 1
        rowLeft = 0

        colRight = len(matrix[0]) - 1
        colLeft = 1

        while rowLeft <= rowRight:
            rowMid = (rowRight + rowLeft) // 2

            if matrix[rowMid][0] == target:
                return True
        
            elif matrix[rowMid][0] > target:
                rowRight = rowMid - 1

            else: 
                rowLeft = rowMid + 1

        while colLeft <= colRight:

            colMid = (colRight + colLeft) // 2

            if matrix[rowRight][colMid] == target:
                return True
        
            elif matrix[rowRight][colMid] > target:
                colRight = colMid - 1

            else:
                colLeft = colMid + 1
    
        return False

       
