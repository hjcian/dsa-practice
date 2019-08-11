from linkedlist import LinkList

def printChain(current):
    while(current):
        print(f"({current.idx}) {current.val} - " , end='')
        current = current.next
    print(f"END")

def findMiddle(head):
    fast = slow = head
    # find the mid node
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow

def reverseMiddle(middle):
    if not middle:
        return middle
    left = None
    curr = middle
    right = middle.next
    while(right):
        curr.next = left
        left = curr
        curr = right
        right = right.next
    curr.next = left
    return curr # curr is new head

def isPalindrome(head):
    # find the mid node
    middle = findMiddle(head)
    print("middle", middle)
    # printChain(middle)
    # reverse the second half    
    newHead = reverseMiddle(middle)
    print("newHead", newHead)
    # printChain(newHead)
    # print("check original chian: ")
    # printChain(head)
    # # compare the first and second half nodes
    while newHead: # while node and head:
        if newHead.val != head.val:
            print("No")
            return False
        head = head.next
        newHead = newHead.next
    print("Yes")
    return True

if __name__ == "__main__":
    import json
    linklist = LinkList()
    l = json.load(open('large.json', 'r'))
    print(f"length of testcase: {len(l)}")
    for i in l:
        linklist.pushBack(i)
    
    # linklist.pushBack(2)
    # linklist.pushBack(3)
    # linklist.pushBack(5)
    # linklist.pushBack(3)
    # linklist.pushBack(2)
    # linklist.pushBack(1)
    print("start")
    isPalindrome(linklist.firstNode)
