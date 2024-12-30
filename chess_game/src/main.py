import pygame
import sys

from board import Board

# Initialisation de Pygame
pygame.init()

# Dimension et Couleurs
WINDOW_SIZE = 600
BOARD_SIZE = 8
SQUARE_SIZE = WINDOW_SIZE // BOARD_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (234, 234, 233)
GREEN = (6, 212, 147)
HIGHLIGHT_COLOR = (255, 255, 0)

PIECE_IMAGES = {
        'P': pygame.image.load('chess_game/images/wp.png'),
        'R': pygame.image.load('chess_game/images/wR.png'),
        'r': pygame.image.load('chess_game/images/bR.png'),
        'N': pygame.image.load('chess_game/images/wN.png'),
        'p': pygame.image.load('chess_game/images/bp.png'),
        'n': pygame.image.load('chess_game/images/bN.png'),
        'B': pygame.image.load('chess_game/images/wB.png'),
        'b': pygame.image.load('chess_game/images/bB.png'),
        'Q': pygame.image.load('chess_game/images/wQ.png'),
        'q': pygame.image.load('chess_game/images/bQ.png'),
        'K': pygame.image.load('chess_game/images/wK.png'),
        'k': pygame.image.load('chess_game/images/bK.png'),
    }


# Initialisation de l'écran
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Chess Game by The Performer")

# Fonction pour dessiner le plateau
def draw_board():
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            color = GRAY if (row + col) % 2 == 0 else GREEN
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

# Fonction pour initialiser les pièces sur l'échiquier
def draw_pieces(chess_board):
    """Dessine les pièces en fonction de l'état du plateau."""
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            piece = chess_board.get_piece(row, col)
            if piece:
                piece_image = PIECE_IMAGES[piece]
                piece_image = pygame.transform.scale(piece_image, (SQUARE_SIZE, SQUARE_SIZE))
                screen.blit(piece_image, (col * SQUARE_SIZE, row * SQUARE_SIZE))


def draw_valid_moves(valid_moves):
    for row, col in valid_moves:
        pygame.draw.rect(
            screen,
            HIGHLIGHT_COLOR,
            (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE),
            5  # Épaisseur du contour
        )


def main():
    chess_board = Board()
    selected_piece = None
    valid_moves = []

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                col = mouse_x // SQUARE_SIZE
                row = mouse_y // SQUARE_SIZE

                if selected_piece is None:
                    # Sélectionner une pièce
                    selected_piece = (row, col)
                else:
                    # Déplacer une pièce
                    start_row, start_col = selected_piece
                    if chess_board.move_piece(start_row, start_col, row, col):
                        selected_piece = None  # Réinitialiser la sélection après un déplacement valide
                    else:
                        selected_piece = None  # Annuler la sélection en cas de mouvement invalide

        # Dessiner l'échiquier et les pièces
        draw_board()
        if valid_moves:
            draw_valid_moves(valid_moves)
        draw_pieces(chess_board)
        pygame.display.flip()


if __name__ == "__main__":
    main()