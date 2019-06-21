

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2:
            return None
        elif not l1:
            return l2
        elif not l2:
            return l1

        head = cur = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
                cur = cur.next
            else:
                cur.next = l2
                l2 = l2.next
                cur = cur.next
        cur.next = l1 or l2

        return head.next


if __name__ == "__main__":
    node = ListNode(1)
    node.next = ListNode(2)
    node.next.next = ListNode(4)

    node2 = ListNode(1)
    node2.next = ListNode(3)
    node2.next.next = ListNode(4)

    obj = Solution()
    head = obj.mergeTwoLists(node, node2)
