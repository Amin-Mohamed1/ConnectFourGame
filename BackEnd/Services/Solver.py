from abc import abstractmethod

from Services.Node import Node


class Solver:
    @staticmethod
    @abstractmethod
    def solve(board: list[list[str]], piece: str, max_depth: int) -> Node:
        pass