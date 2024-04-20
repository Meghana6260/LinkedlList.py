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

def AddNodeAtEnd(head,val):
    newblock=Node(val)
    if head==None:
        return newblock
    tail=head
    while tail.next!=None:
        tail=tail.next
    tail.next=newblock
    newblock.prev=tail
    return head        

n=int(input())
l=list(map(int,input().split()))
head = None 
for ele in l:
    #head = addNodeAtTailOfLinkedList(head, ele)
    head = AddNodeAtEnd(head, ele)
printLeftToRightManner(head)
printRightToLeftManner(head)   
 
head =deleteHeadNodeInDoublyLinkedList(head)
printLeftToRightManner(head)
printRightToLeftManner(head) 
