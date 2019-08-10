from util import LinkList

class SpaceCompactMinStack(object):
    def __init__(self):
        self.dataStack = LinkList()
        self.minStack = LinkList()

    def pushFront(self, data):
        if self.isEmpty():
            self.minStack.pushFront(data)
        else:
            topMin = self.minStack.firstNode.data
            if data <= topMin: # different in here from minStack
                self.minStack.pushFront(data)
        self.dataStack.pushFront(data)
    
    def top(self):
        '''
        just get the top element
        '''
        if self.isEmpty():
            return None
        return self.dataStack.firstNode.data

    def pop(self):
        '''
        remove and return the top element
        '''
        if self.isEmpty():
            return None
        data = self.dataStack.firstNode.data
        self.dataStack.delete(data)
        minData = self.minStack.firstNode.data
        if data == minData: # different in here from minStack
            self.minStack.delete(minData)
        return data

    def size(self):
        '''
        return the size of Stack
        '''
        return self.dataStack.size()

    def isEmpty(self):
        '''
        check if Stack is empty
        '''
        return not bool(self.dataStack.size)

    def printStack(self):
        print("-> Regular Stack")
        self.dataStack.printAll()
        print("-> Min. Stack")
        self.minStack.printAll()

if __name__ == "__main__":
    stack = SpaceCompactMinStack()

    stack.pushFront(2)
    stack.pushFront(6)
    stack.pushFront(4)
    stack.pushFront(1)
    stack.pushFront(5)
    stack.pushFront(1)
    stack.printStack()

    print()
    print("Pop One:")
    stack.pop()    
    stack.printStack()

    print()
    print("Pop One:")
    stack.pop()    
    stack.printStack()

    print()
    print("Pop One:")
    stack.pop()    
    stack.printStack()
