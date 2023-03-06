import pygame, sys
from button import Button

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.png")

def render_multi_line(text, x, y, fsize):
        lines = text.splitlines()
        for i, l in enumerate(lines):
            SCREEN.blit(get_font(30).render(l, 0, "Black"), (x, y + fsize*i))

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

def play():

    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("assets/board.png")

        PLAY_TEXT = get_font(45).render("Game Mode:", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Red")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:

                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()
    


def instructions():
    while True:
        INSTRUCTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        text = "Both players need four pieces to play.\nThe older player places their four pieces on four of the five forks around the outer ring.\nThe younger player places their four pieces on the central pentagon, each one on a fork opposite one of the older player’s pieces.\nThe older player takes the first turn. Thereafter players alternate.\nOn your turn, move one of your four pieces along a single edge to an empty adjacent fork.\nYou must move a piece.\nA piece is bound if is surrounded on all three sides, by any combination of players’ pieces.\nIf, at any time, one of your opponent’s pieces is bound, you have won the game."

        render_multi_line(text, 100, 200, 75)

        INSTRUCTIONS_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(30), base_color="Black", hovering_color="Red")

        INSTRUCTIONS_BACK.changeColor(INSTRUCTIONS_MOUSE_POS)
        INSTRUCTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if INSTRUCTIONS_BACK.checkForInput(INSTRUCTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(125).render("BOUND GAME", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(None, pos=(640, 375), 
                            text_input="PLAY", font=get_font(100), base_color="White", hovering_color="Red")
        INSTRUCTIONS_BUTTON = Button(None, pos=(640, 450), 
                            text_input="INSTRUCTIONS", font=get_font(30), base_color="White", hovering_color="Red")
        QUIT_BUTTON = Button(None, pos=(640, 500), 
                            text_input="QUIT", font=get_font(30), base_color="White", hovering_color="Red")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, INSTRUCTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if INSTRUCTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    instructions()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()