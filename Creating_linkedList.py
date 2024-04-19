class Node:
    def __init__(self,Data):
        self.data=Data
        self.next=None
def insertartend(head,ele):
    new=Node(ele)
    while head==None:
        return new
    cur=head
    while cur.next!=None:
        cur=cur.next
    cur.next=new
    return head
def printdetails(head):
    cur=head
    while cur!=None:
        print(cur.data,end=" ")
        cur=cur.next
num=int(input())
elements=list(map(int,input().split()))
head=None
for ele in elements:
    head=insertartend(head,ele)
printdetails(head)    
