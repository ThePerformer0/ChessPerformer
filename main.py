import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Dimensions par défaut de la fenêtre
DEFAULT_WINDOW_SIZE = 800
BOARD_SIZE = 8  # Taille fixe du plateau en termes de carrés

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BEIGE = (240, 217, 181)
BROWN = (181, 136, 99)

# Créer la fenêtre
screen = None
WINDOW_SIZE = DEFAULT_WINDOW_SIZE
SQUARE_SIZE = WINDOW_SIZE // BOARD_SIZE

# Fonction pour dessiner le plateau
def draw_board():
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            color = BEIGE if (row + col) % 2 == 0 else BROWN
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

# Boucle principale
def main(window_size=DEFAULT_WINDOW_SIZE):
    global screen, WINDOW_SIZE, SQUARE_SIZE

    # Ajuster la taille de la fenêtre et des cases
    WINDOW_SIZE = window_size
    SQUARE_SIZE = WINDOW_SIZE // BOARD_SIZE
    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption("Chess Game by The Performer")

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Dessiner le plateau
        draw_board()

        # Mettre à jour l'affichage
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main(700)  # Taille personnalisée du plateau
