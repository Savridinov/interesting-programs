X = 'X'
O = 'O'
EMPTY = " "
TIE = 'Tie'
NUM_SQUARES = 9


def display_instruction():
    print(
        '''
        1 | 2 | 3
        ----------
        4 | 5 | 6 
        ----------
        7 | 8 | 9
        '''
    )


def ask_yes_no(question):
    response = None
    while response not in ('y', 'n'):
        response = input(question).lower()
    return response


def ask_number(question, low, high):
    response = None
    while response not in range(low, high):
        response = int(input(question)) - 1
    return response


def pieces():
    """Choice who's first move"""
    go_first = ask_yes_no('Whoud you take first move (y/n): ')
    if go_first == 'y':
        print('\nFine. You play with "X"')
        human = X
        computer = O
    else:
        print('\nhasdhshdaa')
        computer = X
        human = O
    return human, computer


def new_board():
    """Makes a clear new board"""
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board


def dislpay_board(board):
    """display playground"""
    print(f'\n\t {board[0]} | {board[1]} | {board[2]}')
    print(f'\t ---------')
    print(f'\t {board[3]} | {board[4]} | {board[5]}')
    print(f'\t ---------')
    print(f'\t {board[6]} | {board[7]} | {board[8]}')


def legal_moves(board):
    """makes a list of avialible moves"""
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves


def winner(board):
    """Winnable moves"""
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner

        if EMPTY not in board:
            return TIE
    return None


def human_move(board, human):
    """Takes human move"""
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number('Your turn. Choice one of (1-9)', 1, NUM_SQUARES)
        if move not in legal:
            print('\nFunny human this square is alredy taken\n')
    print('\nOK...')
    return move


def computer_moves(board, human, computer):
    """make move for computer"""
    # make a copy of board
    board = board[:]
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    print('OK i\'ll take a number', end=" ")
    for move in legal_moves(board):
        board[move] = human
        if winner(board) == computer:
            print(move)
            return move
        board[move] = EMPTY
    for move in legal_moves(board):
        print(move)
        return move


def next_turn(turn):
    if turn == X:
        return O
    else:
        return X


def congrat_the_winner(the_winner, human, computer):
    if the_winner != TIE:
        print(f'3 of {the_winner} is line\n')
    else:
        print('Tie!\n')
    if the_winner == computer:
        print('FATALITY')
    elif the_winner == human:
        print('Ohh that\'s bad')
    elif the_winner == TIE:
        print('Your lucky. Next time i\'ll show you')


def main():
    display_instruction()
    computer, human = pieces()
    turn = X
    board = new_board()
    dislpay_board(board)
    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_moves(board, human, computer)
            board[move] = computer
        dislpay_board(board)
        turn = next_turn(turn)
    the_winner = winner(board)
    congrat_the_winner(the_winner, human, computer)


if __name__ == '__main__':
    main()
