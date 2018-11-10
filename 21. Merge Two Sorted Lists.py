# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        temp = ListNode(-1)

        prev = temp

        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next

        if l1 is not None:
            prev.next = l1
        else:
            prev.next = l2

        return temp.next


'''
Time - O(n+m)
Space - O(1)
Learnt - 
Try again from scratch, it has good logic. The above solution is directly from leetcode solution.
recursive is costlier here because space will be O(n), hence used iteration. 

'''