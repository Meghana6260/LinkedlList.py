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

def deleteHeadNodeInDoublyLinkedList(head):
    if head==None or head.next==None:
        return None
    secondNode=head.next
    head.next=None
    secondNode.prev=None
    return secondNode

def addNodeAtTailOfLinkedList(head, val):
    newBlock = Node(val)
 
    if head == None:
        return newBlock
 
    tail = head 
    while tail.next != None:
        tail = tail.next 
    tail.next = newBlock 
 # right to left link 
    newBlock.prev = tail 
    return head
     

def deleteNodeAtSpecificPosition(head, position):
    if position == 1:
        return deleteHeadNodeInDoublyLinkedList(head)
 
    curr = head 
    index = 1 
 
    while index != position - 1:
        curr = curr.next 
        index += 1 
 
    nodeToBeDeleted = curr.next 
    nextNode = nodeToBeDeleted.next 
    curr.next = nextNode 
    nextNode.prev = curr 
    return head

n=int(input())
l = list(map(int,input().split()))
pos=int(input())
head = None 
for ele in l:
    head = addNodeAtTailOfLinkedList(head, ele)
    #head = addNodeAtHeadOfLinkedList(head, ele)
printLeftToRightManner(head)
printRightToLeftManner(head)   
 
#head = insertAtSpecificPosition(head, 12222, 3)
head = deleteNodeAtSpecificPosition(head, pos)
 
printLeftToRightManner(head)
printRightToLeftManner(head)       
      
