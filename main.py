board = [[' ',' ',' '], [' ',' ',' '], [' ',' ',' ']]

outcomes = {'X':1, 'tie':0, 'O':-1}

def printBoard():
    print('\n')
    print(' '+board[0][0]+' | '+board[0][1]+' | '+board[0][2]+' ')
    print('-----------')
    print(' '+board[1][0]+' | '+board[1][1]+' | '+board[1][2]+' ')
    print('-----------')
    print(' '+board[2][0]+' | '+board[2][1]+' | '+board[2][2]+' ')
    print('\n')

def playGame():
    moves = 0
    while checkWinner() == 0:
        bestM = calculateMove()
        move(bestM[1], bestM[0], 'X')
        printBoard()
        move(0, 0, 'O')
        moves += 1
    print('winner is ' + checkWinner())

def calculateMove():
    bestScore = -10000
    bestMove = {0, 0}
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                bestScore = max(minimax(0, 'O'), bestScore)
                bestMove = (i, j)
                board[i][j] = ' '
    return bestMove

def move(x, y, player):
    if player == 'O':
        x = int(input('Give Y: '))
        y = int(input('Give X: '))
    board[x][y] = player
    printBoard()

def minimax(depth, player):
    result = checkWinner()
    if result != 0:
        return outcomes[result]

    if player == 'X':
        bestScore = -10000
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    bestScore = max(minimax(depth + 1, 'O'), bestScore)
                    board[i][j] = ' '
        return bestScore
    else:
        bestScore = 10000
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    bestScore = min(minimax(depth + 1, 'X'), bestScore)
                    board[i][j] = ' '
        return bestScore

def checkWinner():

    # VERTICAL
    if board[0][0] == 'O' and board[1][0] == 'O' and board[2][0] == 'O':
        print('here1')
        return 'O'
    elif board[0][1] == 'O' and board[1][1] == 'O' and board[2][1] == 'O':
        print('here2')
        return 'O'
    elif board[0][2] == 'O' and board[1][2] == 'O' and board[2][2] == 'O':
        print('here3')
        return 'O'
    elif board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X':
        return 'X'
    elif board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X':
        return 'X'
    elif board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == 'X':
        return 'X'

    # HORIZONTAL
    if board[0][0] == 'O' and board[0][1] == 'O' and board[0][2] == 'O':
        return 'O'
    elif board[1][0] == 'O' and board[1][1] == 'O' and board[1][2] == 'O':
        return 'O'
    elif board[2][0] == 'O' and board[2][1] == 'O' and board[2][2] == 'O':
        return 'O'

    if board[0][0] == 'X' and board[0][1] == 'X' and board[0][2] == 'X':
        return 'X'
    elif board[1][0] == 'X' and board[1][1] == 'X' and board[1][2] == 'X':
        return 'X'
    elif board[2][0] == 'X' and board[2][1] == 'X' and board[2][2] == 'X':
        return 'X'

    # DIAGONAL
    if board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X':
        return 'X'
    elif board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X':
        return 'X'
    elif board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O':
        return 'O'
    elif board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O':
        return 'O'

    return 0

playGame()
