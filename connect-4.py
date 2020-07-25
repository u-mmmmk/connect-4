#!/bin/python3

#minimax and alpha-beta pruning implemented to play connect 4 and always win.
import numpy as np

def main():
    print("Connect 4!")
    global board
    global player 
    global cpu
    global column
    board = np.array([["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "1"], 
                      ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "2"],
                      ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "3"],
                      ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "4"],
                      ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "5"],
                      ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "6"],
                      [" a ", " b ", " c ", " d ", " e ", " f ", " g ", " "]])
    column = {"a":0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6}
    player = input("Type 'X' to be X, or 'O' to be O. X will go first.\n").upper()
    if player == 'X':
        print("You are X.")
        player = "[X]"
        cpu = "[O]"
        print(board)
        playermove()
    elif player == 'O':
        print("You are O.")
        player = "[O]"
        cpu = "[x]"
    else:
        print("Invalid Character. \nComputer will move first.")
        player = "[O]"
        cpu = "[X]"
    while True:
        print(board)
        cpumove()
        if checkwin() != False:
            print(board)
            print("CPU Wins")
            break
        if checktie() == True:
            print(board)
            print("Tie. No winner.")
            break
        print(board)
        playermove()
        if checkwin() != False:
            print(board)
            print("You Win")
            break
        if checktie() == True:
            print(board)
            print("Tie. No winner.")
            break

def checkwin():
    #horizontal
    for i in range(6):
        for j in range(4):
            if board[i][j] != "[ ]" and board[i][j] == board[i][j + 1] == board[i][j + 2] == board[i][j + 3]:
                return board[i][j]
    #vertical
    for i in range(3):
        for j in range(7):
            if board[i][j] != "[ ]" and board[i][j] == board[i + 1][j] == board[i + 2][j] == board[i + 3][j]:
                return board[i][j]
    #right diagonals
    for i in range(3):
        for j in range(4):
            if board[i][j] != "[ ]" and board[i][j] == board[i + 1][j + 1] == board[i + 2][j + 2] == board[i + 3][j + 3]:
                return board[i][j]
    #left diagonals
    for i in range(3):
        for j in range(3, 7):
            if board[i][j] != "[ ]" and board[i][j] == board[i + 1][j - 1] == board[i + 2][j - 2] == board[i + 3][j - 3]:
                return board[i][j]

    return False

def checktie():
    count = 0
    for i in range(6):
        for j in range(7):
            if board[i][j] == "[ ]":
                return False
            else:
                count = count + 1
                if count == 42: #if the whole board is full then return True
                    return True
            
    return False

def checkspace(row, column):
    if board[row + 1][column] != "[ ]" and board[row][column] == "[ ]":
        return True 
    else:
        return False

def playermove():
    global board
    move = input("Your Move. Enter a square <column><row> ex: 'c2'").lower()
    try:
        if checkspace(int(move[1]) - 1,column[move[0]]) == True:
            board[int(move[1]) - 1][column[move[0]]] = player
        else:
            print("invalid move")
            playermove()
    except:
        print("invalid move")
        playermove()

def cpumove():
    global board
    alpha = -99999
    beta = 99999
    depth = 8
    print("cpu move")
    bestscore = -9999
    for i in range(5, 0 , -1):
        for j in range(6, 0, -1):
            if checkspace(i, j) == True:
                board[i][j] = cpu
                score = minimax(depth, alpha, beta, False)
                board[i][j] = "[ ]" #revert the baord back to normal
                if score > bestscore:
                    bestscore = score
                    row = i
                    column = j
    board[row][column] = cpu

def minimax(depth, alpha, beta, maximize):
    global board
    depth = depth - 1
    if checkwin() == cpu:
            return 4
    elif checkwin() == player:
        return -4
    elif checktie() == True:
        return 0
    elif depth == 0:
        return func_eval()
    
    if maximize == True: #if cpu turn
        maxscore = -9999
        for i in range(5, 0, -1): #find all open spaces
            for j in range(6, 0, -1):
                if checkspace(i, j) == True:
                    board[i][j] = cpu
                    score = minimax(depth, alpha, beta, False) #call minimax on open space
                    board[i][j] = "[ ]"
                    maxscore = max(maxscore, score) #find the maxevaluation
                    alpha = max(alpha, maxscore) #pruning
                    if alpha >= beta:
                         return maxscore
        return maxscore

    else: #if players turn
        minscore = 9999
        for i in range(5, 0, -1): #find all open spaces
            for j in range(6, 0, -1):
                if checkspace(i, j) == True:
                    board[i][j] = player
                    score = minimax(depth, alpha, beta, True) #call minimax on open space
                    board[i][j] = "[ ]"
                    minscore = min(minscore, score) #set minscore to smallest score
                    beta = min(beta, minscore) #pruning
                    if beta <= alpha:
                        return minscore
        return minscore

def func_eval():
    eval = 0 #eval is based on how close the position is to winning ex 3 in a row gives 2 points
    '''
    #eval the position for cpu
    #I'm not sure how much this helps or if it does.
    for i in range(6):
        for j in range(4):
            if board[i][j] == cpu: 
                if board[i][j] == board[i][j + 1]:
                    eval = eval + 1
                    if board[i][j + 1] == board[i][j + 2]:
                        eval = eval + 1
    #vertical
    for i in range(3):
        for j in range(7):
            if board[i][j] == cpu:
                if board[i][j] == board[i + 1][j]:
                    eval = eval + 1
                    if board[i + 1][j] == board[i + 2][j]:
                        eval = eval + 1
    #right diagonals
    for i in range(3):
        for j in range(4):
            if board[i][j] == cpu:
                if board[i][j] == board[i + 1][j + 1]:
                    eval = eval + 1
                    if board[i + 1][j + 1] == board[i + 2][j + 2]:
                        eval = eval + 1
    #left diagonals
    for i in range(3):
        for j in range(3, 7):
            if board[i][j] == cpu:
                if board[i][j] == board[i + 1][j - 1]:
                    eval = eval + 1
                    if board[i + 1][j - 1] == board[i + 2][j - 2]:
                        eval = eval + 1
    '''
    #penalize the position for how many pieces the player has in a row
    for i in range(6):
        for j in range(4):
            if board[i][j] == player: 
                if board[i][j] == board[i][j + 1]:
                    eval = eval - 1
                    if board[i][j + 1] == board[i][j + 2]:
                        eval = eval - 1
    #vertical
    for i in range(3):
        for j in range(7):
            if board[i][j] == player:
                if board[i][j] == board[i + 1][j]:
                    eval = eval - 1
                    if board[i + 1][j] == board[i + 2][j]:
                        eval = eval - 1
    #right diagonals
    for i in range(3):
        for j in range(4):
            if board[i][j] == player:
                if board[i][j] == board[i + 1][j + 1]:
                    eval = eval - 1
                    if board[i + 1][j + 1] == board[i + 2][j + 2]:
                        eval = eval - 1
    #left diagonals
    for i in range(3):
        for j in range(3, 7):
            if board[i][j] == player:
                if board[i][j] == board[i + 1][j - 1]:
                    eval = eval - 1
                    if board[i + 1][j - 1] == board[i + 2][j - 2]:
                        eval = eval - 1
    return eval

if __name__ == '__main__':
    main() 
