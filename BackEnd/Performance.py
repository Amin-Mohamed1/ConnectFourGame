import math
import random
import time

import matplotlib.pyplot as plt

from Services.AlphaBetaService import AlphaBetaService
from Services.MinMaxService import MinMaxService
from Services.Node import Node


class Performance:
    def generate(self, repeat: int = 3, depth: int = 10, moves: int = 10) -> None:
        runs: int = repeat
        k_range: int = depth
        piece: str = 'r' if moves % 2 == 0 else 'y'
        all_time_for_normal: list[float] = []
        all_time_for_pruning: list[float] = []
        nodes_visited_normal: list[int] = []
        nodes_visited_pruning: list[int] = []
        for k in range(1, k_range + 1):
            time_normal: float = 0.0
            time_pruning: float = 0.0
            nodes_normal: int = 0
            nodes_pruning: int = 0
            for _ in range(runs):
                board: list[list[str]] = self.__generate_board(moves)

                start_time: float = time.time()
                node: Node = MinMaxService.solve(board, piece, k)
                time_normal += (time.time() - start_time) * 1000  # Convert to milliseconds
                nodes_normal += node.get_num_nodes_expanded()

                start_time = time.time()
                node = AlphaBetaService.solve(board, piece, k)
                time_pruning += (time.time() - start_time) * 1000  # Convert to milliseconds
                nodes_pruning += node.get_num_nodes_expanded()

            all_time_for_normal.append(time_normal / runs)
            all_time_for_pruning.append(time_pruning / runs)
            nodes_visited_normal.append(math.ceil(nodes_normal / runs))
            nodes_visited_pruning.append(math.ceil(nodes_pruning / runs))

        self.__save_into_file(all_time_for_normal, nodes_visited_normal, "normal.txt")
        self.__save_into_file(all_time_for_pruning, nodes_visited_pruning, "pruning.txt")

        self.__draw(all_time_for_normal, all_time_for_pruning, "Normal", "Pruning",
                  "Average Time at a specific depth (ms)", "Average Time at a specific depth (ms)")
        self.__draw(nodes_visited_normal, nodes_visited_pruning, "Normal", "Pruning",
                  "Nodes visited at a specific depth", "Nodes visited at a specific depth")

        k_values = [i for i in range(1, k_range + 1)]
        self.__draw(k_values, all_time_for_normal, "Tree Depth", "MinMax",
                  "Depth", "Average Time (ms)")
        self.__draw(k_values, all_time_for_pruning, "Tree Depth", "AlphaBeta",
                  "Depth", "Average Time (ms)")

    def __generate_board(self, moves: int) -> list[list[str]]:
        rows, cols = 6, 7
        board = [['' for _ in range(cols)] for _ in range(rows)]
        moves = moves
        current_piece = ''
        while moves > 0:
            col = random.randint(0, cols - 1)
            for row in range(rows - 1, -1, -1):
                if board[row][col] == "":
                    board[row][col] = current_piece
                    current_piece = 'y' if current_piece == 'r' else 'r'
                    moves -= 1
                    break
        return board

    def __save_into_file(self, times: list[float], nodes: list[int], filename: str):
        with open(filename, "w") as file:
            file.write(" ".join(map(str, times)) + "\n")
            file.write(" ".join(map(str, nodes)) + "\n")

    def __draw(self, list1, list2, label1: str, label2: str, x_label: str, y_label: str):
        plt.plot(list1, list2, marker='o')
        plt.title(f"{label1} vs {label2}")
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.legend()
        plt.grid(True, linestyle='-', linewidth=0.5, color='gray')
        plt.show()

if __name__ == '__main__':
    performance = Performance()
    performance.generate(3, 10, 13)
    file1_data = [0.0, 7.441043853759766, 19.814014434814453, 91.69149398803711, 349.9791622161865,
                  1283.5532029469807, 4172.321160634358, 12510.696411132812, 40442.13740030924, 106472.64035542806]
    file2_data = [1.0058879852294922, 1.6747315724690754, 10.481675465901693, 35.10236740112305,
                  113.54708671569824, 275.04340807596844, 807.8405857086182, 3515.2389208475747,
                  11438.16868464152, 18629.90601857503]

    # Define the x-axis values from 1 to 10
    x_values = range(1, 11)

    # Plot the data
    plt.figure(figsize=(10, 6))
    plt.plot(x_values, file1_data, label="Minmax", marker='o', linestyle='-', color='blue')
    plt.plot(x_values, file2_data, label="Alpha-Beta", marker='s', linestyle='-', color='green')

    # Customizing the plot
    plt.xlabel("Depth (1 to 10)")
    plt.ylabel("Time (ms)")
    plt.title("Comparison of Data from Two Files")
    plt.grid(True, which="both", linestyle='--', linewidth=0.5)
    plt.legend()

    # Show the plot
    plt.tight_layout()
    plt.show()