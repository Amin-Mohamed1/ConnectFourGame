from abc import ABC
from Services.GameService import GameService
from Services.Heuristic import get_heuristic_value
from Services.Solver import Solver


class Node:
    def __init__(self, board: list[list[str]], move: int, depth: int, is_maximizing_player: bool):
        self.board = [row[:] for row in board]
        self.move = move
        self.depth = depth
        self.is_maximizing_player = is_maximizing_player
        self.children = []
        self.evaluation = None
        self.best_child_column = -1

    def __repr__(self):
        return f"Move: {self.move}, Depth: {self.depth}, Evaluation: {self.evaluation}"

    def to_dict(self) -> dict:
        return {
            'column': -1 if self.move is None else self.move,
            'value': self.evaluation,
            'best_child_column': self.best_child_column,
            'children': [child.to_dict() for child in self.children]
        }


class AlphaBetaService(Solver, ABC):
    memo = {}

    @staticmethod
    def solve(board: list[list[str]], piece: str, max_depth: int) -> int:
        def minimax(node: Node, alpha: float, beta: float) -> int:
            board_key = array_to_string(node.board)
            print(board_key)

            if board_key in AlphaBetaService.memo:
                return AlphaBetaService.memo[board_key]

            if node.depth == max_depth or GameService.is_full_board(node.board):
                # Evaluate the board if it's a leaf node or if we've reached max depth
                node.evaluation = get_heuristic_value(node.board, piece)
                AlphaBetaService.memo[board_key] = node.evaluation  # Cache the result
                return node.evaluation

            # Generate child nodes
            possible_moves = GameService.get_valid_moves(node.board)
            for move in possible_moves:
                child_board = GameService.get_board_after_move(node.board, move, piece)
                child_is_maximizing = not node.is_maximizing_player
                child_node = Node(child_board, move, node.depth + 1, child_is_maximizing)
                node.children.append(child_node)

            # Perform Minimax on each child and apply Alpha-Beta Pruning
            if node.is_maximizing_player:
                max_eval = float('-inf')
                for child in node.children:
                    eval = minimax(child, alpha, beta)
                    if eval > max_eval:
                        max_eval = eval
                        node.best_child_column = child.move
                    alpha = max(alpha, eval)
                    if alpha >= beta:
                        break
                node.evaluation = max_eval
                AlphaBetaService.memo[board_key] = max_eval  # Cache the result
                return max_eval

            else:
                min_eval = float('inf')
                for child in node.children:
                    eval = minimax(child, alpha, beta)
                    if eval < min_eval:
                        min_eval = eval
                        node.best_child_column = child.move
                    beta = min(beta, eval)
                    if alpha >= beta:
                        break

                node.evaluation = min_eval
                AlphaBetaService.memo[board_key] = min_eval
                return min_eval

        # Initialize the root node
        root_node = Node(board, None, 0, True)
        # Perform Minimax with Alpha-Beta Pruning
        minimax(root_node, float('-inf'), float('inf'))
        best_move = max(root_node.children, key=lambda child: child.evaluation)
        return best_move.move


def array_to_string(board: list[list[str]]) -> str:
    return "\n".join(" ".join(row) for row in board)


def main():
    board = [
        ['r', 'r', '', '', '', '', ''],
        ['r', 'r', '', 'r', 'r', '', ''],
        ['r', 'y', '', 'y', 'y', '', ''],
        ['y', 'y', '', 'r', 'r', 'r', 'r'],
        ['y', 'y', 'y', 'y', 'r', 'y', 'r'],
        ['r', 'r', 'r', 'r', 'y', 'y', 'y']
    ]

    piece = 'y'
    max_depth = 1
    print("Current board:")
    for row in board:
        print(row)

    best_move = AlphaBetaService.solve(board, piece, max_depth)
    print(f"The best column for player {piece} to play is: {best_move}")

    row_to_insert = GameService.insert_piece(board, best_move, piece)
    print(f"After the move, the board is:")
    for row in board:
        print(row)


if __name__ == "__main__":
    main()
