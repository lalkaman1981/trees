"""
Binary Tree Traversal program
"""

def pre_order(node):
    """
    Pre-order traversal
    """
    if not node:
        return []

    if isinstance(node, int):
        return [node]

    return [node.data] + pre_order(node.left) + pre_order(node.right)


def in_order(node):
    """
    In-order traversal
    """
    if not node:
        return []

    if isinstance(node, int):
        return [node]

    return in_order(node.left) + [node.data] + in_order(node.right)


def post_order(node):
    """
    Post-order traversal
    """
    if not node:
        return []

    if isinstance(node, int):
        return [node]

    return post_order(node.left) + post_order(node.right) + [node.data]
