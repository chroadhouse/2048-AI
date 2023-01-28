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
                row[i] = str((int(a) + int(b)))
                if not ignoreScore:
                    self.score += int(row[i])
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
            #print(f'Move is {m}')
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
                temp = self.operateRow(self.board[i], ignoreScore=False)
                self.board[i] = temp

            boardChanged = self.compare(self.board, backup)

            if flipped:
                self.board = self.flipBoard(self.board)
            if rotated:
                self.board = self.transposeBoard(self.board)
            if boardChanged:
                self.spawnTile()
