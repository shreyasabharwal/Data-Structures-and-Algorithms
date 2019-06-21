'''206. Reverse Linked List

Reverse a singly linked list.

Example:
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

Follow up:
A linked list can be reversed either iteratively or recursively. Could you implement both?'''


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        cur = head
        prev = None

        while cur:
            temp = cur
            cur = cur.next
            temp.next = prev
            prev = temp

        head = temp

        return head
