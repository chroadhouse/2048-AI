import pygame
import random as r
import sys
pygame.init()


screen_width = 500
screen_height = 500
blockSize = 100
padding = 20
score = 0
screen = pygame.display.set_mode((screen_width, screen_height))

# Create a 4x4 board
board = [['0', '0', '0', '0'],
         ['0', '0', '0', '0'],
         ['0', '0', '0', '0'],
         ['0', '0', '0', '0']]


def printBoard():
    for row in board:
        print(row)


def spawnTile():
    emptyX = []
    emptyY = []
    for i in range(0, 4):
        for j in range(0, 4):
            # print(board[i][j])
            if board[i][j] == '0':
                emptyX.append(i)
                emptyY.append(j)

    randomPlace = r.randint(0, (len(emptyX)-1))

    randomX = emptyX[randomPlace]
    randomY = emptyY[randomPlace]
    temp = r.randint(1, 10) / 10
    if temp > 0.8:
        board[randomX][randomY] = 2
    else:
        board[randomX][randomY] = 4


def slideRow(row):
    # Slides the row to the other side
    if row is None:
        print('Fuck')
    temp = ['0', '0', '0', '0']
    index = 3
    for i in range(3, 0, -1):
        if row[i] != '0':
            temp[index] = row[i]
            index -= 1
    return temp


def combineRow(row):
    for i in range(3, 0, -1):
        a = row[i]
        b = row[i-1]
        # If they are the same value then they need to be combined
        if a == b:
            tempA = int(a)
            tempB = int(b)
            temp = tempA + tempB
            row[i] = str(temp)
            # score += row[i]
            row[i-1] = '0'
    return row


def operateRow(row):
    # print(row)
    row = slideRow(row)
    # print(row)
    row = combineRow(row)
    # print(row)
    row = slideRow(row)
    # print(row)
    return row


def reverseList(tempList=[]):
    reversedList = [0, 0, 0, 0]
    j = 4
    for i in range(0, 4):
        reversedList[j-1] = tempList[i]
        j -= 1


def transposeBoard(tempBoard):
    newBoard = [['0', '0', '0', '0'],
                ['0', '0', '0', '0'],
                ['0', '0', '0', '0'],
                ['0', '0', '0', '0']]
    for i in range(0, 4):
        for j in range(0, 4):
            newBoard[i][j] = tempBoard[j][i]
    return newBoard


def flipBoard(tempBoard):
    # Think i can do this using for row in tempBoard -> will test this later
    for i in range(0, 3):
        tempBoard[i] = reverseList(tempBoard[i])


def compare(a, b):
    for i in range(0, 4):
        for j in range(0, 4):
            if a[i][j] != b[i][j]:
                return True

    return False


# Game starts from here
spawnTile()
spawnTile()

printBoard()

# Draw the board
while True:

    # The for loop is running but it is not looking up at the key events - maybe there needs to be a listener
    for event in pygame.event.get():
        # print('running')
        flipped = False
        rotated = False
        played = True

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RIGHT:
                print('RIGHT KEY BEING PRESSED')

            elif event.key == pygame.K_LEFT:
                print('LEFT KEY BEING PRESSED')
                board = flipBoard(board)
                flipped = True
            elif event.key == pygame.K_DOWN:
                print('DOWN KEY BEING PRESSED')
                board = transposeBoard(board)
                rotated = True
            elif event.key == pygame.K_UP:
                print('UP KEY BEING PRESSED')
                board = transposeBoard(board)
                board = flipBoard(board)
                rotated = True
                flipped = True
            else:
                played = False
        else:
            played = False

        if played:
            # backup = [['0', '0', '0', '0'],
            #           ['0', '0', '0', '0'],
            #           ['0', '0', '0', '0'],
            #           ['0', '0', '0', '0']]

            # for i in range(0, 4):
            #     for j in range(0, 4):
            #         backup[i][j] = board[i][j]

            backup = board
            #print(f'backup is : {backup}')

            for i in range(0, 4):
                # for row in board:
                # row = operateRow(row)
                board[i] = operateRow(board[i])

            boardChanged = compare(backup, board)
            print(boardChanged)
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
            temp = board[i][j]
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

            pygame.draw.rect(surface=screen, color=c, rect=pygame.Rect(
                x, y, blockSize, blockSize))
    # print('********************')
    # printBoard()
    # print('********************')
    available, gameWon = False, False
    for i in range(0, 4):
        for j in range(0, 4):
            if board[i][j] == '2048':
                gameWon = True

    pygame.display.flip()
