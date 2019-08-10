class LinkNode(object):
    def __init__(self, data=None, nextNode=None):
        self.data = data
        self.nextNode = nextNode
    def __repr__(self):
        return f"<LinkNode data:{self.data} hasNext:{bool(self.nextNode)}>"
    
class LinkList(object):
    def __init__(self, node=None):
        self.firstNode = node
        self.size = 1 if node else 0

    def printAll(self):
        print("--- print start ---")
        count = 0
        current = self.firstNode
        while(current):
            count += 1
            print(f"{count}/{self.size}: {current}")
            current = current.nextNode
        print("--- print end ---")

    def pushFront(self, data):
        self.size += 1
        temp = self.firstNode
        self.firstNode = LinkNode(data)
        self.firstNode.nextNode = temp
        
    def pushBack(self, data):
        if not self.firstNode:
            self.pushFront(data)
        else:
            current = self.firstNode
            while(current.nextNode):
                current = current.nextNode
            current.nextNode = LinkNode(data)
            self.size += 1

    def delete(self, data):
        '''
        delete first matched
        '''
        target = None
        if self.firstNode:
            if self.firstNode.data == data:
                # special case
                target = self.firstNode
                self.firstNode = target.nextNode
                self.size -= 1
            else:
                # general case
                prev = self.firstNode
                curr = self.firstNode.nextNode
                while(curr):
                    if curr.data == data:
                        target = curr
                        prev.nextNode = target.nextNode
                        self.size -= 1
                        break
                    prev = curr
                    curr = curr.nextNode
        if target:
            print(f"delete {target}")
            del target
        else:
            print(f'delete empty')

    def clear(self):
        print("--- clear start ---")
        while(self.firstNode):
            print(f"clear {self.firstNode}")
            self.size -= 1
            target = self.firstNode
            self.firstNode = self.firstNode.nextNode            
            del target
        print("--- clear end ---")  

    def reverse(self):
        if self.size > 1:
            left = None
            curr = self.firstNode
            right = self.firstNode.nextNode
            while(right):
                temp = right.nextNode
                curr.nextNode = left
                right.nextNode = curr
                left = curr 
                curr = right
                right = temp
            self.firstNode = curr

if __name__ == "__main__":
    container = LinkList()

    print()
    print("TEST pushFront")
    container.pushFront(1)
    container.printAll()
    container.pushFront(2)
    container.printAll()
    container.pushFront(3)
    container.printAll()

    print()
    print("TEST clear")
    container.clear()
    container.printAll()

    print()
    print("TEST pushBack")
    container.pushBack(1)
    container.printAll()
    container.pushBack(3)
    container.printAll()
    container.pushBack(5)
    container.printAll()
    container.pushBack(7)
    container.printAll()

    print()
    print("TEST delete")
    container.delete(7)
    container.printAll()
    container.delete(4)
    container.printAll()
    container.delete(3)
    container.printAll()

    container.clear()

    print()
    print("TEST reverse")
    for i in range(5):
        container.pushBack(i)
    container.printAll()
    container.reverse()
    container.printAll()
    