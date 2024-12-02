from Services.GameService import GameService
class ScoreModule:
    @staticmethod
    def get_action(board: list[list[str]], position: int, piece: str) -> int:
        row: int = GameService.insert_piece(board, position, piece)
        return GameService.calculate_scores(board, piece, row, position)
