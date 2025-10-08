# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Maximus Amick
#               Daniel Yoo
#               Caleb Carter
#               Noah Kim
# Section:      513
# Assignment:   Lab: Topic 7 (Team)
# Date:         8 September 2025

board = [list("." * 9) for _ in range(9)]

def print_board():
    for row in board:
        # print each cell in the row separated by a space
        print(" ".join(row))

black_turn = True

is_running = True

print_board()

while is_running == True:
    if not any("." in row for row in board):
        print("GAME OVER!")
        is_running = False
    else:
        if black_turn == True:
            print("BLACK'S TURN")
        else:
            print("WHITE'S TURN")
        input_row = int(input('\nEnter the row you would like to place your chip at (0-8): '))
        input_column = int(input('\nEnter the column you would like to place your chip at (0-8): '))
        if board[input_row][input_column] != ".":
            print("You can't park there")
            is_running = False
        else:
            if black_turn == True:
                board[input_row][input_column] = "X"
            else:
                board[input_row][input_column] = "O"
            black_turn = not black_turn
            print_board()