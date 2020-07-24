#!/bin/python3

import numpy as np

'''
Notes
implement cpu move and minimax
implement alpha beta pruning
'''

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
    while True:
        print(board)
        cpumove()
        if checkwin() == True:
            print(board)
            print("CPU Wins")
            break
        if checktie() == True:
            print(board)
            print("Tie. No winner.")
            break
        print(board)
        playermove()
        if checkwin() == True:
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
                return True
    #vertical
    for i in range(3):
        for j in range(7):
            if board[i][j] != "[ ]" and board[i][j] == board[i + 1][j] == board[i + 2][j] == board[i + 3][j]:
                return True
    #right diagonals
    for i in range(3):
        for j in range(4):
            if board[i][j] != "[ ]" and board[i][j] == board[i + 1][j + 1] == board[i + 2][j + 2] == board[i + 3][j + 3]:
                return True
    #left diagonals
    for i in range(3):
        for j in range(3, 7):
            if board[i][j] != "[ ]" and board[i][j] == board[i + 1][j - 1] == board[i + 2][j - 2] == board[i + 3][j - 3]:
                return True

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
    print("cpu move")

def minimax():
    print("minimax function")







if __name__ == '__main__':
    main() 