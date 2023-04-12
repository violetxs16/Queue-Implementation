#Stack implementation
#A stack is a data structure in which has a FILO or First In Last Out implemention
#The addition and removal of items takes place at the end

class Stack:
    def __init__(self): #Constructor for empty stack
        self.items  = []
    
    def push(self, item): #Add an item to the top of the stack
       self.items.append(item)

    def pop(self): #Removes the top item from the stack
        item = self.items.pop()
        return item
    
    def peek(self):#Returns the top most item in the stack
        item = self.items[len(self.items)-1]
        return item
    
    def isEmpty(self):#Checks is stack is empty
        boolVal = len(self.items) == 0
        return boolVal
    
    def size(self): #Returns size of stack
        length = len(self.items)
        return length
    