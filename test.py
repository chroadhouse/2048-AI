import Board

import pygame


import copy
pygame.init()

b = Board()

screen_width = 500
screen_height = 500
blockSize = 100
padding = 20
score = 0
screen = pygame.display.set_mode((screen_width, screen_height))

# Game starts from here
b.spawnTile()
b.spawnTile()

# printBoard(board)

# Draw the board
while True:

    # The for loop is running but it is not looking up at the key events - maybe there needs to be a listener
    for event in pygame.event.get():
        flipped = False
        rotated = False
        played = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                pass
                # printBoard(board)
            if event.key == pygame.K_RIGHT:
                pass

            elif event.key == pygame.K_LEFT:

                board = flipBoard(board)
                flipped = True
            elif event.key == pygame.K_DOWN:

                board = transposeBoard(board)
                rotated = True
            elif event.key == pygame.K_UP:

                board = transposeBoard(board)
                board = flipBoard(board)
                rotated = True
                flipped = True
            else:
                played = False
        else:
            played = False

        if played:

            backup = board.copy()

            for i in range(0, 4):

                temp = operateRow(board[i])

                board[i] = temp

            boardChanged = compare(backup, board)

            if flipped == True:
                board = flipBoard(board)
            if rotated == True:
                board = transposeBoard(board)
            if boardChanged == True:
                spawnTile()
    # Screen background
    screen.fill([255, 255, 255])
    # background rectangle created
    pygame.draw.rect(surface=screen, color=[150, 150, 150], rect=pygame.Rect(
        0, 0, screen_width, screen_height))
    # Don't acc know why i need this here
    # pygame.display.flip()
    # Nest the loops and create the rectangles
    for i in range(0, 4):
        for j in range(0, 4):

            x = padding+(padding+blockSize)*j
            y = padding+(padding+blockSize)*i

            c = [200, 200, 200]
            if(board[i][j] != '0'):
                if board[i][j] == '2':
                    c = [238, 228, 218]
                elif board[i][j] == '4':
                    c = [237, 224, 200]
                elif board[i][j] == '8':
                    c = [242, 177, 121]
                elif board[i][j] == '16':
                    c = [245, 149, 99]
                elif board[i][j] == '32':
                    c = [246, 124, 95]
                elif board[i][j] == '64':
                    c = [246, 94, 59]
                elif board[i][j] == '128':
                    c = [237, 207, 114]
                elif board[i][j] == '256':
                    c = [237, 204, 97]
                elif board[i][j] == '512':
                    c = [237, 200, 80]
                elif board[i][j] == '1024':
                    c = [237, 197, 63]
                else:
                    c = [237, 194, 46]
            # Just need to get the text feature in there now
            pygame.draw.rect(surface=screen, color=c, rect=pygame.Rect(
                x, y, blockSize, blockSize))
            if board[i][j] != '0':
                if board[i][j] == '128' or board[i][j] == '256' or board[i][j] == '512':
                    text = font.render(board[i][j], True, (0, 0, 0))
                    screen.blit(text, (x+18, y+30))
                elif board[i][j] == '1024' or board[i][j] == '2048':
                    text = font.render(board[i][j], True, (0, 0, 0))
                    screen.blit(text, (x, y+30))
                else:
                    text = font.render(board[i][j], True, (0, 0, 0))
                    screen.blit(text, (x+30, y+30))
                # We want to display the text here for the user of what the current number is
    if '2048' in board:
        gameWon = True
    else:
        gameWon = False

    if '0' in board:
        available = True
    else:
        available = False

    if gameWon or available:
        pygame.quit()
        break

    pygame.display.flip()
