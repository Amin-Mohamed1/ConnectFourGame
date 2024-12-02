from Services.GameService import GameService
from Services.HeuristicCriterias.AlreadyConnectedFours import count_connected_fours
class ScoreModule:
    @staticmethod
    def get_action(board: list[list[str]], piece: str) -> int:
        return count_connected_fours(board, piece)
