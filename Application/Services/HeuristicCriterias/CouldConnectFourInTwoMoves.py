def count_connected_twos(board, piece) -> int:
    return (__connected_twos_horizontal(board, piece) +
            __connected_twos_vertical(board, piece) +
            __connected_twos_diagonal(board, piece))


def __connected_twos_horizontal(board: list[list[str]], piece: str) -> int:
    score: int = 0
    for row in range(len(board)):
        piece_count: int = 0
        for col in range(len(board[0])):
            if board[row][col] == piece:
                piece_count += 1
                if piece_count >= 2:
                    if col + 2 < len(board[0]) and board[row][col + 1] == '' and board[row][col + 2] == '':
                        score += 1
                    if col - 3 >= 0 and board[row][col - 2] == '' and board[row][col - 3] == '':
                        score += 1
            else:
                piece_count = 0
    return score


def __connected_twos_vertical(board: list[list[str]], piece: str) -> int:
    score: int = 0
    for col in range(len(board[0])):
        piece_count: int = 0
        for row in range(len(board)):
            if board[row][col] == piece:
                piece_count += 1
                if piece_count >= 2:
                    if row + 2 < len(board) and board[row + 1][col] == '' and board[row + 2][col] == '':
                        score += 1
                    if row - 3 >= 0 and board[row - 2][col] == '' and board[row - 3][col] == '':
                        score += 1
            else:
                piece_count = 0
    return score


def __connected_twos_diagonal(board: list[list[str]], piece: str) -> int:
    score: int = 0
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == piece:
                if (row + 3 < len(board) and col + 3 < len(board[0])) and (board[row + 1][col + 1] == piece) and \
                        board[row + 2][col + 2] == '' and board[row + 3][col + 3] == '':
                    score += 1
                if (row + 3 < len(board) and col - 3 >= 0) and (board[row + 1][col - 1] == piece) and board[row + 2][
                    col - 2] == '' and board[row + 3][col - 3] == '':
                    score += 1
    return score
