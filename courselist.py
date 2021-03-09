class Node:
    def __init__(self, dataval = None):
        self.next = None
        self.dataval = dataval


class MyList:
    def __init__(self): #this is my list
        self.head = None
        self.first = None
    
    def insert(self, course):

  def index(self, item):
        index = 0
        while index < self.length():
            if self.get(index).dataval == item:
                return index
            index += 1
        return -1


    def remove(self, item):
        index = self. index(item)
        if self.last == self.first:
            self.last = None
            self.first = None
        elif index == 0:
            temp = self.first.next
            self.first.next = None
            self.first = temp
        elif index > 0:
            oneBefore = self.get(index-1)
            temp = oneBefore.next
            if self.last == temp:
                self.last = oneBefore
            oneBeofre.next = temp.next
            temp.next = None
    
    def size(self):



print(help_node)       

