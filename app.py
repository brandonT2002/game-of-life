class Grid:
    def __init__(self,size : int):
        self.size = size
        self.matrix = [[0 for j in range(size)] for i in range(size)]
        self.newMatrix = [[0 for j in range(size)] for i in range(size)]

    def killCell(self,x,y):
        self.matrix[x][y] = 1
        self.newMatrix[x][y] = 1

    def showCells(self):
        board = ''
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                if self.matrix[i][j] == 0:
                    board += '░░░'
                else:
                    board += '███'
            board += '\n'
        print(board)

    def nextPeriod(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                self.decision(i,j,self.neighbour(i,j))
        
        self.matrix = [[self.newMatrix[i][j] for j in range(self.size)] for i in range(self.size)]

    def neighbour(self,row,column):
        dead = 0
        for i in range(row - 1,row + 2):
            if i >= 0 and i < len(self.matrix):
                for j in range(column - 1, column + 2):
                    if j >= 0 and j < len(self.matrix):
                        if i == row and j == column:
                            continue
                        if self.matrix[i][j] == 1:
                            dead += 1
        return dead
    
    def decision(self,row,column,counter):
        if self.matrix[row][column] == 0:
            if counter == 3:
                self.newMatrix[row][column] = 1
            return
        if counter != 2 and counter != 3:
            self.newMatrix[row][column] = 0

    def generatePeriod(self,noPeriod):
        for i in range(noPeriod + 1):
            self.showCells()
            self.nextPeriod()
            #grill.showCells()