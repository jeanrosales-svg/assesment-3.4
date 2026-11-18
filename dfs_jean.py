# ==========================================
# Assessment 3.6: DFS Methods in Tree ("JEAN")
# ==========================================

# Tree structure mapping for JEAN: A -> E (left), N (right); E -> J (left)
tree = {
    'A': {'left': 'E', 'right': 'N'},
    'E': {'left': 'J', 'right': None},
    'N': {'left': None, 'right': None},
    'J': {'left': None, 'right': None}
}

# 1. Pre-Order Traversal (Root -> Left -> Right)
def pre_order(node, visited=None):
    if visited is None:
        visited = []
    if node:
        visited.append(node)
        pre_order(tree[node]['left'], visited)
        pre_order(tree[node]['right'], visited)
    return visited

# 2. In-Order Traversal (Left -> Root -> Right)
def in_order(node, visited=None):
    if visited is None:
        visited = []
    if node:
        in_order(tree[node]['left'], visited)
        visited.append(node)
        in_order(tree[node]['right'], visited)
    return visited

# 3. Post-Order Traversal (Left -> Right -> Root)
def post_order(node, visited=None):
    if visited is None:
        visited = []
    if node:
        post_order(tree[node]['left'], visited)
        post_order(tree[node]['right'], visited)
        visited.append(node)
    return visited

if __name__ == "__main__":
    root_node = 'A'
    print("=== DFS METHODS FOR TREE (JEAN) ===")
    print("Pre-Order :", ", ".join(pre_order(root_node)))
    print("In-Order  :", ", ".join(in_order(root_node)))
    print("Post-Order:", ", ".join(post_order(root_node)))