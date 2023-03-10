import pygame

SCREEN = pygame.display.set_mode((1280, 720))
BG = pygame.image.load("resources/images/Background.png")
PVP = 1
PVC = 2
CVC = 3
E = 1
M = 2
H = 3

BLUE = (0, 0, 255)

BLACK = (0 , 0, 0)

WHITE = (255, 255 ,255)

POSITIONS  = [(568, 190), (585, 238), (410, 400), (475, 395),
            (555, 340), (670, 305), (770, 305), (825, 268),
            (608, 372), (655, 355), (563, 460), (605, 425),
            (653, 445), (685, 400), (737, 400), (590, 555),
            (670, 495), (773, 500), (570, 612), (820, 530)]

PIECE_RADIUS = 19

def distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5