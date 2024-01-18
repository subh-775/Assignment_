# Reverse in k-groups

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseKGroup(head: ListNode, k: int) -> ListNode:
    lst = []
    length = 0
    curr = head
    while curr is not None:
        lst.append(curr)
        length+=1
        curr = curr.next
    effective_arr = length - length%k
    for i in range(0,effective_arr,k):
        left = i
        right = i+k-1
        while left<=right:
            lst[left], lst[right] = lst[right], lst[left]
            left+=1
            right-=1
    
    for i in range(length):
        try:
            lst[i].next = lst[i+1]
        except IndexError:
            lst[i].next = None
    return lst[0]
