'''

19. Remove Nth Node From End of List

Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.

'''

class LinkedListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        pointer1 = head
        pointer2 = head
        previous = head
        while pointer1 != None:
            if pointer1.next != None:
                pointer1 = pointer1.next
                n -= 1
                if n <= 0 :
                    previous = pointer2
                    pointer2 = pointer2.next
            else :
                if n >0:
                    return head.next
                else:
                    pointer1 = pointer1.next
                    previous.next = pointer2.next

        return head

    def print_linkedList(self,head):
        while head is not None:
            print(head.val)
            head = head.next



LinkedListNode_1 = LinkedListNode(1)
LinkedListNode_2 = LinkedListNode(2)
LinkedListNode_3 = LinkedListNode(3)
LinkedListNode_4 = LinkedListNode(4)
LinkedListNode_5 = LinkedListNode(5)

LinkedListNode_1.next = LinkedListNode_2
LinkedListNode_2.next = LinkedListNode_3
LinkedListNode_3.next = LinkedListNode_4
LinkedListNode_4.next = LinkedListNode_5

sol = Solution()
sol.print_linkedList(LinkedListNode_1)
head = sol.removeNthFromEnd(LinkedListNode_1,4)
print()
sol.print_linkedList(head)
