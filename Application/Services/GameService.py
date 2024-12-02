class GameService:
    @staticmethod
    def is_valid_move(board: list[list[str]], column: int) -> bool:
        return board[0][column] == ''

    @staticmethod
    def insert_piece(board: list[list[str]], column: int, piece: str) -> int:
        for row in range(len(board) - 1, -1, -1):
            if board[row][column] == '':
                board[row][column] = piece
                return row

    @staticmethod
    def is_full_board(board: list[list[str]]):
        for col in range(len(board[0])):
            if board[0][col] == '':
                return False
        return True

    @staticmethod
    def calculate_scores(board: list[list[str]], piece: str, row: int, column: int) -> int:
        return (GameService.__calculate_horizontal(board, piece, row, column)
                + GameService.__calculate_vertical(board, piece, row, column)
                + GameService.__calculate_diagonal(board, piece, row, column))

    @staticmethod
    def __calculate_horizontal(board: list[list[str]], piece: str, row: int, column: int) -> int:
        def score(board_state: list[list[str]], current_piece: str, row_number: int, column_number: int,
                  direction: int) -> int:
            for i in range(1 * direction, 4 * direction, 1 * direction):
                if (not GameService.__is_valid_column(board_state, column_number + i)
                        or board_state[row_number][column_number + i] != current_piece):
                    return 0
            return 1

        return score(board, piece, row, column, 1) + score(board, piece, row, column, -1)

    @staticmethod
    def __calculate_vertical(board: list[list[str]], piece: str, row: int, column: int) -> int:
        def score(board_state: list[list[str]], current_piece: str, row_number: int, column_number: int,
                  direction: int) -> int:
            for i in range(1 * direction, 4 * direction, 1 * direction):
                if (not GameService.__is_valid_row(board_state, row_number + i)
                        or board_state[row_number + i][column_number] != current_piece):
                    return 0
            return 1

        return score(board, piece, row, column, 1) + score(board, piece, row, column, -1)

    @staticmethod
    def __calculate_diagonal(board: list[list[str]], piece: str, row: int, column: int) -> int:
        def score(board_state: list[list[str]], current_piece: str, row_number: int, column_number: int,
                  row_direction: int,
                  col_direction: int) -> int:
            for _ in range(3):
                if (not GameService.__is_valid_row(board_state, row_number + row_direction) or
                        not GameService.__is_valid_column(board_state, column_number + col_direction) or
                        board_state[row_number + row_direction][column_number + col_direction] != current_piece):
                    return 0
                row_number += row_direction
                column_number += col_direction
            return 1

        return (score(board, piece, row, column, 1, 1)
                + score(board, piece, row, column, -1, 1)
                + score(board, piece, row, column, 1, -1)
                + score(board, piece, row, column, -1, -1))

    @staticmethod
    def __is_valid_column(board: list[list[str]], column: int) -> bool:
        return 0 <= column < len(board[0])

    @staticmethod
    def __is_valid_row(board: list[list[str]], row: int) -> bool:
        return 0 <= row < len(board)

    @staticmethod
    def get_valid_moves(board: list[list[str]]) -> list[int]:
        valid_moves = []
        for col in range(len(board[0])):
            if board[0][col] == '':
                valid_moves.append(col)
        return valid_moves

    @staticmethod
    def get_board_after_move(board: list[list[str]], column: int, piece: str) -> list[list[str]]:
        new_board = [row[:] for row in board]
        GameService.insert_piece(new_board, column, piece)
        return new_board  

    @staticmethod
    def convert_board_to_string(board: list[list[str]]) ->str:
        return "\n".join(" ".join(cell if cell else "." for cell in row) for row in board)
