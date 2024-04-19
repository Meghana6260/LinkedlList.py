class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insertAtEnd(head, ele):
    new = Node(ele)
    if head == None:
        return new
    cur = head
    while cur.next != None:
        cur = cur.next
    cur.next = new
    return head

def deleteAtSpecific(head, position):
    if position == 1:
        return None
    index = 1
    cur = head
    while index != position - 1:
        cur = cur.next
        index += 1
    delnode = cur.next
    cur.next = delnode.next
    delnode = None
    return head

def printDetails(head):
    if head == None:
        return
    cur = head
    while cur != None:
        print(cur.data, end=" ")
        cur = cur.next
    print()

n = int(input())
l = list(map(int, input().split()))
pos = int(input())
head = None
for ele in l:
    head = insertAtEnd(head, ele)
printDetails(head)

head = deleteAtSpecific(head, pos)
printDetails(head)
