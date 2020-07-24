#!/bin/python3
import numpy as np


def main():
    board = np.array([[0, 1],
                      [2, 3]])
    print(board[1][0])

    dict = {"a1":board[0][0]}

    print(dict["a1"])

    string = "P23456"

    print(string[0])
if __name__ == '__main__':
    main() 