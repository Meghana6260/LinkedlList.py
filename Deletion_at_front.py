class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def PrintList(head):
    cur=head
    while cur!=None:
        print(cur.data,end=" ")
        cur=cur.next
    print()         
    
def insertAtEnd(head,ele):
    newblock=Node(ele)
    if head==None:
        return newblock
    cur=head
    while cur.next!=None:
        cur=cur.next
    cur.next=newblock 
    return head       

def DeleteAtHead(head):
    if head==None:
        return None
    secondNode=head.next
    head.next=None
    return secondNode


n=int(input())
elements=list(map(int,input().split()))
head=None
for ele in elements:
    head=insertAtEnd(head,ele)
PrintList(head)    
head=DeleteAtHead(head)    
PrintList(head)    


