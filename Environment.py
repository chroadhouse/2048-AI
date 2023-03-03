import pygame
from Board import Board
import copy


class Environment():

    def __init__(self, agent=None) -> None:
        pygame.init()
        self.screenSize = 500
        self.blockSize = 100
        self.padding = 20
        self.screen = pygame.display.set_mode(
            (self.screenSize, self.screenSize))
        self.font = pygame.font.SysFont('timesnewroman', 50)
        self.b = Board()
        self.agent = agent
        self.numberOfMoves = 0

    def runHuman(self):
        self.b.reset()
        self.numberOfMoves = 0
        while True:

            # The for loop is running but it is not looking up at the key events - maybe there needs to be a listener
            for event in pygame.event.get():
                flipped = False
                rotated = False
                played = False

                if event.type == pygame.KEYDOWN:
                    print(f'Print: {self.b.score}')
                    if event.key == pygame.K_RIGHT:
                        played = True
                    elif event.key == pygame.K_LEFT:
                        self.b.board = self.b.flipBoard(self.b.board)
                        flipped = True
                        played = True
                    elif event.key == pygame.K_DOWN:
                        self.b.board = self.b.transposeBoard(self.b.board)
                        rotated = True
                        played = True
                    elif event.key == pygame.K_UP:
                        self.b.board = self.b.transposeBoard(self.b.board)
                        self.b.board = self.b.flipBoard(self.b.board)
                        rotated = True
                        flipped = True
                        played = True

                if played:

                    backup = self.b.board.copy()
                    for i in range(0, 4):
                        #print(f'Row index {i}')
                        temp = self.b.operateRow(self.b.board[i], False)
                        self.b.board[i] = temp

                    boardChanged = self.b.compare(backup, self.b.board)

                    if flipped:
                        self.b.board = self.b.flipBoard(self.b.board)
                    if rotated:
                        self.b.board = self.b.transposeBoard(self.b.board)
                    if boardChanged:
                        self.numberOfMoves += 1
                        print(f'Number of Moves: {self.numberOfMoves}')
                        self.b.spawnTile()
            # Screen background
            self.screen.fill([255, 255, 255])
            # background rectangle created
            pygame.draw.rect(surface=self.screen, color=[150, 150, 150], rect=pygame.Rect(
                0, 0, self.screenSize, self.screenSize))

            # Don't acc know why i need this here
            # pygame.display.flip()
            # Nest the loops and create the rectangles
            for i in range(0, 4):
                for j in range(0, 4):

                    x = self.padding+(self.padding+self.blockSize)*j
                    y = self.padding+(self.padding+self.blockSize)*i

                    c = [200, 200, 200]
                    if(self.b.board[i][j] != '0'):
                        if self.b.board[i][j] == '2':
                            c = [238, 228, 218]
                        elif self.b.board[i][j] == '4':
                            c = [237, 224, 200]
                        elif self.b.board[i][j] == '8':
                            c = [242, 177, 121]
                        elif self.b.board[i][j] == '16':
                            c = [245, 149, 99]
                        elif self.b.board[i][j] == '32':
                            c = [246, 124, 95]
                        elif self.b.board[i][j] == '64':
                            c = [246, 94, 59]
                        elif self.b.board[i][j] == '128':
                            c = [237, 207, 114]
                        elif self.b.board[i][j] == '256':
                            c = [237, 204, 97]
                        elif self.b.board[i][j] == '512':
                            c = [237, 200, 80]
                        elif self.b.board[i][j] == '1024':
                            c = [237, 197, 63]
                        else:
                            c = [237, 194, 46]
                    # Just need to get the text feature in there now
                    pygame.draw.rect(surface=self.screen, color=c, rect=pygame.Rect(
                        x, y, self.blockSize, self.blockSize))
                    if self.b.board[i][j] != '0':
                        if self.b.board[i][j] == '128' or self.b.board[i][j] == '256' or self.b.board[i][j] == '512':
                            text = self.font.render(
                                self.b.board[i][j], True, (0, 0, 0))
                            self.screen.blit(text, (x+18, y+30))
                        elif self.b.board[i][j] == '1024' or self.b.board[i][j] == '2048':
                            text = self.font.render(
                                self.b.board[i][j], True, (0, 0, 0))
                            self.screen.blit(text, (x, y+30))
                        else:
                            text = self.font.render(
                                self.b.board[i][j], True, (0, 0, 0))
                            self.screen.blit(text, (x+30, y+30))
                        # We want to display the text here for the user of what the current number is

            if self.b.isGameOver():
                self.b.printBoard()
                pygame.quit()
                print('Thank you for playing')
                break

            pygame.display.flip()
        return self.b, self.numberOfMoves

    def runAgent(self):
        self.b.reset()
        self.numberOfMoves = 0
        while True:

            flipped = False
            rotated = False
            played = True
            tempBoard = copy.deepcopy(self.b)
            move = self.agent.act(tempBoard)
            print(move)
            if move == 'left':
                self.b.board = self.b.flipBoard(self.b.board)
                flipped = True
            elif move == 'right':
                pass
            elif move == 'up':
                self.b.board = self.b.transposeBoard(self.b.board)
                self.b.board = self.b.flipBoard(self.b.board)
                flipped = True
                rotated = True
            elif move == 'down':
                self.b.board = self.b.transposeBoard(self.b.board)
                rotated = True
            else:
                played = False

            if played:
                backup = self.b.board.copy()
                for i in range(0, 4):
                    temp = self.b.operateRow(self.b.board[i], False)
                    self.b.board[i] = temp

                boardChanged = self.b.compare(backup, self.b.board)

                if flipped:
                    self.b.board = self.b.flipBoard(self.b.board)
                if rotated:
                    self.b.board = self.b.transposeBoard(self.b.board)
                if boardChanged:
                    self.numberOfMoves += 1
                    print(f'Number of Moves: {self.numberOfMoves}')
                    print(f'Print: {self.b.score}')
                    self.b.spawnTile()

            self.screen.fill([255, 255, 255])
            # background rectangle created
            pygame.draw.rect(surface=self.screen, color=[150, 150, 150], rect=pygame.Rect(
                0, 0, self.screenSize, self.screenSize))

            # Don't acc know why i need this here
            # pygame.display.flip()
            # Nest the loops and create the rectangles
            for i in range(0, 4):
                for j in range(0, 4):

                    x = self.padding+(self.padding+self.blockSize)*j
                    y = self.padding+(self.padding+self.blockSize)*i

                    c = [200, 200, 200]
                    if(self.b.board[i][j] != '0'):
                        if self.b.board[i][j] == '2':
                            c = [238, 228, 218]
                        elif self.b.board[i][j] == '4':
                            c = [237, 224, 200]
                        elif self.b.board[i][j] == '8':
                            c = [242, 177, 121]
                        elif self.b.board[i][j] == '16':
                            c = [245, 149, 99]
                        elif self.b.board[i][j] == '32':
                            c = [246, 124, 95]
                        elif self.b.board[i][j] == '64':
                            c = [246, 94, 59]
                        elif self.b.board[i][j] == '128':
                            c = [237, 207, 114]
                        elif self.b.board[i][j] == '256':
                            c = [237, 204, 97]
                        elif self.b.board[i][j] == '512':
                            c = [237, 200, 80]
                        elif self.b.board[i][j] == '1024':
                            c = [237, 197, 63]
                        else:
                            c = [237, 194, 46]
                    # Just need to get the text feature in there now
                    pygame.draw.rect(surface=self.screen, color=c, rect=pygame.Rect(
                        x, y, self.blockSize, self.blockSize))
                    if self.b.board[i][j] != '0':
                        if self.b.board[i][j] == '128' or self.b.board[i][j] == '256' or self.b.board[i][j] == '512':
                            text = self.font.render(
                                self.b.board[i][j], True, (0, 0, 0))
                            self.screen.blit(text, (x+18, y+30))
                        elif self.b.board[i][j] == '1024' or self.b.board[i][j] == '2048':
                            text = self.font.render(
                                self.b.board[i][j], True, (0, 0, 0))
                            self.screen.blit(text, (x, y+30))
                        else:
                            text = self.font.render(
                                self.b.board[i][j], True, (0, 0, 0))
                            self.screen.blit(text, (x+30, y+30))
                        # We want to display the text here for the user of what the current number is

            if self.b.isGameOver():
                self.b.printBoard()
                pygame.quit()
                return self.b, self.numberOfMoves

            pygame.display.flip()
            # Here the agent will play the game
