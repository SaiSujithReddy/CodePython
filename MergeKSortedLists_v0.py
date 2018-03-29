'''

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

'''

from queue import PriorityQueue

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = point = ListNode(0)
        q = PriorityQueue()
        for l in lists:
            if l:
                q.put((l.val, l))
        while not q.empty():
            val, node = q.get()
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                q.put((node.val, node))
        return head.next

# class Solution(object):
#     def mergeKLists(self, lists):
#         dummy = ListNode(None)
#         curr = dummy
#         q = PriorityQueue()
#         for node in lists:
#             if node: q.put((node.val,node))
#         while q.qsize()>0:
#             curr.next = q.get()[1]
#             curr=curr.next
#             if curr.next: q.put((curr.next.val, curr.next))
#         return dummy.next



listnode1 = ListNode(1)
listnode2 = ListNode(2)
listnode3 = ListNode(3)
listnode7 = ListNode(7)
listnode1.next = listnode2
listnode2.next = listnode3
listnode3.next = listnode7

listnode5 = ListNode(5)
listnode6 = ListNode(6)
listnode8 = ListNode(8)
listnode5.next = listnode6
listnode6.next = listnode8


number_lists = [listnode1,listnode5]
sol = Solution()
head = sol.mergeKLists(number_lists)

while head.next is not None:
    print(head.val)
    head = head.next
print(head.val)

'''

Things learnt 

PQ are different from Heap 
https://www.youtube.com/watch?v=wptevk0bshY


PQ = each element has a certain priority 
say 14,4,8,3 are inserted 
smaller numbers have highest priority

poll_PQ()
output = 3
poll_PQ()
output = 3,4
poll_PQ()
output = 3,4,8
poll_PQ()
output = 3,4,8,14

How does PQ know which is smallest.
PQ uses Heap 

We use PQ in case thread safety or else we can use Heap

All heaps must be trees , no cycles should b expected in trees

PQ used in Dijkstras's shortest patch algo 
used in Huffman encoding (lossless data compression)
For BFS we use PQ
PQ used in in Minimum spanning tree 


Heap construction - O(n)
poll - O(logn)
peek - O(1)
Addition - O(logn)
naive removing - O(n) - scan all elements
removing element with help of hashtable - O(logn)


'''