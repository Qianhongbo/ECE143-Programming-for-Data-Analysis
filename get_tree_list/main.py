class Node:
    def __init__(self, val:int=0, left=None, right=None):
        assert left is None or isinstance(left, Node)
        assert right is None or isinstance(right, Node)
        self.val = val
        self.left = left
        self.right = right

def get_tree_list(p: list[int]):
    """
    Your function get_tree_list(p:List[int]) takes a permutation p as input and returns a list
    that represents the binary tree.
    The index of each item in the list is the value of each node in your tree
    and the value at each index is the parent of that node.
    Recall that in a tree, every node has exactly one parent.

    :param p: list
    :return: list
    """
    assert isinstance(p, list)
    assert len(p) == len(list(set(p)))
    for i in p:
        assert isinstance(i, int)

    root = Node(p[0])
    for i in range(1, len(p)):
        helper(p, i, root)
    result = [0] * len(p)
    result = preorder_traversal_recursion(result, root, root)
    return result


def helper(p: list[int], ind: int, currentNode: Node):
    if p[ind] > currentNode.val:
        if currentNode.right is None:
            currentNode.right = Node(p[ind])
        else:
            helper(p, ind, currentNode.right)
    else:
        if currentNode.left is None:
            currentNode.left = Node(p[ind])
        else:
            helper(p, ind, currentNode.left)

def preorder_traversal_recursion(result, parent, root, v = 0):
    if root is None:
        return
    v = root.val
    result[root.val] = parent.val
    preorder_traversal_recursion(result, root, root.left, v)
    preorder_traversal_recursion(result, root, root.right, v)
    return result

# if __name__ == '__main__':
#     p = [8, 5, 1, 10, 0, 4, 2, 3, 7, 9, 6]
#     print(get_tree_list(p))


