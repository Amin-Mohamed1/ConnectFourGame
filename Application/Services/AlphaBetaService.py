from abc import ABC
from Services.GameService import GameService
from Services.Node import Node
from Services.Solver import Solver
from Services.Heuristic import get_heuristic_value_2 as h
from Services.Heuristic import get_opponent_piece


class AlphaBetaService(Solver, ABC):
    board_cache = {}
    num_nodes = 0

    @staticmethod
    def solve(board: list[list[str]], piece: str, max_depth: int) -> Node:
        root: Node = Node(-1)
        AlphaBetaService.__maximize(board, piece, max_depth, root, float("-inf"), float("inf"))
        root.set_num_nodes_expanded(AlphaBetaService.num_nodes)
        return root

    @staticmethod
    def __maximize(board: list[list[str]], piece: str, depth: int,
                   parent_node: Node, alpha: float,
                   beta: float) -> None:
        AlphaBetaService.num_nodes += 1
        board_tuple = GameService.convert_board_to_string(board)
        if board_tuple in AlphaBetaService.board_cache:
            parent_node.set_value(AlphaBetaService.board_cache[board_tuple])
            return

        if GameService.is_full_board(board):
            heuristic_value = h(board, piece, True)
            AlphaBetaService.board_cache[board_tuple] = heuristic_value
            parent_node.set_value(heuristic_value)
            return

        if depth == 0:
            heuristic_value = h(board, piece, False)
            AlphaBetaService.board_cache[board_tuple] = heuristic_value
            parent_node.set_value(heuristic_value)
            return

        max_value = float("-inf")
        parent_node.set_value(max_value)

        for col in range(len(board[0])):
            if GameService.is_valid_move(board, col):
                row = GameService.insert_piece(board, col, piece)
                child_node = Node(col)
                parent_node.add_child(child_node)

                AlphaBetaService.__minimize(board, piece, depth - 1, child_node, alpha, beta)
                if child_node.get_value() > max_value:
                    max_value = child_node.get_value()
                    parent_node.set_value(max_value)
                    parent_node.set_best_child_column(col)

                board[row][col] = ''
                if max_value >= beta:
                    break
                alpha = max(alpha, max_value)
        AlphaBetaService.board_cache[board_tuple] = parent_node.get_value()

    @staticmethod
    def __minimize(board: list[list[str]], piece: str, depth: int, parent_node: Node, alpha: float,
                   beta: float) -> None:
        AlphaBetaService.num_nodes += 1
        board_tuple = GameService.convert_board_to_string(board)
        if board_tuple in AlphaBetaService.board_cache:
            parent_node.set_value(AlphaBetaService.board_cache[board_tuple])
            return

        if GameService.is_full_board(board):
            heuristic_value = h(board, piece, True)
            AlphaBetaService.board_cache[board_tuple] = heuristic_value
            parent_node.set_value(heuristic_value)
            return
        if depth == 0:
            heuristic_value = h(board, piece, False)
            AlphaBetaService.board_cache[board_tuple] = heuristic_value
            parent_node.set_value(heuristic_value)
            return

        min_value = float("inf")
        parent_node.set_value(min_value)

        for col in range(len(board[0])):
            if GameService.is_valid_move(board, col):
                row = GameService.insert_piece(board, col, get_opponent_piece(piece))
                child_node = Node(col)
                parent_node.add_child(child_node)
                AlphaBetaService.__maximize(board, piece, depth - 1, child_node, alpha, beta)

                if child_node.get_value() < min_value:
                    min_value = child_node.get_value()
                    parent_node.set_value(min_value)
                    parent_node.set_best_child_column(col)
                board[row][col] = ''

                if min_value <= alpha:
                    break
                beta = min(beta, min_value)

        AlphaBetaService.board_cache[board_tuple] = parent_node.get_value()
