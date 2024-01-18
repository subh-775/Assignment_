# REMOVE Nth NODE

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    dummy = ListNode(0)
    dummy.next = head
    first = dummy
    second = dummy
        
        
    for _ in range(n + 1):
        if not second:
            return head 
        second = second.next
        
    while second:
        first = first.next
        second = second.next
        
    first.next = first.next.next
        
    return dummy.next
