# REORDER GIVEN LIST

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorderList(head: ListNode) -> None:
    lst = []
    curr = head
    while curr is not None:
        lst.append(curr)
        curr = curr.next
    i = 0
    j = len(lst)-1
    mid = len(lst)//2
    while i<j:
        temp = lst[i].next
        lst[i].next = lst[j]
        lst[j].next = temp
        i+=1
        j-=1
    lst[mid].next = None