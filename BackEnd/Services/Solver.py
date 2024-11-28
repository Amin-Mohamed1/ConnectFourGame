from abc import abstractmethod


class Solver:
    @staticmethod
    @abstractmethod
    def solve(board: list[list[str]], piece: str) -> int:
        pass