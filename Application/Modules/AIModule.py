from Services.AlphaBetaService import AlphaBetaService
from Services.MinMaxService import MinMaxService
from Services.ExpectiMiniMaxService import ExpectiMinimaxService
from Services.Node import Node


class AIModule:
    def __init__(self):
        self.__root: Node = None

    def get_action(self, board: list[list[str]], piece: str, max_depth: int, method: str) -> int:
        if method == 'AlphaBeta':
            self.__root = AlphaBetaService.solve(board, piece, max_depth)
            return self.__root.get_best_child_column()
        elif method == 'MinMax':
            self.__root = MinMaxService.solve(board, piece, max_depth)
            return self.__root.get_best_child_column()
        elif method == 'ExpectiiMinMax':
            self.__root = ExpectiMinimaxService.solve(board, piece, max_depth)
            return self.__root.get_best_child_column()
        else:
            return -1

    def get_root(self) -> Node:
        return self.__root