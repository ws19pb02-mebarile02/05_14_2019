"""
tictactoe.py

This program accepts a tictactoe board configuration from the user and determines if
it is a winner.  It protects against incorrect input and the possibiity of both X and O
winning, but it does not protect against a configuration where either X or O have multiple
winning combinations on the same board, so that needs to be worked out.  An example:
XXX
XXX
XOX
"""


import sys

while True:

    try: 
        row1 = input('Enter row 1: ')      # accepts row input from user 
        row2 = input('Enter row 2: ')
        row3 = input('Enter row 3: ')
    except EOFError:   
        sys.exit(0)

    board = row1 + row2 + row3
        
    xo = ['x','o',' ']

    """
    checks to see if board is string of length 9 containing only x,o and whitespace
    """
    
    if isinstance(board,str) and len(board) == 9:  
        board = board.lower()
        for j in board:
            if j not in xo:
                print('Illegal input. Only X, O and whitespace!')
                break

    else:
        print('Enter a string of length 3 for each row! ')
            
    count = 0
    temp = []

    # determines if there is a winning configuration
    
    for i in xo[:2]:
        if 3*i in board[:3] or 3*i in board[3:6]\
        or 3*i in board[6:9] or 3*i in board[:8:3]\
        or 3*i in board[1:9:3] or 3*i in board[2::3]\
        or 3*i in board[::4] or 3*i in board[2:7:2]:
            count += 1
            temp.append(i)
    
    # prints results
    
    if count == 2:
        print("X and O can't both win!  Try again.")
    elif count == 1:
        print(f"{temp[0].upper()} wins!")
        break
    else:
        print("Not a winner.")
              
sys.exit(0)
    
                


    
