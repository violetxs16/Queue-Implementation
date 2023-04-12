#Queue implementation
#The front of the list will be considered the "rear"
#The back of the list will be considered the "front"
class Queue:
    def __init__(self): #Constructor that initializes an empty queue
        self.items = []
    def enqueue(self, item):#Enqueue item to queue
        self.items.insert(0,item)
    def dequeue(self):#Dequeue's the front most item
        item = self.items.pop()
        return item
    def isEmpty(self):#Is queue empty
        boolVal = self.items == 0
        return boolVal
    def size(self): #Return numbers of items in queue
        return len(self.items)