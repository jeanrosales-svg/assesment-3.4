# ==========================================
# Assessment 3.6: DFS Methods in Tree ("JEAN ROSALES")
# ==========================================

# Tree structure mapping for JEAN ROSALES:
# Root 'R' -> Left 'E', Right 'S_right'
# 'E' -> Left 'A_left', Right 'O'
# 'A_left' -> Left 'J', Right 'N'
# 'S_right' -> Left 'A_right', Right 'L'
# 'A_right' -> Left 'E_right'
# 'E_right' -> Right 'S_deep'

tree = {
    'R': {'left': 'E', 'right': 'S_right'},
    'E': {'left': 'A_left', 'right': 'O'},
    'A_left': {'left': 'J', 'right': 'N'},
    'J': {'left': None, 'right': None},
    'N': {'left': None, 'right': None},
    'O': {'left': None, 'right': None},
    'S_right': {'left': 'A_right', 'right': 'L'},
    'A_right': {'left': 'E_right', 'right': None},
    'E_right': {'left': None, 'right': 'S_deep'},
    'S_deep': {'left': None, 'right': None},
    'L': {'left': None, 'right': None}
}

# Mapping unique keys back to display characters
display_name = {
    'A_left': 'A',
    'A_right': 'A',
    'S_right': 'S',
    'S_deep': 'S',
    'E_right': 'E'
}

# 1. Pre-Order Traversal (Root -> Left -> Right)
def pre_order(node, visited=None):
    if visited is None:
        visited = []
    if node:
        visited.append(display_name.get(node, node))
        pre_order(tree[node]['left'], visited)
        pre_order(tree[node]['right'], visited)
    return visited

# 2. In-Order Traversal (Left -> Root -> Right)
def in_order(node, visited=None):
    if visited is None:
        visited = []
    if node:
        in_order(tree[node]['left'], visited)
        visited.append(display_name.get(node, node))
        in_order(tree[node]['right'], visited)
    return visited

# 3. Post-Order Traversal (Left -> Right -> Root)
def post_order(node, visited=None):
    if visited is None:
        visited = []
    if node:
        post_order(tree[node]['left'], visited)
        post_order(tree[node]['right'], visited)
        visited.append(display_name.get(node, node))
    return visited

if __name__ == "__main__":
    root_node = 'R'
    print("=== DFS METHODS FOR TREE (JEAN ROSALES) ===")
    print("Pre-Order :", ", ".join(pre_order(root_node)))
    print("In-Order  :", ", ".join(in_order(root_node)))
    print("Post-Order:", ", ".join(post_order(root_node)))