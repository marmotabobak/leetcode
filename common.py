# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        node = self
        res = ''
        while node.next:
            res += f'{node.val} -> '
            node = node.next
        res += f'{node.val}'
        return res


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)

    def traverse_width_from_left(self):
        stack = [self]
        while stack:
            node = stack.pop(0)
            print(node)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

    def traverse_width_from_right(self):
        stack = [self]
        while stack:
            node = stack.pop(0)
            print(node)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)