class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 
        self.prev = None 
 
def printLeftToRightManner(head):
    # print("Left to Right")
    curr = head 
    while curr != None:
        print(curr.data, end=" ")
        curr = curr.next 
    print()
 
def printRightToLeftManner(head):
    # print("Right to Left")
    if head is None:  # Handle empty list
        print()
        return
 
    tail = head 
    while tail.next != None:
        tail = tail.next 
 
    curr = tail
    while curr != None:
        print(curr.data, end=" ")
        curr = curr.prev 
    print()
 
def addNodeAtTailOfLinkedList(head, val):
    newBlock = Node(val)
 
    if head == None:
        return newBlock
 
    tail = head 
    while tail.next != None:
        tail = tail.next 
 
    tail.next = newBlock 
    newBlock.prev = tail 
    return head

# Getting input
n = int(input().strip())  # Number of elements in initial list
l = list(map(int, input().strip().split()))  # Initial list
head=None 
new_number = int(input().strip())  # New number to add at the end
# head = None
    
for val in l:
    head = addNodeAtTailOfLinkedList(head, val)
printLeftToRightManner(head)
printRightToLeftManner(head)

head = addNodeAtTailOfLinkedList(head, new_number)
printLeftToRightManner(head)
printRightToLeftManner(head)
