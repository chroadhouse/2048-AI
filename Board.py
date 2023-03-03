import random as r
import copy


class Board:
    # Creates an empty board
    def __init__(self):
        self.board = [['0', '0', '0', '0'],
                      ['0', '0', '0', '0'],
                      ['0', '0', '0', '0'],
                      ['0', '0', '0', '0']]

        self.score = 0

    # Slide row left or right
    def slideRow(self, row):
        temp = ['0', '0', '0', '0']
        index = 3
        for i in range(3, -1, -1):
            if row[i] != '0':
                temp[index] = row[i]
                index -= 1

        return temp

    # Combines the rows once they have being combined
    def combineRow(self, row, ignoreScore):
        for i in range(3, -1, -1):
            a = row[i]
            b = row[i-1]

            if a == b:
                #print(f'Column index {i}')
                row[i] = str((int(a) + int(b)))
                if not ignoreScore:
                    self.score += int(row[i])
                    # print(f'Score after this {self.score}')
                row[i-1] = '0'
        return row

    def operateRow(self, row, ignoreScore):
        row = self.slideRow(row)
        row = self.combineRow(row, ignoreScore)
        row = self.slideRow(row)
        return row

    def reverseList(self, tempList):
        reversedList = ['0', '0', '0', '0']
        j = 4
        for i in range(0, 4):
            reversedList[j-1] = tempList[i]
            j -= 1
        return reversedList

    def transposeBoard(self, tempBoard):
        newBoard = [['0', '0', '0', '0'],
                    ['0', '0', '0', '0'],
                    ['0', '0', '0', '0'],
                    ['0', '0', '0', '0']]
        for i in range(0, 4):
            for j in range(0, 4):
                newBoard[i][j] = tempBoard[j][i]
        return newBoard

    def flipBoard(self, tempBoard):
        for i in range(0, 4):
            tempBoard[i] = self.reverseList(tempBoard[i])
        return tempBoard

    def compare(self, a, b):
        for i in range(0, 4):
            for j in range(0, 4):
                if a[i][j] != b[i][j]:
                    return True
        return False

    def spawnTile(self):
        emptyList = []
        for i in range(0, 4):
            for j in range(0, 4):
                if self.board[i][j] == '0':
                    emptyList.append([i, j])

        randomTemp = r.randint(0, len(emptyList)-1)
        temp = r.randint(1, 10) / 10
        randomSpot = emptyList[randomTemp]
        if temp > 0.8:
            self.board[randomSpot[0]][randomSpot[1]] = '2'
        else:
            self.board[randomSpot[0]][randomSpot[1]] = '4'

    def isGameOver(self):
        # First check if you have won the game
        for r in self.board:
            for c in r:
                if c == '2048':
                    print('Won')
                    return True

        if not self.isLegalMove():
            return True  # The game is over
        return False

    def getPossibleMoves(self):
        # check whether you can move up down left or right
        # If you can returnt the moves you can do
        # If not return a empty list -- This can be done to check game over

        moves = ['left', 'right', 'up', 'down']
        possibleMoves = []

        for m in moves:
            # print(f'Move is {m}')
            tempBoard = self.board.copy()
            if m == 'left':
                tempBoard = self.flipBoard(tempBoard)
            elif m == 'right':
                # We do nothing
                pass
            elif m == 'down':
                tempBoard = self.transposeBoard(tempBoard)
            else:  # m is up
                tempBoard = self.transposeBoard(tempBoard)
                tempBoard = self.flipBoard(tempBoard)

            backup = tempBoard.copy()

            for i in range(0, 4):
                temp = self.operateRow(tempBoard[i], True)

                tempBoard[i] = temp

            boardChange = self.compare(backup, tempBoard)

            # Board has changed so we can make a legal move in one direction
            if boardChange:
                possibleMoves.append(m)

        return possibleMoves
        # The method was no broken so there must be not possible moves
        return False

    def isLegalMove(self):
        temp = self.getPossibleMoves()
        # print(temp)

        if temp:
            return True  # There are moves you can do
        else:
            return False

    def move(self, direction):
        flipped = False
        rotated = False
        played = True

        if direction == 'right':
            pass
        elif direction == 'left':
            self.board = self.flipBoard(self.board)
            flipped = True
        elif direction == 'down':
            self.board = self.transposeBoard(self.board)
            rotated = True
        elif direction == 'up':
            self.board = self.transposeBoard(self.board)
            rotated = True
            self.board = self.flipBoard(self.board)
            flipped = True
        else:
            played = False

        if played:
            backup = self.board.copy()
            for i in range(0, 4):
                temp = self.operateRow(self.board[i], ignoreScore=True)
                self.board[i] = temp

            boardChanged = self.compare(self.board, backup)

            if flipped:
                self.board = self.flipBoard(self.board)
            if rotated:
                self.board = self.transposeBoard(self.board)
            if boardChanged:
                self.spawnTile()

    def boardToInt(self):
        tempBoard = [map(int, i) for i in self.board]

        return tempBoard

    def getBoardScore(self):
        tempBoard = self.boardToInt()
        max = 0
        for r in tempBoard:
            for c in r:
                if c > max:
                    max = c
        if max == 32:
            return 1
        elif max == 64:
            return 2
        elif max == 128:
            return 3
        elif max == 256:
            return 4
        elif max == 512:
            return 5
        elif max == 1024:
            return 8
        elif max == 2048:
            return 10
        else:
            return 0

    def getState(self):
        state = []
        tempBoard = self.boardToInt()
        for row in tempBoard:
            for col in row:
                state.append(col)

        return state

    def step(self, action):
        # For the reward store the score and the highest tile
        # This is a kind of idea of stepping
        self.move(action)
        # This moves - now check that the game is done
        reward = self.getBoardScore()
        done = self.isGameOver()
        return self, reward, done

    def reset(self):
        print('Data has being reset')
        self.board = [['0', '0', '0', '0'],
                      ['0', '0', '0', '0'],
                      ['0', '0', '0', '0'],
                      ['0', '0', '0', '0']]

        self.score = 0
        self.spawnTile()
        self.spawnTile()

    def printBoard(self):
        for row in self.board:
            print(row)

    def boardForData(self):
        tempBoard = self.boardToInt()
        max = 0
        for r in tempBoard:
            for c in r:
                if c > max:
                    max = c

        return max, self.score
