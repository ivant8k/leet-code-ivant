# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

def list_to_tree(lst):
    """Helper function to convert list to binary tree"""
    if not lst:
        return None
    
    nodes = [TreeNode(val) if val is not None else None for val in lst]
    for i in range(len(nodes)):
        if nodes[i]:
            left_idx = 2 * i + 1
            right_idx = 2 * i + 2
            if left_idx < len(nodes):
                nodes[i].left = nodes[left_idx]
            if right_idx < len(nodes):
                nodes[i].right = nodes[right_idx]
    
    return nodes[0] if nodes else None

# Test cases
solution = Solution()

# Test case 1: [1,2,3] vs [1,2,3] - should be True
tree1 = list_to_tree([1, 2, 3])
tree2 = list_to_tree([1, 2, 3])
print(solution.isSameTree(tree1, tree2))  # Output: True

# Test case 2: [1,2] vs [1,None,2] - should be False
tree3 = list_to_tree([1, 2])
tree4 = list_to_tree([1, None, 2])
print(solution.isSameTree(tree3, tree4))  # Output: False

# Test case 3: [1,2,1] vs [1,1,2] - should be False
tree5 = list_to_tree([1, 2, 1])
tree6 = list_to_tree([1, 1, 2])
print(solution.isSameTree(tree5, tree6))  # Output: False