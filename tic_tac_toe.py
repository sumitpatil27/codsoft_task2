import math

board = [' ']*9

def show_board():
    print()
    for i in range(0,9,3):
        print(board[i], '|', board[i+1], '|', board[i+2])
        if i < 6:
            print("---------")

def winner(p):
    win = [(0,1,2),(3,4,5),(6,7,8),
           (0,3,6),(1,4,7),(2,5,8),
           (0,4,8),(2,4,6)]
    return any(board[a]==board[b]==board[c]==p for a,b,c in win)
    


def draw():
    return ' ' not in board

def minimax(ai_turn):
    if winner('O'): return 1
    if winner('X'): return -1
    if draw(): return 0

    scores = []
    for i in range(9):
        if board[i]==' ':
            board[i] = 'O' if ai_turn else 'X'
            scores.append(minimax(not ai_turn))
            board[i] = ' '
    return max(scores) if ai_turn else min(scores)

def ai_play():
    best = -math.inf
    move = 0
    for i in range(9):
        if board[i]==' ':
            board[i]='O'
            score = minimax(False)
            board[i]=' '
            if score > best:
                best = score
                move = i
    board[move]='O'

print("Tic-Tac-Toe (You = X, AI = O)")

while True:
    show_board()
    pos = int(input("Enter position (0-8): "))

    if board[pos] != ' ':
        print("Invalid move!")
        continue

    board[pos] = 'X'

    if winner('X'):
        show_board()
        print(" You win ")
        break

    if draw():
        show_board()
        print("It's a draw ")
        break

    ai_play()

    if winner('O'):
        show_board()
        print("AI wins!")
        break
