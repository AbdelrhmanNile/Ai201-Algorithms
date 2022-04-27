import os

#board = {1:' ', 2:' ', 3:' ',
#         4:' ', 5:' ', 6:' ',
#         7:' ', 8:' ', 9:' '}



board = {1:' ', 2:'X', 3:' ',
         4:'O', 5:' ', 6:'X',
         7:'O', 8:'O', 9:'X'}


def drawBoard(board):
    for key in board:
        if key % 3 == 0:
            print(board[key] + '\n')
        else:
            print(board[key] + ' | ', end='')
    print("+++++++++++++++")

def isEmpty(pos):
    if board[pos] == ' ':
        return True
    else:
        return False

def checkDraw():
    for key in board:
        if board[key] == ' ':
            return False
    return True

def checkWin():
    if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
        return True
    else:
        return False

def checkWinMark(mark):
    if (board[1] == board[2] and board[1] == board[3] and board[1] == mark):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] == mark):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] == mark):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == mark):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == mark):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] == mark):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == mark):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] == mark):
        return True
    else:
        return False

def insertPos(letter, pos):
    if isEmpty(pos):
        board[pos] = letter;
        #os.system('clear')
        drawBoard(board)

        

        if(checkWin()):
            if letter == 'X':
                print("Ai wins")
                exit()
            else:
                print("player wins")
                exit()
        if(checkDraw()):
            print("IT IS DRAW!")
            exit()
        return
    else:
        print("posutuon is not empty")
        pos = int(input("enter another position: "))
        insertPos(letter, pos)
        return


def minimax(board, depth, isMaximizing):
    if(checkWinMark(ai)):
        return 100
    elif(checkWinMark(player)):
        return -100
    elif(checkDraw()):
        return 0

    if(isMaximizing):
        bestScore = -1000

        for key in board:
            if(board[key]==' '):
                board[key] = ai
                score = int(minimax(board, 100, False))
                drawBoard(board) ## for debugging and seeing the tree
                board[key] = ' '
                if(score > bestScore):
                    bestScore = score
        return bestScore

    else:
        bestScore = 1000

        for key in board:
            if(board[key]==' '):
                board[key] = player
                score = int(minimax(board, 100, True))
                #drawBoard(board)
                board[key] = ' '
                if(score < bestScore):
                    bestScore = score
        return bestScore




ai = 'X'
player = 'O'

def playerMove():
    pos = int(input("enter position: "))
    insertPos(player, pos)
    return

def aiMove():
    bestScore = -1000
    bestMove = 0

    for key in board:
        if(board[key]==' '):
            board[key] = ai
            score = int(minimax(board, 100, False))
            #drawBoard(board)
            board[key] = ' '
            if(score > bestScore):
                bestScore = score
                bestMove = key

    insertPos(ai, bestMove)
    return

while not checkWin():
    aiMove()
    playerMove()


