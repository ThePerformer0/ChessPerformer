BOARD_SIZE = 8

def get_pawn_moves(start_row, start_col, board, is_white):
    """Retourne les mouvements valides pour un pion."""
    moves = []
    direction = -1 if is_white else 1  # Blancs montent, Noirs descendent
    forward_row = start_row + direction

    # Mouvement en avant
    if 0 <= forward_row < BOARD_SIZE and board[forward_row][start_col] is None:
        moves.append((forward_row, start_col))

        # Mouvement initial de deux cases
        initial_row = 6 if is_white else 1
        if start_row == initial_row and board[forward_row + direction][start_col] is None:
            moves.append((forward_row + direction, start_col))

    # Capture diagonale
    for col_offset in [-1, 1]:
        capture_col = start_col + col_offset
        if 0 <= capture_col < BOARD_SIZE:
            target_piece = board[forward_row][capture_col]
            if target_piece and target_piece.is_white != is_white:
                moves.append((forward_row, capture_col))

    return moves


def get_rook_moves(start_row, start_col, board, is_white):
    """Retourne les mouvements valides pour une tour."""
    return get_straight_line_moves(start_row, start_col, board, is_white)


def get_bishop_moves(start_row, start_col, board, is_white):
    """Retourne les mouvements valides pour un fou."""
    return get_diagonal_moves(start_row, start_col, board, is_white)


def get_knight_moves(start_row, start_col, board, is_white):
    """Retourne les mouvements valides pour un cavalier."""
    moves = []
    knight_moves = [
        (-2, -1), (-1, -2), (1, -2), (2, -1),
        (-2, 1), (-1, 2), (1, 2), (2, 1),
    ]

    for dr, dc in knight_moves:
        row, col = start_row + dr, start_col + dc
        if 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE:
            target_piece = board[row][col]
            if not target_piece or target_piece.is_white != is_white:
                moves.append((row, col))

    return moves


def get_queen_moves(start_row, start_col, board, is_white):
    """Retourne les mouvements valides pour une reine."""
    return get_straight_line_moves(start_row, start_col, board, is_white) + \
           get_diagonal_moves(start_row, start_col, board, is_white)


def get_king_moves(start_row, start_col, board, is_white):
    """Retourne les mouvements valides pour un roi."""
    moves = []
    king_moves = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),         (0, 1),
        (1, -1), (1, 0), (1, 1),
    ]

    for dr, dc in king_moves:
        row, col = start_row + dr, start_col + dc
        if 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE:
            target_piece = board[row][col]
            if not target_piece or target_piece.is_white != is_white:
                moves.append((row, col))

    return moves


def get_straight_line_moves(start_row, start_col, board, is_white):
    """Retourne les mouvements en ligne droite (utilisé par la tour et la reine)."""
    moves = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in directions:
        row, col = start_row + dr, start_col + dc
        while 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE:
            target_piece = board[row][col]
            if not target_piece:
                moves.append((row, col))
            elif target_piece.is_white != is_white:
                moves.append((row, col))
                break
            else:
                break
            row += dr
            col += dc

    return moves


def get_diagonal_moves(start_row, start_col, board, is_white):
    """Retourne les mouvements en diagonale (utilisé par le fou et la reine)."""
    moves = []
    directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

    for dr, dc in directions:
        row, col = start_row + dr, start_col + dc
        while 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE:
            target_piece = board[row][col]
            if not target_piece:
                moves.append((row, col))
            elif target_piece.is_white != is_white:
                moves.append((row, col))
                break
            else:
                break
            row += dr
            col += dc

    return moves
