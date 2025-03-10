# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution2:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = fast = prev = head
        distance = 0

        while fast:
            fast = fast.next

            if distance == n:
                prev = slow
                slow = slow.next
            else:
                distance += 1

        prev.next = slow.next

        if slow == head:
            head = head.next

        return head

        