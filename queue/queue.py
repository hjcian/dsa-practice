class Node(object):
    def __init__(self, data, name='node'):
        self.name = name
        self.data = data
        self.next = None
    def __repr__(self):
        return f"< {self.name} data: {self.data}, next: {bool(self.next)} >"

class Queue(object):
    def __init__(self):
        self.firstNode = None
        self.lastNode = None
        self.size = 0

    def push(self, data):
        '''
        push data from the back
        '''
        if self.isEmpty():
            self.firstNode = Node(data)
            self.lastNode = self.firstNode
        else:
            self.lastNode.next = Node(data)
            self.lastNode = self.lastNode.next
        self.size += 1

    def pop(self):
        '''
        pop data from the front
        '''
        data = None
        if not self.isEmpty():
            temp = self.firstNode
            self.firstNode = self.firstNode.next
            self.size -= 1
            data = temp.data
            del temp
        return data

    def isEmpty(self):
        return not bool(self.size)

    def getSize(self):
        return self.size
    
    def printAll(self):
        print("----- start print -----")
        current = self.firstNode
        count = 0
        while(current):
            count += 1
            print(f"{count}/{self.size}: {current}")
            current = current.next
        print("----- end print -----")

    @property
    def front(self):
        return self.firstNode.data if self.firstNode else None

    @property
    def back(self):
        return self.lastNode.data if self.lastNode else None

if __name__ == "__main__":
    queue = Queue()

    print()
    print("TEST push")
    queue.push(1)
    queue.push(3)
    queue.push(5)
    queue.push(7)
    queue.printAll()

    print()    
    print("TEST pop")
    print(f"pop data: {queue.pop()}")
    queue.printAll()
    print(f"pop data: {queue.pop()}")
    print(f"pop data: {queue.pop()}")
    queue.printAll()

