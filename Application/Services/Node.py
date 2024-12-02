class Node:
    def __init__(self, column: int):
        self.__column: int = column
        self.__children: list[Node] = []
        self.__value: float = 0
        self.__best_child_column: int = -1
        self.__nods_expanded: int = 0

    def add_child(self, child: 'Node') -> None:
        self.__children.append(child)

    def get_children(self) -> list['Node']:
        return self.__children

    def get_column(self) -> int:
        return self.__column

    def set_value(self, value: float) -> None:
        self.__value = value

    def get_value(self) -> float:
        return self.__value

    def set_best_child_column(self, column: int) -> None:
        self.__best_child_column = column

    def get_best_child_column(self) -> int:
        return self.__best_child_column

    def get_num_nodes_expanded(self) -> int:
        return self.__nods_expanded

    def set_num_nodes_expanded(self, num_nodes: int) -> None:
        self.__nods_expanded = num_nodes

    def to_dict(self) -> dict:
        return {
            'column': self.__column,
            'value': self.__value,
            'best_child_column': self.__best_child_column,
            'children': [child.to_dict() for child in self.__children]
        }