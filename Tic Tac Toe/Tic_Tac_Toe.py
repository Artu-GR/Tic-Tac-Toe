
from pickle import TRUE
import pygame
import random

from pygame.constants import SCRAP_SELECTION

pygame.init()

width = 512
height = 512

dimension = 3

sq_size = width/3

board = [
        ["--", "--", "--"],
        ["--", "--", "--"],
        ["--", "--", "--"]
    ]

Images = {}
occupied = [0]

def loadImages():
    pieces = ["Circle", "Cross"]
    for piece in pieces:
        Images[piece] = pygame.transform.scale(pygame.image.load("Players/" + piece + ".png"), (150, 150))

def main():
    screen = pygame.display.set_mode((width, height))
    screen.fill(pygame.Color("white"))
    running = True

    player1 = True

    loadImages()

    plays = int(input("Select players: \n1 or 2\n"))

    while running:
        for action in pygame.event.get():
            if action.type == pygame.QUIT:
                running = False
            elif action.type == pygame.MOUSEBUTTONDOWN:
                location = pygame.mouse.get_pos()
                col = int(location[0] // sq_size)
                row = int(location[1] // sq_size)
                if plays == 2:
                    if player1:
                        if board[row][col] == "--":
                           board[row][col] = "Circle"
                           player1 = not player1
                    else:
                        if board[row][col] == "--":
                           board[row][col] = "Cross"
                           player1 = not player1
                else:
                    if board[row][col] == "--":
                        board[row][col] = "Circle"
                        if row == 0:
                            occupied.append(col+1)
                        elif row == 1:
                            occupied.append(col+4)
                        elif row == 2:
                            occupied.append(col+7)
                        if checkWin(screen, board, row, col) == True:
                            AI_Move(board, occupied)
                running = checkWin(screen, board, row, col)
        drawBoard(screen, board)
        pygame.display.flip()
        if running == False:
            running = True
            print("Press 'Esc' to exit\n\n")
            while running:
                for move in pygame.event.get():
                    if move.type == pygame.KEYDOWN:
                        if move.key == pygame.K_ESCAPE:
                            running = False
                            break

def drawBoard(screen, board):
    colors = [pygame.Color("black"), pygame.Color("white")]
    pygame.draw.rect(screen, colors[0], pygame.Rect(160, 0, 10, 512))
    pygame.draw.rect(screen, colors[0], pygame.Rect(340, 0, 10, 512))
    pygame.draw.rect(screen, colors[0], pygame.Rect(0, 160, 512, 10))
    pygame.draw.rect(screen, colors[0], pygame.Rect(0, 340, 512, 10))
    for r in range(dimension):
        for c in range(dimension):
            piece = board[r][c]
            if piece != "--":
                screen.blit(Images[piece], pygame.Rect(c*sq_size, r*sq_size, sq_size,sq_size))

def checkWin(screen, board, r, c):
    if board[0][0] == board[0][1] and board[0][1] == board[0][2] and board[0][0] != "--":
        print(board[0][0], " WIN!")
        return False
    if board[1][0] == board[1][1] and board[1][1] == board[1][2] and board[1][0] != "--":
        print(board[1][0], " WIN!")
        return False
    if board[2][0] == board[2][1] and board[2][1] == board[2][2] and board[2][0] != "--":
        print(board[2][0], " WIN!")
        return False
    if board[0][0] == board[1][0] and board[1][0] == board[2][0] and board[0][0] != "--":
        print(board[0][0], " WIN!")
        return False
    if board[0][1] == board[1][1] and board[1][1] == board[2][1] and board[0][1] != "--":
        print(board[0][1], " WIN!")
        return False
    if board[0][2] == board[1][2] and board[1][2] == board[2][2] and board[0][2] != "--":
        print(board[0][2], " WIN!")
        return False
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[1][1] != "--":
        print(board[1][1], " WIN!")
        return False
    if board[2][0] == board[1][1] and board[1][1] == board[0][2] and board[1][1] != "--":
        print(board[1][1], " WIN!")
        return False
    return True

def AI_Move(board, occupied):
    pos = 0;
    while(pos in occupied):
       pos = random.randint(1, 9)
    if pos == 1 and board[0][0] == "--":
        board[0][0] = "Cross"
    if pos == 2 and board[0][1] == "--":
        board[0][1] = "Cross"
    if pos == 3 and board[0][2] == "--":
        board[0][2] = "Cross"
    if pos == 4 and board[1][0] == "--":
        board[1][0] = "Cross"
    if pos == 5 and board[1][1] == "--":
        board[1][1] = "Cross"
    if pos == 6 and board[1][2] == "--":
        board[1][2] = "Cross"
    if pos == 7 and board[2][0] == "--":
        board[2][0] = "Cross"
    if pos == 8 and board[2][1] == "--":
        board[2][1] = "Cross"
    if pos == 9 and board[2][2] == "--":
        board[2][2] = "Cross"
    occupied.append(pos)
    print(pos, "*****", sorted(occupied), "\n")

if __name__ == "__main__":
    main()