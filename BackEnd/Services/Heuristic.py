def get_opponent_piece(piece) -> str:
    return 'r' if piece == 'y' else 'y'


def count_connected_fours(board, piece) -> int:
    return (count_connected_fours_horizontal(board, piece) +
            connected_fours_vertical(board, piece) +
            connected_fours_diagonal(board, piece))


def count_connected_fours_horizontal(board: list[list[str]], piece: str) -> int:
    score: int = 0
    for row in range(len(board)):
        piece_count: int = 0
        for col in range(len(board[0])):
            if board[row][col] == piece:
                piece_count += 1
                if piece_count >= 4:
                    score += 1
            else:
                piece_count = 0
    return score


def connected_fours_vertical(board: list[list[str]], piece: str) -> int:
    score: int = 0
    for col in range(len(board[0])):
        piece_count: int = 0
        for row in range(len(board)):
            if board[row][col] == piece:
                piece_count += 1
                if piece_count >= 4:
                    score += 1
            else:
                piece_count = 0
    return score


def connected_fours_diagonal(board: list[list[str]], piece: str) -> int:
    score: int = 0
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == piece:
                if (row + 3 < len(board) and col + 3 < len(board[0]) and
                        board[row + 1][col + 1] == piece and
                        board[row + 2][col + 2] == piece and
                        board[row + 3][col + 3] == piece):
                    score += 1
                if (row + 3 < len(board) and col - 3 >= 0 and
                        board[row + 1][col - 1] == piece and
                        board[row + 2][col - 2] == piece and
                        board[row + 3][col - 3] == piece):
                    score += 1
    return score


def count_connected_threes(board, piece) -> int:
    return (connected_threes_horizontal(board, piece) +
            connected_threes_vertical(board, piece) +
            connected_threes_diagonal(board, piece))


def connected_threes_horizontal(board: list[list[str]], piece: str) -> int:
    score: int = 0
    for row in range(len(board)):
        piece_count: int = 0
        for col in range(len(board[0])):
            if board[row][col] == piece:
                piece_count += 1
                if piece_count >= 3:
                    if col + 1 < len(board[0]) and board[row][col + 1] == '':
                        score += 1
                    if col - 3 >= 0 and board[row][col - 3] == '':
                        score += 1
            else:
                piece_count = 0
    return score


def connected_threes_vertical(board: list[list[str]], piece: str) -> int:
    score: int = 0
    for col in range(len(board[0])):
        piece_count: int = 0
        for row in range(len(board)):
            if board[row][col] == piece:
                piece_count += 1
                if piece_count >= 3:
                    if row + 1 < len(board) and board[row + 1][col] == '':
                        score += 1
                    if row - 3 >= 0 and board[row - 3][col] == '':
                        score += 1
            else:
                piece_count = 0
    return score


def connected_threes_diagonal(board: list[list[str]], piece: str) -> int:
    score: int = 0
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == piece:
                if (row + 3 < len(board) and col + 3 < len(board[0])) and (board[row + 1][col + 1] == piece) and \
                        board[row + 2][col + 2] == piece and board[row + 3][col + 3] == '':
                    score += 1
                if (row + 3 < len(board) and col - 3 >= 0) and (board[row + 1][col - 1] == piece) and board[row + 2][
                    col - 2] == piece and board[row + 3][col - 3] == '':
                    score += 1
    return score


def count_connected_twos(board, piece) -> int:
    return (connected_twos_horizontal(board, piece) +
            connected_twos_vertical(board, piece) +
            connected_twos_diagonal(board, piece))


def connected_twos_horizontal(board: list[list[str]], piece: str) -> int:
    score: int = 0
    for row in range(len(board)):
        piece_count: int = 0
        for col in range(len(board[0])):
            if board[row][col] == piece:
                piece_count += 1
                if piece_count >= 2:
                    if col + 1 < len(board[0]) and board[row][col + 1] == '':
                        score += 1
                    if col - 2 >= 0 and board[row][col - 2] == '':
                        score += 1
            else:
                piece_count = 0
    return score


def connected_twos_vertical(board: list[list[str]], piece: str) -> int:
    score: int = 0
    for col in range(len(board[0])):
        piece_count: int = 0
        for row in range(len(board)):
            if board[row][col] == piece:
                piece_count += 1
                if piece_count >= 2:
                    if row + 1 < len(board) and board[row + 1][col] == '':
                        score += 1
                    if row - 2 >= 0 and board[row - 2][col] == '':
                        score += 1
            else:
                piece_count = 0
    return score


