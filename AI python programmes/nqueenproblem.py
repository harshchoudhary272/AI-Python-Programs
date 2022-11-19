global N
N = int(input("Enter the value of matrix"))
j=0
#N = int(input("Enter the value of the matrix"))

def printSol(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j],end = " ")
        
        print(" ") 

def isSafe(board,row,col):
    for i in range(col):
        if board[row][i] == 'Q':
            return False

    for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
        if board[i][j] == 'Q':
            return False

    for i,j in zip(range(row,N,1),range(col,-1,-1)):
        if board[i][j] == 'Q':
            return False
    return True
 
def solveNQtill(board,col):
    if col>=N:
        return True

    for i in range(N):
        if isSafe(board,i,col):
            board[i][col] = 'Q'

            if solveNQtill(board,col+1) == True:
                return True

            board[i][col] = 0
    return False

def solveNQ():
    board = [[0,0,0,0,0],
             [0,0,0,0,0],
             [0,0,0,0,0],
             [0,0,0,0,0],
             [0,0,0,0,0]
             ]
    if solveNQtill(board,0) == False:
        print("Solution does not exist")
        return False
    printSol(board)
    return True

solveNQ()
