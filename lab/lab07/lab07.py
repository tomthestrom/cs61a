""" Lab 07: Midterm Review """

def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    "*** YOUR CODE HERE ***"
    if m == 1 or n == 1:
        return 1
    else:
        move_left = paths(m - 1, n) 
        move_down = paths(m, n - 1)

        return move_left + move_down

def build_fbt(nodes):
    if nodes == 0:
        return [tree('LEAF')]
    else:
        trees = []
        """
        Begins with 0 for the left and "nodes - 0 - 1(the root node)" for the right - so we start building the trees from the right side
        """
        for left_range in range(nodes):
            right_range = nodes - left_range - 1
            left_branch = build_fbt(left_range) 
            right_branch = build_fbt(right_range)
            for right_trees in right_branch:
                for left_trees in left_branch:
                    trees.append(tree('NODE', [left_trees, right_trees]))
        return trees
    
def num_trees(n):
    """How many full binary trees have exactly n leaves? E.g.,

    1   2        3       3    ...
    *   *        *       *
       / \      / \     / \
      *   *    *   *   *   *
              / \         / \
             *   *       *   *

    >>> num_trees(1)
    1
    >>> num_trees(2)
    1
    >>> num_trees(3)
    2
    >>> num_trees(8)
    429

    """
    "*** YOUR CODE HERE ***"
    return len(build_fbt(n-1))
def prune_leaves(t, vals):
    """Return a modified copy of t with all leaves that have a label
    that appears in vals removed.  Return None if the entire tree is
    pruned away.

    >>> t = tree(2)
    >>> print(prune_leaves(t, (1, 2)))
    None
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    >>> print_tree(prune_leaves(numbers, (3, 4, 6, 7)))
    1
      2
      3
        5
      6
    """
    "*** YOUR CODE HERE ***"
    def is_leaf_to_remove(t, vals):
        return is_leaf(t) and label(t) in vals
    
    #case we get a leaf as input and it's value in vals
    if is_leaf_to_remove(t, vals):
        return None
            
    if is_leaf(t):
        return tree(label(t))
    else:
        new_branches = []
        for branch in branches(t):
            if is_leaf_to_remove(branch, vals):
                continue
            new_branches += [prune_leaves(branch, vals)]
    
        return tree(label(t), new_branches)
    

def dict_to_lst(d):
    """Returns a list containing all the (key, value) pairs in d as two-element
    tuples ordered by increasing value.

    >>> nums = {1: 5, 2: 3, 3: 4}
    >>> dict_to_lst(nums)
    [(2, 3), (3, 4), (1, 5)]
    >>> words = {'first': 'yes', 'second': 'no', 'third': 'perhaps'}
    >>> dict_to_lst(words)
    [('second', 'no'), ('third', 'perhaps'), ('first', 'yes')]
    """
    result = []
    for i in range(len(d)):
        pair = min(d.items(), key=lambda x: x[1])
        d.pop(pair[0])
        result += (pair,)
    return result

# Tree ADT
def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    """Return the label value of a tree."""
    return tree[0]

def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]

def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)

def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

def copy_tree(t):
    """Returns a copy of t. Only for testing purposes.

    >>> t = tree(5)
    >>> copy = copy_tree(t)
    >>> t = tree(6)
    >>> print_tree(copy)
    5
    """
    return tree(label(t), [copy_tree(b) for b in branches(t)])
