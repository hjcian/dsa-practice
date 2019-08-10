from util import LinkList

class MinStack(object):
    def __init__(self):
        self.dataStack = LinkList()
        self.minStack = LinkList()

    def pushFront(self, data):
        if self.isEmpty():
            self.minStack.pushFront(data)
        else:
            topMin = self.minStack.firstNode.data
            self.minStack.pushFront(min(data, topMin))
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
    minstack = MinStack()

    minstack.pushFront(6)
    minstack.pushFront(13)
    minstack.pushFront(4)
    minstack.pushFront(9)
    minstack.pushFront(1)

    minstack.printStack()

    print()
    print("After pop two elements: ")
    minstack.pop()
    minstack.pop()
    minstack.printStack()
