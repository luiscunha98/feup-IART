import pygame, sys
from button import Button

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

PVP = 1
PVC = 2
CVC = 3

E = 1
M = 2
H = 3

BG = pygame.image.load("assets/Background.png")

def render_multi_line(text, x, y, fsize):
        lines = text.splitlines()
        for i, l in enumerate(lines):
            SCREEN.blit(get_font(30).render(l, 0, "White"), (x, y + fsize*2*i))

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

def play():

    while True:
        SCREEN.blit(BG, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        #BOARD = pygame.image.load("assets/board.png")
        #SCREEN.blit(BOARD, (0, 0))
        PLAY_TEXT = get_font(45).render("Game Mode:", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(300, 100))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAYER_VS_PLAYER = Button(image=None, pos=(500, 250), 
                            text_input="PLAYER VS PLAYER", font=get_font(35), base_color="White", hovering_color="Red")
        PLAYER_VS_PLAYER.changeColor(PLAY_MOUSE_POS)
        PLAYER_VS_PLAYER.update(SCREEN)

        PLAYER_VS_CPU = Button(image=None, pos=(447, 350), 
                            text_input="PLAYER VS CPU", font=get_font(35), base_color="White", hovering_color="Red")
        PLAYER_VS_CPU.changeColor(PLAY_MOUSE_POS)
        PLAYER_VS_CPU.update(SCREEN)

        CPU_VS_CPU = Button(image=None, pos=(395, 450), 
                            text_input="CPU VS CPU", font=get_font(35), base_color="White", hovering_color="Red")
        CPU_VS_CPU.changeColor(PLAY_MOUSE_POS)
        CPU_VS_CPU.update(SCREEN)

        PLAY_BACK = Button(image=None, pos=(640, 600), 
                            text_input="BACK", font=get_font(50), base_color="White", hovering_color="Red")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAYER_VS_PLAYER.checkForInput(PLAY_MOUSE_POS):
                    pvp()
                if PLAYER_VS_CPU.checkForInput(PLAY_MOUSE_POS):
                    difficulty(PVC)
                if CPU_VS_CPU.checkForInput(PLAY_MOUSE_POS):
                    difficulty(CVC)
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()
    


def instructions():
    while True:
        SCREEN.blit(BG, (0, 0))
        INSTRUCTIONS_MOUSE_POS = pygame.mouse.get_pos()

        text = "Both players need four pieces to play.\nThe older player places their four pieces on four of the five forks around the outer ring.\nThe younger player places their four pieces on the central pentagon, each one on a fork opposite one of the older player’s pieces.\nThe older player takes the first turn. Thereafter players alternate.\nOn your turn, move one of your four pieces along a single edge to an empty adjacent fork.\nYou must move a piece.\nA piece is bound if is surrounded on all three sides, by any combination of players’ pieces.\nIf, at any time, one of your opponent’s pieces is bound, you have won the game."

        render_multi_line(text, 75, 200, 25)

        INSTRUCTIONS_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(30), base_color="White", hovering_color="Red")

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

def difficulty(mode):
    while True:
        SCREEN.blit(BG, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        
        PLAY_TEXT = get_font(45).render("Difficulty:", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(300, 100))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        EASY = Button(image=None, pos=(300, 250), 
                            text_input="EASY", font=get_font(35), base_color="White", hovering_color="Red")
        EASY.changeColor(PLAY_MOUSE_POS)
        EASY.update(SCREEN)

        MEDIUM = Button(image=None, pos=(335, 350), 
                            text_input="MEDIUM", font=get_font(35), base_color="White", hovering_color="Red")
        MEDIUM.changeColor(PLAY_MOUSE_POS)
        MEDIUM.update(SCREEN)

        HARD = Button(image=None, pos=(300, 450), 
                            text_input="HARD", font=get_font(35), base_color="White", hovering_color="Red")
        HARD.changeColor(PLAY_MOUSE_POS)
        HARD.update(SCREEN)

        PLAY_BACK = Button(image=None, pos=(640, 600), 
                            text_input="BACK", font=get_font(50), base_color="White", hovering_color="Red")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if EASY.checkForInput(PLAY_MOUSE_POS):
                    if mode == PVC:
                        pvc(E)
                    else:
                        cvc(E)        
                if MEDIUM.checkForInput(PLAY_MOUSE_POS):
                    if mode == PVC:
                        pvc(M)
                    else:
                        cvc(M) 
                if HARD.checkForInput(PLAY_MOUSE_POS):
                    if mode == PVC:
                        pvc(H)
                    else:
                        cvc(H) 
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    play()

        pygame.display.update()

def pvp():
    while True:
        SCREEN.blit(BG, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        #BOARD = pygame.image.load("assets/board.png")
        #SCREEN.blit(BOARD, (0, 0))
        PLAY_TEXT = get_font(45).render("PLAYER VS PLAYER", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(400, 100))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 600), 
                            text_input="BACK", font=get_font(50), base_color="White", hovering_color="Red")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    play()

        pygame.display.update()

def pvc(dif):
    while True:
        SCREEN.blit(BG, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        #BOARD = pygame.image.load("assets/board.png")
        #SCREEN.blit(BOARD, (0, 0))
        PLAY_TEXT = get_font(45).render("PLAYER VS CPU", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(400, 100))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 600), 
                            text_input="BACK", font=get_font(50), base_color="White", hovering_color="Red")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    difficulty(PVC)

        pygame.display.update()

def cvc(dif):
    while True:
        SCREEN.blit(BG, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        #BOARD = pygame.image.load("assets/board.png")
        #SCREEN.blit(BOARD, (0, 0))
        PLAY_TEXT = get_font(45).render("CPU VS CPU", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(400, 100))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 600), 
                            text_input="BACK", font=get_font(50), base_color="White", hovering_color="Red")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    difficulty(CVC)

        pygame.display.update()

main_menu()