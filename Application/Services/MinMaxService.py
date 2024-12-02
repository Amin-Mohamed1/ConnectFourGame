from abc import ABC
from sys import maxsize

from Services.GameService import GameService
from Services.Node import Node
from Services.Solver import Solver
from Services.Heuristic import get_heuristic_value_2 as h
from Services.Heuristic import get_opponent_piece


class MinMaxService(Solver, ABC):
    @staticmethod
    def solve(board: list[list[str]], piece: str, max_depth: int) -> Node:
        root: Node = Node(-1)  # root node
        MinMaxService.__maximize(board, piece, max_depth, root)
        return root

    @staticmethod
    def __maximize(board: list[list[str]], piece: str, depth: int, parent_node: Node) -> None:
        if GameService.is_full_board(board):
            parent_node.set_value(h(board, piece, True))
            return
        if depth == 0:
            parent_node.set_value(h(board, piece, False))
            return
        max_value: int = -maxsize - 1
        parent_node.set_value(max_value)
        for col in range(len(board[0])):
            if GameService.is_valid_move(board, col):
                row: int = GameService.insert_piece(board, col, piece)
                child_node: Node = Node(col)
                parent_node.add_child(child_node)
                MinMaxService.__minimize(board, piece, depth - 1, child_node)
                if child_node.get_value() > max_value:
                    max_value = child_node.get_value()
                    parent_node.set_value(max_value)
                    parent_node.set_best_child_column(col)
                board[row][col] = ''

    @staticmethod
    def __minimize(board: list[list[str]], piece: str, depth: int, parent_node: Node) -> None:
        if GameService.is_full_board(board):
            parent_node.set_value(h(board, piece, True))
            return
        if depth == 0:
            parent_node.set_value(h(board, piece, False))
            return
        min_value: int = maxsize
        parent_node.set_value(min_value)
        for col in range(len(board[0])):
            if GameService.is_valid_move(board, col):
                row: int = GameService.insert_piece(board, col, get_opponent_piece(piece))
                child_node: Node = Node(col)
                parent_node.add_child(child_node)
                MinMaxService.__maximize(board, piece, depth - 1, child_node)
                if child_node.get_value() < min_value:
                    min_value = child_node.get_value()
                    parent_node.set_value(min_value)
                    parent_node.set_best_child_column(col)
                board[row][col] = ''


if __name__ == '__main__':
    board = [
        ['r', 'y', 'r', 'y', 'y', 'y', ''],
        ['r', 'r', 'y', 'r', 'r', 'r', 'r'],
        ['r', 'y', 'r', 'y', 'y', 'y', 'y'],
        ['y', 'y', 'r', 'r', 'r', 'r', 'r'],
        ['y', 'y', 'y', 'y', 'r', 'y', 'r'],
        ['r', 'r', 'r', 'r','y','y','y']
    ]

    best_move = MinMaxService.solve(board, 'y', 10).get_best_child_column()
    print(best_move)