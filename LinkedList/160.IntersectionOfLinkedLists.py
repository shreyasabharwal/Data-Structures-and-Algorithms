'''160. Intersection of Two Linked Lists

Write a program to find the node at which the intersection of two singly linked lists begins.

Notes:
"""  """
If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.'''

'''
Approach: Maintain two pointers pApA and pBpB initialized at the head of A and B, respectively. Then let them both traverse through the lists, one node at a time.
When pApA reaches the end of a list, then redirect it to the head of B (yes, B, that's right.); similarly when pBpB reaches the end of a list, redirect it the head of A.
If at any point pApA meets pBpB, then pApA/pBpB is the intersection node.
To see why the above trick would work, consider the following two lists: A = {1,3,5,7,9,11} and B = {2,4,9,11}, which are intersected at node '9'. Since B.length (=4) < A.length (=6), pBpB would reach the end of the merged list first, because pBpB traverses exactly 2 nodes less than pApA does. By redirecting pBpB to head A, and pApA to head B, we now ask pBpB to travel exactly 2 more nodes than pApA would. So in the second iteration, they are guaranteed to reach the intersection node at the same time.
'''


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None

        a = headA
        b = headB
        while a != b:
            if not a:
                a = headB
            else:
                a = a.next
            if not b:
                b = headA
            else:
                b = b.next

        return a
