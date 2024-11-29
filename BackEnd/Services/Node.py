class Node:
    def __init__(self, column: int):
        self.__column: int = column
        self.__children: list[Node] = []
        self.__value: int = 0
        self.__best_child_column: int = -1

    def add_child(self, child: 'Node') -> None:
        self.__children.append(child)

    def get_children(self) -> list['Node']:
        return self.__children

    def get_column(self) -> int:
        return self.__column

    def set_value(self, value: int) -> None:
        self.__value = value

    def get_value(self) -> int:
        return self.__value

    def set_best_child_column(self, column: int) -> None:
        self.__best_child_column = column

    def get_best_child_column(self) -> int:
        return self.__best_child_column