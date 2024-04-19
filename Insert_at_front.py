
    

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

def INsertAtFront(head,ele):
    newblock=Node(ele)
    if head==None:
        return newblock
    newblock.next=head
    return newblock    


l=[11,22,33,44,55,66,77,88,99]
head=None
for ele in l:
    head=INsertAtFront(head,ele)
printLinkedList(head)  


