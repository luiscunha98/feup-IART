from game.elements.dificulty.dificulty import *
from functions.auxiliar import *

def play(main_menu):

    while True:

        #base
        SCREEN.blit(BG, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        PLAY_TEXT = get_font(45).render("Game Mode:", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(300, 100))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        #button definition
        PLAYER_VS_PLAYER = Button(image=None, pos=(500, 250), text_input="PLAYER VS PLAYER", font=get_font(35), base_color="White", hovering_color="Red")
        PLAYER_VS_CPU = Button(image=None, pos=(447, 350), text_input="PLAYER VS CPU", font=get_font(35), base_color="White", hovering_color="Red")
        CPU_VS_CPU = Button(image=None, pos=(395, 450), text_input="CPU VS CPU", font=get_font(35), base_color="White", hovering_color="Red")
        PLAY_BACK = Button(image=None, pos=(640, 600), text_input="BACK", font=get_font(50), base_color="White", hovering_color="Red")

        # button hover changes and update
        for button in [PLAYER_VS_PLAYER, PLAYER_VS_CPU, CPU_VS_CPU, PLAY_BACK]:
            button.changeColor(PLAY_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            quit_game(event)

            #select mode
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAYER_VS_PLAYER.checkForInput(PLAY_MOUSE_POS):
                    difficulty(main_menu, play, PVP)
                if PLAYER_VS_CPU.checkForInput(PLAY_MOUSE_POS):
                    difficulty(main_menu, play, PVC)
                if CPU_VS_CPU.checkForInput(PLAY_MOUSE_POS):
                    dif1 = difficulty1(main_menu, play)
                    difficulty2(main_menu, play, dif1)
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def instructions(main_menu):

    while True:

        #base
        SCREEN.blit(BG, (0, 0))
        INSTRUCTIONS_MOUSE_POS = pygame.mouse.get_pos()
        text = "Both players need four pieces to play. The older player\nplaces their four pieces on four of the five forks around\nthe outer ring. The younger player places their four pieces\non the central pentagon, each one on a fork opposite one of\nthe older player’s pieces. The older player takes the first\nturn. Thereafter players alternate. On your turn, move one of\nyour four pieces along a single edge to an empty adjacent\nfork. You must move a piece. A piece is bound if is\nsurrounded on all three sides, by any combination of\nplayers’ pieces. If, at any time, one of your opponent’s\npieces is bound, you have won the game."
        render_multi_line(text, 50, 100, 20)

        # button definition, hover changes and update
        INSTRUCTIONS_BACK = Button(image=None, pos=(640, 650), text_input="BACK", font=get_font(30), base_color="White", hovering_color="Red")
        INSTRUCTIONS_BACK.changeColor(INSTRUCTIONS_MOUSE_POS)
        INSTRUCTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            quit_game(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if INSTRUCTIONS_BACK.checkForInput(INSTRUCTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()