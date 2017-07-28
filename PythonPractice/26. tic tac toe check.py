''' make tic tac toe
'''
import numpy as np

gameover = False

board = np.arange(2,20,2).reshape(3,3)
for a in board:
    a = ''
turncount = 0

def reset():
    gameover = False
    for a in board:
        a = ''

while gameover == False:
       print("0 goes first")
       winner = False
       player = 0
       while turncount < 9 and winner == False:
           print("take turn:")
           row = int(input())
           collum = int(input())
           if board[row][collum] == 0 or board[row][collum] == 1:
               print("enter unpicked space")
               StopIteration
           else:
               board[row-1][collum-1] = player
           if player == 0:
               player = 1
           else:
               player = 0
           print(board)
           turncount += 1
           if board[1][1] == 1:
               if board[1][0] == 1 and board[1][2] == 1:
                   print('1 wins')
                   gameover == True
       if turncount == 9 and gameover == False:
           print("It's a tie")
           gameover == True



















