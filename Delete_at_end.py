class Node:
    def __init__(self,Data):
        self.data=Data
        self.next=None

def printLinkedList(head):
    curr=head
    while curr!=None:
        print(curr.data,end="-->")
        curr=curr.next
    print("None")

def InsertAtEndOfLoop(head,ele):
    newblock=Node(ele)
    if head==None:
        return newblock
    curr=head
    while curr.next!=None:
        curr=curr.next
    curr.next=newblock
    return head    


def deleteatend(head):
    curr=head
    previous=None
    while curr.next!=None:
        previous=curr
        curr=curr.next
    previous.next=None
    return head    
l=[11,22,33,44,55,66,77,88,99]
head=None
for ele in l:
    head=INsertAtEndofLoop(head,ele)
head=deleteatend(head)
printLinkedList(head)  
