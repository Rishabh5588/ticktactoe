board = ["_", "_", "_",
         "_", "_", "_",
         "_", "_", "_"]

game_still_going = True

winner = None

current_player = "X"

def  display_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])

def play_game():
    display_board()
    while game_still_going:
        handle_turn(current_player)
        check_if_game_over()
        flip_player()
    if winner == "X" or winner == "O":
        print(winner +"won.")
    elif winner == None:
        print("Tie.")

def handle_turn(player):
    print(player+"'s turn'")
    position = input("choose a position bwtween 1-9")
    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("invalid input.Choose within 1-9")
    
        position = int(position) - 1
        if board[position] == "_":
            valid = True
        else:
            print("you can't go there,GO AGAIN.")
    board[position] = player
    display_board()

def check_if_game_over():
    check_for_winner()
    check_if_tie()

def check_for_winner():
    global winner
    row_winner = check_row()
    column_winner = check_columns()
    diagnols_winner = check_diagnols()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagnols_winner:
        winner = diagnols_winner
    else:
        winner = None
    return

def check_row():
    global game_still_going
    
    row1 = board[0] == board[1] == board[2] != "_"
    row2 = board[3] == board[4] == board[5] != "_"
    row3 = board[6] == board[7] == board[8] != "_"
    if row1 or row2 or row3:
        game_still_going == False
    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]
    return

def check_columns():
    global game_still_going
    
    column1 = board[0] == board[3] == board[6] != "_"
    column2 = board[1] == board[4] == board[7] != "_"
    column3 = board[2] == board[5] == board[8] != "_"
    if column1 or column2 or column3:
        game_still_going == False
    if column1:
        return board[0]
    elif column2:
        return board[1]
    elif column3:
        return board[2]
    return

def check_diagnols():
    global game_still_going
    
    diagnol1 = board[0] == board[4] == board[8] != "_"
    diagnol2 = board[6] == board[4] == board[3] != "_"
    if diagnol1 or diagnol2:
        game_still_going == False
    if diagnol1:
        return board[0]
    elif diagnol2:
        return board[6]
    return

def check_if_tie():
    global game_still_going
    if "_" not in board:
        game_still_going = False
    return

def flip_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return

play_game()