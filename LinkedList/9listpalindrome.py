# IS LIST PALINDROME

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(head: ListNode) -> bool:
    curr = head
    lst = [] 
    while curr is not None:
        lst .append(curr.val)
        curr = curr.next
    left = 0
    right = len(lst)-1
    while left<=right:
        if lst[left] != lst[right]:
            return False
        left+=1
        right-=1
    return True
