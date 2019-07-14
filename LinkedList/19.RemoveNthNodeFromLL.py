'''19. Remove Nth Node From End of List

Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?'''


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        current = head
        for i in range(n):
            current = current.next

        if not current:
            return head.next

        new_ptr = head

        while current and current.next:
            new_ptr = new_ptr.next
            current = current.next

        new_ptr.next = new_ptr.next.next

        return head
