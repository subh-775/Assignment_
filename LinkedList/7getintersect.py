# IF LIST INTERSECT

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def getIntersectionNode(headA: ListNode, headB: ListNode) -> ListNode:
    def get_length(node):
        length = 0
        while node:
            length += 1
            node = node.next
        return length

    len_A = get_length(headA)
    len_B = get_length(headB)

    while len_A > len_B:
        headA = headA.next
        len_A -= 1
        
    while len_B > len_A:
        headB = headB.next
        len_B -= 1
        
        
    while headA and headB:
        if headA == headB:
            return headA
        headA = headA.next
        headB = headB.next
        
    return None