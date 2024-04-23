"""
sorts binary tree by levels
"""

def tree_by_levels(node):
    """
    builds tree by levels
    """
    if not node:
        return []
    lst = [node]
    counter = 0

    while True:
        if counter >= len(lst):
            break
        new_val = lst[counter]
        if new_val.left:
            lst.append(new_val.left)
        if new_val.right:
            lst.append(new_val.right)
        counter += 1

    return [i.value for i in lst]
