# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import random

class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head
        current = head
        self.num = 0
        while current is not None:
            self.num += 1
            current = current.next


    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        current = None
        r = random.randint(0, self.num - 1)
        for i in range(r + 1):
            if i == 0:
                current = self.head
            else:
                current = current.next
        return current.val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
