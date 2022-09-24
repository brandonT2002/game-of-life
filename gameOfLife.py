from HeaderNode import HeaderNode
from InternalNode import InternalNode
from OrthogonalMatrix import OrthogonalMatrix
import os

class Grid:
    def __init__(self,size : int):
        self.size = size
        self.matrix = OrthogonalMatrix(size,size)
        self.newMatrix = OrthogonalMatrix(size,size)

    def killCell(self,row,column):
        self.matrix.insert(row,column,1)
        self.newMatrix.insert(row,column,1)


    def nextPeriod(self):
        currentC : HeaderNode = self.matrix.column.first
        currentR : InternalNode
        while currentC != None:
            currentR = currentC.access
            while currentR != None:
                self.decision(currentR,self.neighbour(0,currentR))
                currentR = currentR.down
            currentC = currentC.next
        self.matrix = self.cloneMatrix()
        

    def decision(self,node : InternalNode,counter : int):
        if node.value == 0:
            if counter == 3:
                self.newMatrix.insert(node.row,node.column,1)
            return
        if counter != 2 and counter != 3:
            self.newMatrix.insert(node.row,node.column,0)

    def cloneMatrix(self):
        clon : OrthogonalMatrix = OrthogonalMatrix(self.size,self.size)
        currentR : HeaderNode = self.newMatrix.row.first
        currentC : InternalNode
        while currentR:
            currentC = currentR.access
            while currentC:
                clon.insert(currentC.row,currentC.column,currentC.value)
                currentC = currentC.right
            currentR = currentR.next

        return clon


    def neighbour(self,counter : int,node : InternalNode):
        if node.down:
            if node.right:
                if node.down.right.value == 1:
                    counter += 1
            if node.left:
                if node.down.left.value == 1:
                    counter += 1
            if node.down.value == 1:
                counter += 1
        if node.up:
            if node.right:
                if node.up.right.value == 1:
                    counter += 1
            if node.left:
                if node.up.left.value == 1:
                    counter += 1
            if node.up.value == 1:
                counter += 1
        if node.right:
            if node.right.value == 1:
                counter += 1
        if node.left:
            if node.left.value == 1:
                counter += 1

        return counter

    def generatePeriod(self,noPeriod):
        self.generatePDF(0)
        for i in range(noPeriod):
            self.showCells()
            self.generatePDF(i + 1)
            self.nextPeriod()


    def showCells(self):
        self.matrix.printMatrix()

    def generateIMG(self,i):
        self.generateTXT(i)
        os.system("neato -Tpng dot/mtrx" + str(i) + ".txt -o dot/mtrx" + str(i) + ".png")
    
    def generatePDF(self,i):
        self.generateTXT(i)
        os.system("neato -Tpdf dot/mtrx" + str(i) + ".txt -o pdf/mtrx" + str(i) + ".pdf")

    def generateTXT(self,i):
        with open ('dot/mtrx' + str(i) + '.txt','w') as file:
            file.write(self.getDot())

    def getDot(self):
        currentR : HeaderNode = self.matrix.row.first
        currentC : InternalNode
        dot = 'digraph html {\n\tabc [shape=none, margin=0, label=<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4">'
        while currentR:
            currentC = currentR.access
            dot += '\n\t\t<tr>'
            while currentC:
                if currentC.value == 1:
                    dot += '\n\t\t\t<td BGCOLOR="#4472C4" width="60" height="60">'
                else:
                    dot += '\n\t\t\t<td BGCOLOR="white" width="60" height="60">'
                dot += '</td>'
                currentC = currentC.right
            dot += '\n\t\t</tr>'
            currentR = currentR.next

        dot += '\n\t</TABLE>>];\n}'
        return dot