from collections import defaultdict 

board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

cols = defaultdict(set)
rows = defaultdict(set)
squares = defaultdict(set) # key = (r/3 , c/3)


# for i in range(len(board)):
#     for k in range(len(board)):
#         if board[i][k] not in x and board[i][k] != ".":
#             x[k]=board[i][k]
#     rows[i] = x[k]


 
 
