from Services.AlphaBetaService import AlphaBetaService
from Services.Node import Node


def solve(board: list[list[str]], turn: str, depth: int = 10) -> int:
    node:Node = AlphaBetaService.solve(board, turn, depth)
    return node.get_best_child_column()

if __name__ == "__main__":
    current_board = [
        ['', '', '', '', '', '', ''],
        ['', '', '', '', '', '', ''],
        ['', 'r', '', '', '', '', ''],
        ['', 'y', 'r', '', '', '', ''],
        ['', 'y', 'r', '', '', '', ''],
        ['y', 'y', 'r', '', '', '', ''],
    ]
    max_depth = 5
    current_turn = 'r'
    print(solve(current_board, current_turn, max_depth))