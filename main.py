# Example file showing a circle moving on screen
import pygame
from sys import exit

# pygame setup
pygame.init()
screen = pygame.display.set_mode((720, 720))
screen.fill("black")
pygame.display.set_caption('DAMA')  # window name
clock = pygame.time.Clock()         # creating object *clock*

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()               # zavrie pygame ale nie cyklus
            exit()                      # zavrie cyklus - z knižnice *sys*

    pygame.display.update()
    clock.tick(60)                      # obmedzi *while* loop na 60 opakovaní za 1s

    # pozície rohov prvého štvorca: a,b,c,d
    a = 26
    b = 26
    c = 80
    d = 80

    board_pos = [[0] * 8] * 8           # zadefinovanie pola hracej plochy - obsahuje zápis pozície rohov štvorcov

    for j in range(0, 8):  # rows

        for i in range(0, 8):  # fields
            rec_pos = [a, b, c, d]      # vytvorenie pola rohov štvorca
            board_pos[j][i] = rec_pos   # zápis pozície rohov štvorca

            if j % 2 == 0:
                if i % 2 == 0:
                    pygame.draw.rect(screen, "white", rec_pos)

                else:
                    pygame.draw.rect(screen, "green", rec_pos)

            elif i % 2 == 1:
                pygame.draw.rect(screen, "white", rec_pos)

            else:
                pygame.draw.rect(screen, "green", rec_pos)

            a += 84     # posun štvorca o jedno v pravo

        a  = 26         # vrátenie sa na začiatok riadku
        b += 84         # posun štvorca o riadok nižšie
    print(board_pos)


