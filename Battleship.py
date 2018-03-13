from random import randint

board = []
boardx = []

for x in range(5):
  board.append(["O"] * 5)
  boardx.append(["O"]*5)

def print_board(board):
    print("---board---")
    for row in board:
        print (" ".join(row))

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

ship_rowx = random_row(board)
ship_colx = random_col(board)

turn = 0
point_playerone = 0
point_playertwo = 0
while (True):
    for turn in range(4):
##        print (ship_row+1)
##        print (ship_col+1)
        print("Player one guess")
        guess_row = int(input())-1
        guess_col = int(input())-1
        if guess_row == ship_row and guess_col==ship_col:
            print ("Congratulations! You sank my battleship! Player one wins")
            point_playerone+=1
            board[guess_row][guess_col] = "X"
            print_board(board)
            break
        elif board[guess_row][guess_col]=="X":
            print ("You guessed that one already.")
        else:
            if guess_row not in range(5) or guess_col not in range(5):
              print("Oops, that's not even in the ocean.")
            else:
              print ("You missed my battleship!")

##        print (ship_rowx+1)
##        print (ship_colx+1)
        print("Player Two guess")
        guess_rowx = int(input())-1
        guess_colx = int(input())-1
        if guess_rowx == ship_rowx and guess_colx==ship_colx:
            print ("Congratulations! You sank my battleship! Player two wins")
            point_playertwo+=1
            boardx[guess_rowx][guess_colx] = "X"
            print_board(boardx)
            break
        elif board[guess_rowx][guess_colx]=="X":
            print ("You guessed that one already.")
        else:
            if guess_rowx not in range(5) or guess_colx not in range(5):
              print("Oops, that's not even in the ocean.")
            else:
              print ("You missed my battleship!")
        if turn==3:
            print ("Game Over")
        print_board(boardx)
        print("turn: %d"%(turn+1))
    answer = input("Would you like to play again? 1 for yes, anything else for no")
    print("Player one has: %s points" %(point_playerone))
    print("Player two has: %s points" %(point_playertwo))
    if(answer!="1"):
        break
    ship_row = random_row(board)
    ship_col = random_col(board)
    ship_rowx = random_row(board)
    ship_colx = random_col(board)

