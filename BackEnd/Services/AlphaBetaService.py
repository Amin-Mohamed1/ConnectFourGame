from abc import ABC
from Services.GameService import GameService
from Services.Node import Node
from Services.Solver import Solver
from Services.Heuristic import get_heuristic_value_2 as h
from Services.Heuristic import get_opponent_piece


class AlphaBetaService(Solver, ABC):
    num_nodes = 0

    @staticmethod
    def solve(board: list[list[str]], piece: str, max_depth: int) -> Node:
        root: Node = Node(-1)  # root node
        AlphaBetaService.__maximize(board, piece, max_depth, root, float("-inf"), float("inf"))
        print(AlphaBetaService.num_nodes)
        return root

    @staticmethod
    def __maximize(board: list[list[str]], piece: str, depth: int, parent_node: Node, alpha: float,
                   beta: float) -> None:
        AlphaBetaService.num_nodes += 1
        if GameService.is_full_board(board):
            parent_node.set_value(h(board, piece, True))
            return
        if depth == 0:
            parent_node.set_value(h(board, piece, False))
            return
        max_value: float = float('-inf')
        for col in range(len(board[0])):
            if GameService.is_valid_move(board, col):
                row: int = GameService.insert_piece(board, col, piece)
                child_node: Node = Node(col)
                parent_node.add_child(child_node)
                AlphaBetaService.__minimize(board, piece, depth - 1, child_node, alpha, beta)
                if child_node.get_value() > max_value:
                    max_value = child_node.get_value()
                    parent_node.set_value(max_value)
                    parent_node.set_best_child_column(col)
                board[row][col] = ''

                if max_value >= beta:
                    break
                if max_value > alpha:
                    alpha = max_value

    @staticmethod
    def __minimize(board: list[list[str]], piece: str, depth: int, parent_node: Node, alpha: float,
                   beta: float) -> None:
        AlphaBetaService.num_nodes += 1
        if GameService.is_full_board(board):
            parent_node.set_value(h(board, piece, True))
            return
        if depth == 0:
            parent_node.set_value(h(board, piece, False))
            return

        min_value: float = float('-inf')
        for col in range(len(board[0])):
            if GameService.is_valid_move(board, col):
                row: int = GameService.insert_piece(board, col, get_opponent_piece(piece))
                child_node: Node = Node(col)
                parent_node.add_child(child_node)
                AlphaBetaService.__maximize(board, piece, depth - 1, child_node, alpha, beta)
                if child_node.get_value() < min_value:
                    min_value = child_node.get_value()
                    parent_node.set_value(min_value)
                    parent_node.set_best_child_column(col)
                board[row][col] = ''

                if min_value <= alpha:
                    break
                if min_value < beta:
                    beta = min_value


if __name__ == '__main__':
    board = [
        ["", "", "", "", "", "", ""],
        ["", "", "", "", "", "", ""],
        ["", "", "", "", "", "", ""],
        ["", "y", "", "", "", "", ""],
        ["", "r", "", "y", "", "r", ""],
        ["y", "r", "r", "r", "y", "y", ""],
    ]

    best_move = AlphaBetaService.solve(board, 'r', 6).get_best_child_column()
    print(best_move)
