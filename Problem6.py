#leetcode problem
# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        retVal = ListNode(0)
        tail = retVal
        carry = 0

# Need to visit all node while there is some visitable nodes
# or
# there is a carry even the all nodes are visited
        while l1 or l2 or carry:
            l1val = (l1.val if l1 else 0)
            l2val = (l2.val if l2 else 0)

            carry, out = divmod(l1val + l2val + carry, 10)
            out = (l1val + l2val + carry) % 10

            tail.next = ListNode(out)
            tail = tail.next

            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)

        return retVal.next