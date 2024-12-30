from pieces import (
    get_pawn_moves, get_rook_moves, get_knight_moves, 
    get_bishop_moves, get_queen_moves, get_king_moves
)

class Board:
    def __init__(self):
        # Représentation initiale de l'échiquier (8x8)
        self.board = [
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        ]

    def get_piece(self, row, col):
        return self.board[row][col]
    

    def move_piece(self, start_row, start_col, end_row, end_col):
        """
        Déplace une pièce d'une case à une autre en validant le mouvement.
        :param start_row: Ligne de départ
        :param start_col: Colonne de départ
        :param end_row: Ligne d'arrivée
        :param end_col: Colonne d'arrivée
        :return: True si le mouvement est réussi, False sinon
        """
        piece = self.get_piece(start_row, start_col)

        if piece is None:
            return False

        # Validation basique pour éviter les mouvements hors échiquier
        if not (0 <= end_row < 8 and 0 <= end_col < 8):
            return False

        # Capture ou déplacement sur une case vide
        self.board[end_row][end_col] = piece
        self.board[start_row][start_col] = None
        return True

    def get_valid_moves(self, start_row, start_col):
        piece = self.get_piece(start_row, start_col)
        if not piece:
            return []

        is_white = piece.isupper()

        if piece.lower() == 'p':
            return get_pawn_moves(start_row, start_col, self.grid, is_white)
        elif piece.lower() == 'r':
            return get_rook_moves(start_row, start_col, self.grid, is_white)
        elif piece.lower() == 'n':
            return get_knight_moves(start_row, start_col, self.grid, is_white)
        elif piece.lower() == 'b':
            return get_bishop_moves(start_row, start_col, self.grid, is_white)
        elif piece.lower() == 'q':
            return get_queen_moves(start_row, start_col, self.grid, is_white)
        elif piece.lower() == 'k':
            return get_king_moves(start_row, start_col, self.grid, is_white)
        
        return []

