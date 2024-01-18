# MOVE RIGHT BY K

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def rotateRight(head: ListNode, k: int) -> ListNode:
    if not head or not head.next or k == 0:
        return head
        
    length = 1
    old_tail = head
    while old_tail.next:
        old_tail = old_tail.next
        length += 1
    old_tail.next = head 
        
    k = k % length
        
    if k == 0:
        old_tail.next = None 
        return head
        
    new_tail = head
    for _ in range(length - k - 1):
        new_tail = new_tail.next
    
    new_head = new_tail.next
    new_tail.next = None
        
    return new_head
