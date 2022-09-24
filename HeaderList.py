from HeaderNode import HeaderNode

class HeaderList:
    def __init__(self):
        self.first : HeaderNode = None
        self.last : HeaderNode= None

    def insertNode(self,index : int):
        if self.first:
            self.last.next = HeaderNode(index)
            self.last.prev = self.last
            self.last = self.last.next
            return
        self.first = HeaderNode(index)
        self.last = self.first