# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if (not head) or (not head.next):
            return head

        last = head
        length = 1
        while last.next:
            last = last.next
            length += 1

        k = k % length
        if k == 0:
            return head

        new_last = head
        for _ in range(length - k - 1):
            new_last = new_last.next

        new_head = new_last.next
        last.next = head
        new_last.next = None

        return new_head