class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False


if __name__ == "__main__":
    node = ListNode(3)
    node.next = ListNode(2)
    node.next.next = ListNode(0)
    node.next.next.next = ListNode(-4)
    node.next.next.next.next = node.next
    obj = Solution()
    print(obj.hasCycle(node))
