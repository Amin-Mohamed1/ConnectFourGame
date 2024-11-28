from abc import ABC

from Services.Solver import Solver


class MinMaxService(Solver, ABC):
    @staticmethod
    def solve(board: list[list[str]], piece: str) -> int:
        pass
    