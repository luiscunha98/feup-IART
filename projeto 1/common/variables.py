import pygame
from common.classes.position import *

POSITIONS = [
    Position(568, 190), #0
    Position(585, 238), #1
    Position(410, 400), #2
    Position(475, 395), #3
    Position(555, 340), #4
    Position(670, 305), #5
    Position(770, 305), #6
    Position(825, 268), #7
    Position(608, 372), #8
    Position(655, 355), #9
    Position(563, 460), #10
    Position(605, 425), #11
    Position(653, 445), #12
    Position(685, 400), #13
    Position(737, 400), #14
    Position(590, 555), #15
    Position(670, 495), #16
    Position(773, 500), #17
    Position(570, 612), #18
    Position(820, 530)] #19

for i in range(20):
    POSITIONS[i].set_busy(False)

POSITIONS[0].possible_moves(POSITIONS[1], POSITIONS[2], POSITIONS[7])
POSITIONS[1].possible_moves(POSITIONS[0], POSITIONS[4], POSITIONS[5])
POSITIONS[2].possible_moves(POSITIONS[3], POSITIONS[0], POSITIONS[18])
POSITIONS[3].possible_moves(POSITIONS[2], POSITIONS[4], POSITIONS[10])
POSITIONS[4].possible_moves(POSITIONS[3], POSITIONS[1], POSITIONS[8])
POSITIONS[5].possible_moves(POSITIONS[9], POSITIONS[6], POSITIONS[1])
POSITIONS[6].possible_moves(POSITIONS[7], POSITIONS[14], POSITIONS[5])
POSITIONS[7].possible_moves(POSITIONS[6], POSITIONS[0], POSITIONS[19])
POSITIONS[8].possible_moves(POSITIONS[9], POSITIONS[4], POSITIONS[11])
POSITIONS[9].possible_moves(POSITIONS[8], POSITIONS[13], POSITIONS[16])
POSITIONS[10].possible_moves(POSITIONS[11], POSITIONS[3], POSITIONS[15])
POSITIONS[11].possible_moves(POSITIONS[10], POSITIONS[12], POSITIONS[8])
POSITIONS[12].possible_moves(POSITIONS[16], POSITIONS[11], POSITIONS[13])
POSITIONS[13].possible_moves(POSITIONS[12], POSITIONS[14], POSITIONS[9])
POSITIONS[14].possible_moves(POSITIONS[13], POSITIONS[6], POSITIONS[17])
POSITIONS[15].possible_moves(POSITIONS[18], POSITIONS[10], POSITIONS[16])
POSITIONS[16].possible_moves(POSITIONS[17], POSITIONS[12], POSITIONS[15])
POSITIONS[17].possible_moves(POSITIONS[16], POSITIONS[19], POSITIONS[14])
POSITIONS[18].possible_moves(POSITIONS[15], POSITIONS[19], POSITIONS[2])
POSITIONS[19].possible_moves(POSITIONS[18], POSITIONS[17], POSITIONS[7])




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


PIECE_RADIUS = 19

