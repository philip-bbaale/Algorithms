class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1, l2):
        self.l1 = l1
        self.l2 = l2
        self.l3 = None
        self.head = None
        
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

        while self.l1 and self.l2:

            if self.l1.val <= self.l2.val:
                nxt = self.l3.next
                self.l3.next = self.head
                self.head = self.l1
                self.l3 = nxt
                self.l1 = self.l1.next
            else:
                nxt = self.l3.next
                self.l3.next = self.head
                self.head = self.l1
                self.l3 = nxt
                self.l2 = self.l2.next

        if not self.l1:
            self.l3.next = self.l2
        if not self.l2:
            self.l3.nexxt = self.l1
    
        return self.l3

a = ListNode(-1)
a.next = ListNode(2)
a.next.next = ListNode(3)
a.next.next.next = ListNode(6)
a.next.next.next.next = ListNode(10)
b = ListNode(0)
b.next = ListNode(4)
b.next.next = ListNode(5)
ans = Solution().mergeTwoLists(a,b)
out = []
while ans:
    # print(ans.val)
    out.append(ans.val)
    ans = ans.next
print(out)
#Expected
[-1, 0, 2, 3, 4, 5, 6, 10]