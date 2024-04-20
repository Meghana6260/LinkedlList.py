class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def addNodeAtTailOfLinkedList(head, ele):
    newBlock = Node(ele)
    if head is None:
        return newBlock
    tail = head
    while tail.next is not None:
        tail = tail.next
    tail.next = newBlock
    newBlock.prev = tail
    return head

def insertAtSpecific(head, position, m):
    newBlock = Node(m)
    if position == 1:
        newBlock.next = head
        if head is not None:
            head.prev = newBlock
        return newBlock
    index = 1
    cur = head
    while index != position - 1 and cur is not None:
        cur = cur.next
        index += 1
    if cur is None:
        # print("Position is out of range")
        return head
    nextNode = cur.next
    newBlock.next = nextNode
    if nextNode is not None:
        nextNode.prev = newBlock
    cur.next = newBlock
    newBlock.prev = cur
    return head

def printLeftRight(head):
    cur = head
    while cur is not None:
        print(cur.data, end=" ")
        cur = cur.next
    print()

def printRightToLeftManner(head):
    tail = head
    while tail.next is not None:
        tail = tail.next

    curr = tail
    while curr is not None:
        print(curr.data, end=" ")
        curr = curr.prev
    print()

n = int(input())
l = list(map(int, input().split()))
pos, m = map(int, input().split())
head = None
for ele in l:
    head = addNodeAtTailOfLinkedList(head, ele)
printLeftRight(head)
printRightToLeftManner(head)
head = insertAtSpecific(head, pos, m)
# print("Linked List after insertion:")
printLeftRight(head)
printRightToLeftManner(head)
