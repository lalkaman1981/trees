"""
Deletes node from the tree 
"""
class TreeNode:
    """
    Tree node class
    """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return self.val

class Solution:
    """
    solution class
    """

    def deleteNode(self, root, key: int):
        """
        deletes node from tree
        """

        if not root:
            return root

        root1 = root
        previous = None

        while root1 is not None:
            if root1.val == key:
                break

            elif root1.val > key:
                previous = root1
                root1 = root1.left

            elif root1.val < key:
                previous = root1
                root1 = root1.right

        if root1 is None:
            return root

        new_node = root1.left if root1.left else root1.right

        if root1.right and root1.left:

            minimum_right = root1.right
            minimum_left = minimum_right.left

            while minimum_left and minimum_left.left:
                minimum_left = minimum_left.left

            if minimum_left:
                minimum_left.left = root1.left
            else:
                minimum_right.left = root1.left

            new_node = minimum_right

        if not previous:
            root = new_node
        elif previous.left is root1:
            previous.left = new_node
        else:
            previous.right = new_node

        return root
