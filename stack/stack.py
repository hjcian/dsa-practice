from util import LinkList

class Stack(object):
    '''
    A Last In, First Out (LIFO) data structure.

    ref: http://alrightchiu.github.io/SecondRound/stack-introjian-jie.html
    '''
    def __init__(self):
        self.linklist = LinkList()

    def pushFront(self, data):
        self.linklist.pushFront(data)
    
    def top(self):
        '''
        just get the top element
        '''
        if self.isEmpty():
            return None
        return self.linklist.firstNode.data

    def pop(self):
        '''
        remove and return the top element
        '''
        if self.isEmpty():
            return None
        data = self.linklist.firstNode.data
        self.linklist.delete(data)
        return data

    def size(self):
        '''
        return the size of Stack
        '''
        return self.linklist.size()

    def isEmpty(self):
        '''
        check if Stack is empty
        '''
        return not bool(self.linklist.size)

    def printStack(self):
        self.linklist.printAll()

if __name__ == "__main__":
    stack = Stack()

    stack.pushFront(123)
    stack.pushFront(456)
    stack.pushFront(789)
    stack.printStack()

    pop = stack.pop()
    print(f"pop out: {pop}")
    stack.printStack()

    pop = stack.pop()
    print(f"pop out: {pop}")
    stack.printStack()

    pop = stack.pop()
    print(f"pop out: {pop}")
    stack.printStack()

    pop = stack.pop()
    print(f"pop out: {pop}")
    stack.printStack()
