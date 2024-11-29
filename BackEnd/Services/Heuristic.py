from Services.HeuristicCriterias.AlreadyConnectedFours import count_connected_fours
from Services.HeuristicCriterias.CouldConnectFourInOneMove import could_connect_four_in_one_move
from Services.HeuristicCriterias.CouldConnectFourInTwoMoves import count_connected_twos
from Services.HeuristicCriterias.SinglePiecePosition import count_pieces_in_middle_column, \
    count_pieces_in_columns_next_to_middle, count_pieces_in_remaining_columns_except_corners, count_pieces_in_corners


def get_opponent_piece(piece) -> str:
    return 'r' if piece == 'y' else 'y'


def get_heuristic_value_2(board: list[list[str]], piece: str, is_full_board: bool) -> int:
    if is_full_board:
        already_connected_fours_count_piece: int = count_connected_fours(board, piece)
        already_connected_fours_count_opponent: int = count_connected_fours(board, get_opponent_piece(piece))
        return (already_connected_fours_count_piece - already_connected_fours_count_opponent) * 2_000
    else:
        return get_heuristic_value(board, piece)


def get_heuristic_value(board: list[list[str]], piece: str) -> int:
    already_connected_fours_count_piece: int = count_connected_fours(board, piece)
    already_connected_fours_count_opponent: int = count_connected_fours(board, get_opponent_piece(piece))

    could_connect_four_in_one_move_count: int = could_connect_four_in_one_move(board, piece)
    could_connect_four_in_one_move_count_opponent: int = could_connect_four_in_one_move(board,
                                                                                        get_opponent_piece(piece))

    could_connect_four_in_two_moves_count: int = count_connected_twos(board, piece)
    could_connect_four_in_two_moves_count_opponent: int = count_connected_twos(board, get_opponent_piece(piece))

    pieces_in_middle_column: int = count_pieces_in_middle_column(board, piece)
    pieces_in_middle_column_opponent: int = count_pieces_in_middle_column(board, get_opponent_piece(piece))

    pieces_in_two_columns_before_and_after_middle: int = count_pieces_in_columns_next_to_middle(board, piece)
    pieces_in_two_columns_before_and_after_middle_opponent: int = count_pieces_in_columns_next_to_middle(board,
                                                                                                         get_opponent_piece(
                                                                                                             piece))

    pieces_in_remaining_columns_except_corners: int = count_pieces_in_remaining_columns_except_corners(board, piece)
    pieces_in_remaining_columns_except_corners_opponent: int = count_pieces_in_remaining_columns_except_corners(board,
                                                                                                                get_opponent_piece(
                                                                                                                    piece))

    pieces_in_corners: int = count_pieces_in_corners(board, piece)
    pieces_in_corners_opponent: int = count_pieces_in_corners(board, get_opponent_piece(piece))

    connected_fours_score: int = 2_000
    threes_could_be_fours_score: int = 1_000
    twos_could_be_fours_score: int = 150
    pieces_in_middle_column_score: int = 20
    pieces_in_two_columns_before_and_after_middle_score: int = 10
    pieces_in_remaining_columns_except_corners_score: int = 5
    pieces_in_corners_score: int = 1

    current_player_score: int = (already_connected_fours_count_piece * connected_fours_score +
                                 could_connect_four_in_one_move_count * threes_could_be_fours_score +
                                 could_connect_four_in_two_moves_count * twos_could_be_fours_score +
                                 pieces_in_middle_column * pieces_in_middle_column_score +
                                 pieces_in_two_columns_before_and_after_middle * pieces_in_two_columns_before_and_after_middle_score +
                                 pieces_in_remaining_columns_except_corners * pieces_in_remaining_columns_except_corners_score +
                                 pieces_in_corners * pieces_in_corners_score)

    opponent_score: int = (already_connected_fours_count_opponent * connected_fours_score +
                           could_connect_four_in_one_move_count_opponent * threes_could_be_fours_score +
                           could_connect_four_in_two_moves_count_opponent * twos_could_be_fours_score +
                           pieces_in_middle_column_opponent * pieces_in_middle_column_score +
                           pieces_in_two_columns_before_and_after_middle_opponent * pieces_in_two_columns_before_and_after_middle_score +
                           pieces_in_remaining_columns_except_corners_opponent * pieces_in_remaining_columns_except_corners_score +
                           pieces_in_corners_opponent * pieces_in_corners_score)

    return current_player_score - opponent_score
