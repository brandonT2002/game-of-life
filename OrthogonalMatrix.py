from multiprocessing.sharedctypes import Value
from operator import index
from HeaderList import HeaderList
from HeaderNode import HeaderNode
from InternalNode import InternalNode

class OrthogonalMatrix:
    def __init__(self,row : int,column : int):
        self.row : HeaderList = HeaderList()
        self.column : HeaderList = HeaderList()
        for i in range(row):
            self.row.insertNode(i)
        for i in range(column):
            self.column.insertNode(i)
        for i in range(row):
            for j in range(column):
                self.addNode(i,j)

    def addNode(self,row : int,column : int):
        temporary = InternalNode(row,column)
        self.addRow(temporary)
        self.addColumn(temporary)

    def addRow(self,temporary : InternalNode):
        current :HeaderNode = self.row.first
        while current != None:
            if current.index == temporary.row:
                if current.access != None:
                    current.last.right = temporary
                    current.last.right.left = current.last
                    current.last = current.last.right
                    return
                current.access = temporary
                current.last = current.access
                return
            current = current.next

    def addColumn(self,temporary : InternalNode):
        current :HeaderNode = self.column.first
        while current != None:
            if current.index == temporary.column:
                if current.access != None:
                    current.last.down = temporary
                    current.last.down.up = current.last
                    current.last = current.last.down
                    return
                current.access = temporary
                current.last = current.access
                return
            current = current.next

    def insert(self,row : int,column : int,value : int):
        currentC : HeaderNode = self.column.first
        currentR : InternalNode
        while currentC != None:
            if currentC.index == column:
                currentR = currentC.access
                while currentR != None:
                    if currentR.row == row:
                        currentR.value = value
                        return
                    currentR = currentR.down
                return
            currentC = currentC.next

    def get(self,row : int,column : int):
        currentR : HeaderNode = self.row.first
        currentC : InternalNode
        while currentR:
            if currentR.index == row:
                currentC = currentR.access
                while currentC:
                    if currentC.column == column:
                        return currentC
                    currentC = currentC.right
            currentR = currentR.next


    def printMatrix(self):
        currentR : HeaderNode = self.row.first
        currentC : InternalNode
        matrix = ''
        while currentR != None:
            currentC = currentR.access
            while currentC != None:
                if currentC.value == 0:
                    matrix += '░░░'
                else:
                    matrix += '███'
                currentC = currentC.right
            matrix += '\n'
            currentR = currentR.next
        
        print(matrix)