def connected_twos_diagonal(board: list[list[str]], piece: str) -> int:
    score: int = 0
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == piece:
                if (row + 2 < len(board) and col + 2 < len(board[0])) and (board[row + 1][col + 1] == piece) and \
                        board[row + 2][col + 2] == '':
                    score += 1
                if (row + 2 < len(board) and col - 2 >= 0) and (board[row + 1][col - 1] == piece) and board[row + 2][
                    col - 2] == '':
                    score += 1
    return score


def count_pieces_in_middle_column(board, piece) -> int:
    score: int = 0
    mid: int = len(board[0]) // 2
    for row in range(len(board)):
        if board[row][mid] == piece:
            score += 1
    return score


def count_pieces_in_columns_next_to_middle(board, piece) -> int:
    score: int = 0
    mid: int = len(board[0]) // 2
    if mid - 1 >= 0:
        for row in range(len(board)):
            if board[row][mid - 1] == piece:
                score += 1
    if mid + 1 < len(board[0]):
        for row in range(len(board)):
            if board[row][mid + 1] == piece:
                score += 1
    return score


def count_pieces_in_remaining_columns_except_corners(board, piece) -> int:
    score: int = 0
    mid: int = len(board[0]) // 2
    for row in range(len(board)):
        for col in range(1, mid - 1):
            if board[row][col] == piece:
                score += 1
        for col in range(mid + 2, len(board[0])):
            if board[row][col] == piece:
                score += 1
    return score


def count_pieces_in_corners(board, piece) -> int:
    score: int = 0
    last_col: int = len(board[0]) - 1
    for row in range(len(board)):
        if board[row][0] == piece:
            score += 1
        if board[row][last_col] == piece:
            score += 1
    return score


def get_heuristic_value(board: list[list[str]], piece: str) -> int:
    already_connected_fours_count_piece: int = count_connected_fours(board, piece)
    already_connected_fours_count_opponent: int = count_connected_fours(board, get_opponent_piece(piece))

    already_connected_threes_count_piece: int = count_connected_threes(board, piece)
    already_connected_threes_count_opponent: int = count_connected_threes(board, get_opponent_piece(piece))

    already_connected_twos_count_piece: int = count_connected_twos(board, piece)
    already_connected_twos_count_opponent: int = count_connected_twos(board, get_opponent_piece(piece))

    pieces_in_middle_column: int = count_pieces_in_middle_column(board, piece)
    pieces_in_middle_column_opponent: int = count_pieces_in_middle_column(board, get_opponent_piece(piece))

    pieces_in_two_columns_before_and_after_middle: int = count_pieces_in_columns_next_to_middle(board, piece)
    pieces_in_two_columns_before_and_after_middle_opponent: int = count_pieces_in_columns_next_to_middle(board,
                                                                                                         get_opponent_piece(
                                                                                                             piece))

    pieces_in_remaining_columns_except_corners: int = count_pieces_in_remaining_columns_except_corners(board, piece)
    pieces_in_remaining_columns_except_corners_opponent: int = count_pieces_in_remaining_columns_except_corners(board,
                                                                                                                get_opponent_piece(
                                                                                                                    piece))

    pieces_in_corners: int = count_pieces_in_corners(board, piece)
    pieces_in_corners_opponent: int = count_pieces_in_corners(board, get_opponent_piece(piece))

    connected_fours_score: int = 2_000
    connected_threes_score: int = 500
    connected_twos_score: int = 50
    pieces_in_middle_column_score: int = 20
    pieces_in_two_columns_before_and_after_middle_score: int = 10
    pieces_in_remaining_columns_except_corners_score: int = 5
    pieces_in_corners_score: int = 1

    current_player_score: int = (already_connected_fours_count_piece * connected_fours_score +
                                 already_connected_threes_count_piece * connected_threes_score +
                                 already_connected_twos_count_piece * connected_twos_score +
                                 pieces_in_middle_column * pieces_in_middle_column_score +
                                 pieces_in_two_columns_before_and_after_middle * pieces_in_two_columns_before_and_after_middle_score +
                                 pieces_in_remaining_columns_except_corners * pieces_in_remaining_columns_except_corners_score +
                                 pieces_in_corners * pieces_in_corners_score)

    opponent_score: int = (already_connected_fours_count_opponent * connected_fours_score +
                           already_connected_threes_count_opponent * connected_threes_score +
                           already_connected_twos_count_opponent * connected_twos_score +
                           pieces_in_middle_column_opponent * pieces_in_middle_column_score +
                           pieces_in_two_columns_before_and_after_middle_opponent * pieces_in_two_columns_before_and_after_middle_score +
                           pieces_in_remaining_columns_except_corners_opponent * pieces_in_remaining_columns_except_corners_score +
                           pieces_in_corners_opponent * pieces_in_corners_score)

    return current_player_score - opponent_score
