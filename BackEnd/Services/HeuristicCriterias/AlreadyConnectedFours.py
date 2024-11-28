def count_connected_fours(board, piece) -> int:
    return (__count_connected_fours_horizontal(board, piece) +
            __connected_fours_vertical(board, piece) +
            __connected_fours_diagonal(board, piece))


def __count_connected_fours_horizontal(board: list[list[str]], piece: str) -> int:
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


def __connected_fours_vertical(board: list[list[str]], piece: str) -> int:
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


def __connected_fours_diagonal(board: list[list[str]], piece: str) -> int:
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
