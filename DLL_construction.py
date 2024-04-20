class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 
        self.prev = None 
 
def printLeftToRightManner(head):
    # print("Left to Right")
    curr = head 
    while curr != None:
        print(curr.data, end = " ")
        curr = curr.next 
    print()
 
def printRightToLeftManner(head):
    # print("Right to Left")
    tail = head 
    while tail.next != None:
        tail = tail.next 
 
    curr = tail
    while curr != None:
        print(curr.data, end = " ")
        curr = curr.prev 
    print()
    
    
def addNodeAtHeadOfLinkedList(head, val):
    newBlock = Node(val)
    if head == None:
        return newBlock
    # 11 --> 22 --> 33 --> None 
    # newBlock = 10
    # head = 11 
    newBlock.next = head 
    head.prev = newBlock 
    return newBlock
n=int(input())
l=list(map(int,input().split()))
head=None
for ele in l:
    head=addNodeAtHeadOfLinkedList(head, ele)
# printLeftToRightManner(head)
printRightToLeftManner(head)
printLeftToRightManner(head)
