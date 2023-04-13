#A deque is a data structure which has qualities of a stack and a queue. A deque is a collection of items that can be added or removed from the front or the rear. 
class deque:
    def __init__ (self): #Constructor
        self.items = []
    def addRear(self, item): #Add item to the rear of the deque
        self.items.insert(0,item)
    def addFront(self, item): #Add item to the front of the deque
        self.items.append(item)
    def removeFront(self): #Removes front most item & returns item
        item = self.items.pop()
        return item
    def removeRear(self):#Removes the rear item $ returns item
        item = self.items.pop(0)
        return item
    def isEmpty(self): #returns True if deque is empty
        boolVal = len(self.items) == 0
        return boolVal
    def size(self): #Returns size of deque(integer)
        return len(self.items)
    def __str__(self):
        return str(self.items)
