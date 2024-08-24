# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head.next:
            return True

        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow

        #reverse next half
        prev = None
        cur = mid
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        first = head
        second = prev
        while second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next

        return True