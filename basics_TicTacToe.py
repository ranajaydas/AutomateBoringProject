"""Simple game of tic-tac-toe."""

theBoard = {'1': ' ', '2': ' ', '3': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '7': ' ', '8': ' ', '9': ' '}
game_over = False
whose_turn = 'X'
all_possible_moves = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
all_previous_moves = set()


def printboard(board: dict) -> None:
    """Prints an empty board."""
    print()
    print('{}|{}|{}\t\t1|2|3'.format(board['1'], board['2'], board['3']))
    print('-+-+-\t\t-+-+-')
    print('{}|{}|{}\t\t4|5|6'.format(board['4'], board['5'], board['6']))
    print('-+-+-\t\t-+-+-')
    print('{}|{}|{}\t\t7|8|9'.format(board['7'], board['8'], board['9']))
    print()


def checkwinner(board: dict) -> None:
    """Checks for a winner."""
    check_rows = board['1'] == board['2'] == board['3'] != ' ' or \
                 board['4'] == board['5'] == board['6'] != ' ' or \
                 board['7'] == board['8'] == board['9'] != ' '

    check_cols = board['1'] == board['4'] == board['7'] != ' ' or \
                 board['2'] == board['5'] == board['8'] != ' ' or \
                 board['3'] == board['6'] == board['9'] != ' '

    check_diags = board['1'] == board['5'] == board['9'] != ' ' or \
                  board['3'] == board['5'] == board['7'] != ' '

    if check_rows or check_cols or check_diags:
        declarewinner()


def declarewinner():
    """Declares who the winner is."""
    global game_over
    global whose_turn
    print('The winner is:', whose_turn)
    game_over = True


def checkdraw():
    """Checks for draws."""
    if all_possible_moves == all_previous_moves:
        print("It's a draw!")
        global game_over
        game_over = True


def flipturn():
    """Flips the turn between 'X' and 'O'."""
    global whose_turn
    if whose_turn == 'X':
        whose_turn = 'O'
    else:
        whose_turn = 'X'


# Start of program
printboard(theBoard)
while not game_over:
    coordinate = input("It is {}'s turn. Please enter a move on the board [1-9]: ".format(whose_turn))

    while True:
        if coordinate not in all_possible_moves or coordinate in all_previous_moves:
            coordinate = input('Not a valid move. Please try again, player {}: '.format(whose_turn))
        else:
            all_previous_moves.add(coordinate)
            break

    theBoard[coordinate] = whose_turn
    printboard(theBoard)
    checkwinner(theBoard)
    checkdraw()
    flipturn()
