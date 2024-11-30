import time
from abc import ABC

from Services.AlphaBetaService import AlphaBetaService
from Services.GameService import GameService
from Services.MinMaxService import MinMaxService
from Services.Node import Node
from Services.Solver import Solver
from Services.Heuristic import get_heuristic_value_2 as h
from Services.Heuristic import get_opponent_piece


class ExpectiMinimaxService(Solver, ABC):
    num_nodes = 0
    @staticmethod
    def solve(board: list[list[str]], piece: str, max_depth: int) -> Node:
        root: Node = Node(-1)
        ExpectiMinimaxService.__maximize(board, piece, max_depth, root)
        return root

    @staticmethod
    def __maximize(board: list[list[str]], piece: str, depth: int, parent_node: Node) -> None:
        ExpectiMinimaxService.num_nodes += 1
        if GameService.is_full_board(board):
            parent_node.set_value(h(board, piece, True))
            return

        if depth <= 0:
            parent_node.set_value(h(board, piece, False))
            return

        max_value = float("-inf")
        parent_node.set_value(max_value)

        for col in range(len(board[0])):
            if GameService.is_valid_move(board, col):
                child_node = Node(col)
                parent_node.add_child(child_node)
                ExpectiMinimaxService.__chance(board, piece, depth - 1,
                                               child_node, True)

                if child_node.get_value() > max_value:
                    max_value = child_node.get_value()
                    parent_node.set_value(max_value)
                    parent_node.set_best_child_column(col)

    @staticmethod
    def __chance(board: list[list[str]], piece: str, depth: int, parent_node: Node, maximize: bool) -> None:
        ExpectiMinimaxService.num_nodes += 1
        col = parent_node.get_column()
        probability_distribution = {}

        if GameService.is_valid_move(board, col):
            probability_distribution[col] = 0.6

        if col == 0:
            if GameService.is_valid_move(board, col + 1):  # Right column
                probability_distribution[col + 1] = 0.4
            # If the right column is invalid, make the probability for the current column 1
            elif not GameService.is_valid_move(board, col + 1):
                probability_distribution = {col: 1}

        elif col == len(board[0]) - 1:
            if GameService.is_valid_move(board, col - 1):  # Left column
                probability_distribution[col - 1] = 0.4
            # If the left column is invalid, make the probability for the current column 1
            elif not GameService.is_valid_move(board, col - 1):
                probability_distribution = {col: 1}

        # Handle general case
        else:
            # Left column
            if GameService.is_valid_move(board, col - 1):
                probability_distribution[col - 1] = 0.2
            # Right column
            if GameService.is_valid_move(board, col + 1):
                probability_distribution[col + 1] = 0.2

            # If both left and right columns are invalid, make the probability for the current column 1
            if not GameService.is_valid_move(board, col - 1) and not GameService.is_valid_move(board, col + 1):
                probability_distribution = {col: 1}

            if not GameService.is_valid_move(board, col - 1):
                probability_distribution[col] = 0.6
                probability_distribution[col + 1] = 0.4

            if not GameService.is_valid_move(board, col + 1):
                probability_distribution[col] = 0.6
                probability_distribution[col - 1] = 0.4

        # Calculate expected value
        expected_value = 0
        for col, probability in probability_distribution.items():
            if GameService.is_valid_move(board, col):
                row = GameService.insert_piece(board, col, piece if maximize else get_opponent_piece(piece))
                child_node = Node(col)
                parent_node.add_child(child_node)

                # Recursively calculate for the next layer (Max or Min)
                if maximize:
                    ExpectiMinimaxService.__minimize(board, piece, depth - 1, child_node)
                else:
                    ExpectiMinimaxService.__maximize(board, piece, depth - 1, child_node)

                expected_value += probability * child_node.get_value()
                board[row][col] = ''

        parent_node.set_value(expected_value)

    @staticmethod
    def __minimize(board: list[list[str]], piece: str, depth: int, parent_node: Node) -> None:
        ExpectiMinimaxService.num_nodes += 1
        if GameService.is_full_board(board):
            parent_node.set_value(h(board, piece, True))
            return
        if depth <= 0:
            parent_node.set_value(h(board, piece, False))
            return

        min_value = float("inf")
        parent_node.set_value(min_value)

        for col in range(len(board[0])):
            if GameService.is_valid_move(board, col):
                child_node = Node(col)
                parent_node.add_child(child_node)
                ExpectiMinimaxService.__chance(board, piece, depth - 1, child_node, False)

                if child_node.get_value() < min_value:
                    min_value = child_node.get_value()
                    parent_node.set_value(min_value)


if __name__ == '__main__':

    # Sample board for the game
    board = [
        ["", "", "", "", "", "", ""],
        ["", "", "", "", "", "", ""],
        ["", "", "", "", "", "", ""],
        ["", "", "", "", "", "", ""],
        ["", "", "", "", "", "", ""],
        ["r", "y", "r", "y", "", "", ""],
    ]

    # Timing and printing the results
    print("Starting ExpectiMinimaxService...")
    start_time = time.time()
    best_move1 = ExpectiMinimaxService.solve(board, 'r', 7).get_best_child_column()
    print(f"ExpectiMinimaxService - Nodes expanded: {ExpectiMinimaxService.num_nodes}")
    print(f"Time taken: {time.time() - start_time:.4f} seconds")

    print("\nStarting AlphaBetaService...")
    start_time = time.time()
    best_move2 = AlphaBetaService.solve(board, 'r', 6).get_best_child_column()
    print(f"AlphaBetaService - Nodes expanded: {AlphaBetaService.num_nodes}")
    print(f"Time taken: {time.time() - start_time:.4f} seconds")

    print("\nStarting MinMaxService...")
    start_time = time.time()
    best_move3 = MinMaxService.solve(board, 'r', 8).get_best_child_column()
    print(f"MinMaxService - Nodes expanded: {MinMaxService.num_nodes}")
    print(f"Time taken: {time.time() - start_time:.4f} seconds")

    # Printing best moves for comparison
    print(f"\nBest Move Column (ExpectiMinimax, AlphaBeta, MinMax): {best_move1}, {best_move2}, {best_move3}")

