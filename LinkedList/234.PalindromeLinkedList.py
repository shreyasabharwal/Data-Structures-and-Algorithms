'''234. Palindrome Linked List

Given a singly linked list, determine if it is a palindrome.

Example 1:
Input: 1->2
Output: false

Example 2:
Input: 1->2->2->1
Output: true

Follow up:
Could you do it in O(n) time and O(1) space?'''


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        newHead = self.reverse(slow)

        while newHead and head:
            if newHead.val != head.val:
                return False
            newHead = newHead.next
            head = head.next

        return True

    def reverse(self, head):
        cur = head
        prev = None
        while cur:
            temp = cur
            cur = cur.next
            temp.next = prev
            prev = temp

        head = temp
        return head
