# Created by taka the 05-12-2021 at 11:57

f = open('./input.txt', 'r')
lines = f.readlines()


def get_boards(boards_data):
    '''
    get all the boards from the input.txt file
    :param boards_data: list, lines of the input.txt file
    :return: boards_list : list of all the boards from input file
    '''
    boards_list = []
    board = []
    for l in boards_data:
        l_format = l.strip('\n')
        # if the line is '', the current board is complete, we add it to the list
        # and we create a new board
        if l_format == '':
            boards_list.append(board)
            board = []
            continue
        # add a list to board which is the number of the line
        board.append([l_format[i:i+2].strip() for i in range(0, len(l_format), 3)])

    return boards_list


def mark_board(boards, number):
    '''
    Mark the drawn number on all boards, by replacing it with ''
    :param boards: list, all the boards
    :param number: string, the drawn number of the round
    :return: marked_boards, list, all the boards marked
    '''
    marked_boards = []
    for board in boards:
        marked_boards.append([[el if el != number else '' for el in l] for l in board])

    return marked_boards


def any_board_winner(boards_info):
    '''
    Determine if a board has bingo (any row or any column fully marked)
    :param boards_info:
    :return: tuple(Boolean, list) : True and the board if a board has won
                                    False and None otherwise
    '''
    for b in boards_info:
        # if any row or any column is fully marked
        if any(l == ['', '', '', '', ''] for l in b) or \
                any([el[i] for el in b] == ['', '', '', '', ''] for i in range(5)):
            return True, b
    return False, None


def winning_score(board, winning_numb):
    '''

    :param board: list, board to get the winning score of
    :param winning_numb: int, the drawn number that made that board a winner
    :return: int, winning score of the board
    '''
    res = 0
    for l in board:
        res += sum(int(v) if v != '' else 0 for v in l)
    return res*winning_numb


def bingo(input_data):
    '''
    Main function that play the bingo game :
    for each draw number, marked the boards and determine the potential winner
    :param input_data: list, lines from input file
    :return: int, winning score of the winning board, or 0 if no winner
    '''
    numbers_draw = input_data[0].strip('\n').split(',')
    boards = get_boards(lines[2:])
    for n_draw in numbers_draw:
        boards = mark_board(boards, n_draw)
        is_winner, winning_board = any_board_winner(boards)
        if is_winner:
            return winning_score(winning_board, int(n_draw))

    return 0


print('Part 1 :', bingo(lines))


# Part 2


def not_winners_boards(boards_info):
    '''
    Return all the boards that are not winners
    :param boards_info: list, all the boards
    :return: list, all the none winners boards
    '''
    not_winners = []
    for b in boards_info:
        if not(any(l == ['', '', '', '', ''] for l in b) or \
                any([el[i] for el in b] == ['', '', '', '', ''] for i in range(5))):
            not_winners.append(b)
    return not_winners


def bingo_part2(input_data):
    '''
    main function (for part 2) that plays bingo,
    mark boards for each draw number and determine the winning score of the last winner
    :param input_data: list, data from input file
    :return: int, winning score of the last winner
    '''
    numbers_draw = input_data[0].strip('\n').split(',')
    boards = get_boards(lines[2:])
    for n_draw in numbers_draw:
        boards = mark_board(boards, n_draw)
        nw_boards = not_winners_boards(boards)
        if len(nw_boards) == 0:
            return winning_score(boards[-1], int(n_draw))
        else:
            boards = nw_boards
    print(len(boards))
    return 0


print('Part 2 :', bingo_part2(lines))