class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1, l2):
        self.l1 = l1
        self.l2 = l2
        self.l3 = None
        
        if not self.l1:
            return self.l2
        if not self.l2:
            return self.l1
        
        if self.l1.val <= self.l2.val:
            self.l3 = self.l1
            self.l1 = self.l1.next
        else:
            self.l3 = self.l2
            self.l2 = self.l2.next

        cur = self.l3
        prev = None

        while self.l1 and self.l2:

            if self.l1.val <= self.l2.val:
                prev = cur
                prev.next = self.l1
                cur = prev.next
                self.l1 = self.l1.next
            else:
                prev = cur
                prev.next = self.l2
                cur = prev.next
                self.l2 = self.l2.next

        if not self.l1:
            prev = cur
            prev.next = self.l2
            cur = prev.next
            self.l2 = self.l2.next
        if not self.l2:
            prev = cur
            prev.next = self.l1
            cur = prev.next
    
        return self.l3

a = ListNode(-1)
a.next = ListNode(2)
a.next.next = ListNode(3)
a.next.next.next = ListNode(6)
a.next.next.next.next = ListNode(10)
b = ListNode(0)
b.next = ListNode(4)
b.next.next = ListNode(50)
ans = Solution().mergeTwoLists(a,b)
out = []
while ans:
    # print(ans.val)
    out.append(ans.val)
    ans = ans.next
print(out)
#Expected
[-1, 0, 2, 3, 4, 5, 6, 10]

"""
Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

 

Example 1:


Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: l1 = [], l2 = []
Output: []
Example 3:

Input: l1 = [], l2 = [0]
Output: [0]
"""