from common.functions import *
from common.classes.button import *


def game_over(player_turn):
    if player_turn == 1:
        # Load the p1 wins image
        game_over_image = pygame.image.load("resources/images/p1wins.png")
    elif player_turn == 2:
        # Load the p2 wins image
        game_over_image = pygame.image.load("resources/images/p2wins.png")

    # Resize the image to fit the screen
    game_over_image = pygame.transform.scale(game_over_image, (520, 500))

    # Get the size of the screen
    screen_width, screen_height = pygame.display.get_surface().get_size()

    # Calculate the x and y coordinates to center the image
    x = (screen_width - game_over_image.get_width()) // 2
    y = (screen_height - game_over_image.get_height()) // 2

    # Display the image on the screen
    SCREEN.blit(game_over_image, (x, y))

    # Update the display
    pygame.display.update()
