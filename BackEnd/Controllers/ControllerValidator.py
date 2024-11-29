def validate_board(board: list[list[str]]) -> bool:
    if not isinstance(board, list):
        return False
    for row in board:
        if not isinstance(row, list):
            return False
        for cell in row:
            if not isinstance(cell, str):
                return False
    return True

def validate_position(board: list[list[str]], position: int) -> bool:
    if not isinstance(position, int):
        return False
    if not 0 <= position < len(board[0]):
        return False
    return True

def validate_piece(piece: str) -> bool:
    if not isinstance(piece, str):
        return False
    if piece not in ['y', 'r']:
        return False
    return True

def validate_score_json(data) -> bool:
    if data is None:
        return False
    if 'board' not in data or 'piece' not in data or 'position' not in data:
        return False
    return True

def validate_score_request(data) -> bool:
    if not validate_score_json(data):
        return False
    if not validate_board(data['board']):
        return False
    if not validate_piece(data['piece']):
        return False
    if not validate_position(data['board'], data['position']):
        return False
    return True

def validate_method(method: str) -> bool:
    if not isinstance(method, str):
        return False
    if method not in ['AlphaBeta', 'MinMax', 'ExpectiMinMax']:
        return False
    return True

def validate_depth(depth: int) -> bool:
    if not isinstance(depth, int):
        return False
    if depth < 0 or depth > 42:
        return False
    return True

def validate_ai_request(data) -> bool:
    if 'board' not in data or 'piece' not in data or 'max_depth' not in data or 'method' not in data:
        return False
    if not validate_board(data['board']):
        return False
    if not validate_piece(data['piece']):
        return False
    if not validate_depth(data['max_depth']):
        return False
    if not validate_method(data['method']):
        return False
    return True