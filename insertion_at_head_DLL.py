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
    
 
def addNodeAtHeadOfLinkedList(head, val):
    newBlock = Node(val)
    if head == None:
        return newBlock
    newBlock.next = head 
    head.prev = newBlock 
    return newBlock

n = int(input())  # Number of elements in initial list
l = list(map(int, input().split()))  # Initial list
head=None 
new_number = int(input())  # New number to add at the end
# head = None
    
for val in l:
    head =AddNodeAtEnd(head, val)
printLeftToRightManner(head)
printRightToLeftManner(head)
head = addNodeAtHeadOfLinkedList(head, new_number)
printLeftToRightManner(head)
printRightToLeftManner(head)

