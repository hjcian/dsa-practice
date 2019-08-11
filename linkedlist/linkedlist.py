class LinkNode(object):
    def __init__(self, idx, data):
        self.idx = idx
        self.val = data
        self.next = None
    def __repr__(self):
        return f"<LinkNode idx: {self.idx}, data:{self.val}, hasNext:{bool(self.next)}>"
    
class LinkList(object):
    def __init__(self, node=None):
        self.firstNode = None
        self.lastNode = None
        self.size =  0
        self.id = 0

    def printAll(self):
        print("--- print start ---")
        count = 0
        current = self.firstNode
        while(current):
            count += 1
            print(f"{count}/{self.size}: {current}")
            current = current.next
        print("--- print end ---")
        
    def pushFront(self, data):
        self.size += 1
        temp = self.firstNode
        self.firstNode = LinkNode(self.id, data)
        self.firstNode.next = temp
        self.id += 1
        
    def pushBack(self, data):
        if not self.firstNode:
            self.pushFront(data)
        else:
            current = self.firstNode
            while(current.next):
                current = current.next
            current.next = LinkNode(self.id, data)
            self.size += 1
            self.id += 1

    def delete(self, data):
        '''
        delete first matched
        '''
        target = None
        if self.firstNode:
            if self.firstNode.val == data:
                # special case
                target = self.firstNode
                self.firstNode = target.next
                self.size -= 1
            else:
                # general case
                prev = self.firstNode
                curr = self.firstNode.next
                while(curr):
                    if curr.val == data:
                        target = curr
                        prev.next = target.next
                        self.size -= 1
                        break
                    prev = curr
                    curr = curr.next
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
            self.firstNode = self.firstNode.next            
            del target
        print("--- clear end ---")  

    def reverse(self):
        if self.size > 1:
            left = None
            curr = self.firstNode
            right = self.firstNode.next
            while(right):
                temp = right.next
                curr.next = left
                right.next = curr
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
    