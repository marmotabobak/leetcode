# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        node = self
        res = str(node.val)

        while node := node.next:
            res += f' -> {node.val}'

        return res


class Solution(object):
    def isPalindrome(self, head):

        # 1. find the half
        slow, fast = head, head
        while fast := fast.next:
            slow = slow.next
            if not(fast := fast.next):
                break

        # 2. reverse the second half
        prev, curr = None, slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        left, right_reversed = head, prev

        # 3. compare both halves
        while left and right_reversed:
            if left.val != right_reversed.val:
                return False
            left, right_reversed = left.next, right_reversed.next

        return True






l1 = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
l2 = ListNode(1, ListNode(2))

l3 = ListNode(1, ListNode(2, ListNode(3, ListNode(2, ListNode(1)))))
l4 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))

test_cases = {
    l3: True,
    l2: False,
    l3: True,
    l4: False
}

s = Solution()

for test_case, res in test_cases.items():
    assert s.isPalindrome(test_case) == res, (str(test_case), s.isPalindrome(test_case))
