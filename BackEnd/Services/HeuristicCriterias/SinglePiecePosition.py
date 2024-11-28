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
