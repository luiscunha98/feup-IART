from elements.game.modes.modes import *


def play(main_menu):
    while True:
        SCREEN.blit(BG, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        PLAY_TEXT = get_font(45).render("Game Mode:", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(300, 100))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAYER_VS_PLAYER = Button(image=None, pos=(500, 250),
                                  text_input="PLAYER VS PLAYER", font=get_font(35), base_color="White",
                                  hovering_color="Red")
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
                    pvp(main_menu)
                if PLAYER_VS_CPU.checkForInput(PLAY_MOUSE_POS):
                    difficulty(main_menu, play, PVC)
                if CPU_VS_CPU.checkForInput(PLAY_MOUSE_POS):
                    difficulty(main_menu, play,CVC)
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()