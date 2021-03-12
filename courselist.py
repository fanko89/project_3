class Node:
    def __init__(self, data_val = None):
        self.next = None
        self.data_val = data_val


class MyList:
    def __init__(self): #this is my list
        self.head = None
        self.first = None
        self.count = 0
    
     def __str__(self):
        result = ""
        current = self.first
        while current != None:
            result += str(current.value)
            result += "\n"
            current = current.next        
        return result

    
    
    def __iter__(self):
        self.track = 0
        return self
    

    def __next__(self):
        if self.track == None:
            self.track = self.first
        elif self.track.next == None:
            raise StopIteration()
        else:
            self.track = self.track.next
        return self.track
    
    def index(self, item):
        index = 0
        while index < self.length():
            if self.get(index).data_val == item:
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
            one_before = self.get(index-1)
            temp = one_before.next
            if self.last == temp:
                self.last = one_before
            one_before.next = temp.next
            temp.next = None
    
    def size(self):
        pass
    
    def insert(self, data_val):
        if self.first == None:
            self.first = Node(data_val)
            self.last = self.first
        elif self. first.data_val >data_val:
            new_item = Node(data_val)
            new_item.next = self.first
            self.first.prev = new_item.next
            self.first = new_item
        else:
            current = self.first

            while current.first. next != None and current.data_val <data_val:
                current = current.next
            new_item = Node(data_val)
            new_item.next = current.next #points at the next current
            current.next = new_item #putting Node in
            new_item.prev = current
            if (new_item.next != None):
                new_item.next.prev = new_item 
            else:
                self.last = new_item
        self.count += 1
    
    def calculate_gpa():
        pass
    

    def length(self):
        return count

    
    def get(self,index):
        if self.undefined():
            return None
        else:
            new_index = 0
            part = self.first
            while new_index < index:
                new_index += 1
                part = part.next
            return part


    def undefined():
        return self.first==None