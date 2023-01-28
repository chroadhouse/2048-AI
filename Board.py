import random as r


class Board:

    def __init__(self):
        self.board = [['0', '0', '0', '0'],
                      ['0', '0', '0', '0'],
                      ['0', '0', '0', '0'],
                      ['0', '0', '0', '0']]

    def slideRow(self, row):
        temp = ['0', '0', '0', '0']
        index = 3
        for i in range(3, -1, -1):
            if row[i] != '0':
                temp[index] = row[i]
                index -= 1

        return temp

    def combineRow(self, row):
        for i in range(3, -1, -1):
            a = row[i]
            b = row[i-1]

            if a == b:
                row[i] = str((int(a) + int(b)))
                row[i-1] = '0'
        return row

    def operateRow(self, row):
        row = self.slideRow(row)
        row = self.combineRow(row)
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
            self.boardboard[randomSpot[0]][randomSpot[1]] = '4'
