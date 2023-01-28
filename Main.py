# All inital set up
from Board import Board
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
font = pygame.font.SysFont('timesnewroman',  50)

# Game starts from here
b.spawnTile()
b.spawnTile()

# Draw the board
while True:

    # The for loop is running but it is not looking up at the key events - maybe there needs to be a listener
    for event in pygame.event.get():
        flipped = False
        rotated = False
        played = True

        if event.type == pygame.KEYDOWN:
            print(f'Score: {b.score}')
            if event.key == pygame.K_b:
                pass
                # printBoard(board)
            if event.key == pygame.K_RIGHT:
                pass

            elif event.key == pygame.K_LEFT:

                b.board = b.flipBoard(b.board)
                flipped = True
            elif event.key == pygame.K_DOWN:

                b.board = b.transposeBoard(b.board)
                rotated = True
            elif event.key == pygame.K_UP:
                b.board = b.transposeBoard(b.board)
                b.board = b.flipBoard(b.board)
                rotated = True
                flipped = True
            else:
                played = False
        else:
            played = False

        if played:

            backup = b.board.copy()

            for i in range(0, 4):

                temp = b.operateRow(b.board[i])

                b.board[i] = temp

            boardChanged = b.compare(backup, b.board)

            if flipped == True:
                b.board = b.flipBoard(b.board)
            if rotated == True:
                b.board = b.transposeBoard(b.board)
            if boardChanged == True:
                b.spawnTile()
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
            if(b.board[i][j] != '0'):
                if b.board[i][j] == '2':
                    c = [238, 228, 218]
                elif b.board[i][j] == '4':
                    c = [237, 224, 200]
                elif b.board[i][j] == '8':
                    c = [242, 177, 121]
                elif b.board[i][j] == '16':
                    c = [245, 149, 99]
                elif b.board[i][j] == '32':
                    c = [246, 124, 95]
                elif b.board[i][j] == '64':
                    c = [246, 94, 59]
                elif b.board[i][j] == '128':
                    c = [237, 207, 114]
                elif b.board[i][j] == '256':
                    c = [237, 204, 97]
                elif b.board[i][j] == '512':
                    c = [237, 200, 80]
                elif b.board[i][j] == '1024':
                    c = [237, 197, 63]
                else:
                    c = [237, 194, 46]
            # Just need to get the text feature in there now
            pygame.draw.rect(surface=screen, color=c, rect=pygame.Rect(
                x, y, blockSize, blockSize))
            if b.board[i][j] != '0':
                if b.board[i][j] == '128' or b.board[i][j] == '256' or b.board[i][j] == '512':
                    text = font.render(b.board[i][j], True, (0, 0, 0))
                    screen.blit(text, (x+18, y+30))
                elif b.board[i][j] == '1024' or b.board[i][j] == '2048':
                    text = font.render(b.board[i][j], True, (0, 0, 0))
                    screen.blit(text, (x, y+30))
                else:
                    text = font.render(b.board[i][j], True, (0, 0, 0))
                    screen.blit(text, (x+30, y+30))
                # We want to display the text here for the user of what the current number is
    # if '2048' in b.board:
    #     gameWon = True
    # else:
    #     gameWon = False

    # if '0' in b.board:
    #     available = False
    # else:
    #     available = True

    # print(f'GameWon: {gameWon}')
    # print(f'Available: {available}')

    # if gameWon or not available:
    #     pygame.quit()
    #     print('Thanks for playing')
    #     break

    if b.isGameOver():
        pygame.quit()
        print('Thank you for playing')
        break

    pygame.display.flip()
