from collections import deque

# Binary Tree Adjacency List Representation
binary_tree = {
    'R': ['O', 'S'],
    'O': ['A', 'L'],
    'S': ['E', 'S_right'],  # Unique key for second 'S'
    'A': [],
    'L': [],
    'E': [],
    'S_right': []
}

display_name = {'S_right': 'S'}


def tree_bfs(root):
    visited = []
    queue = deque([root])

    while queue:
        current = queue.popleft()
        visited.append(display_name.get(current, current))
        for neighbor in binary_tree.get(current, []):
            queue.append(neighbor)
    return visited


def tree_dfs(root):
    visited = []
    stack = [root]

    while stack:
        current = stack.pop()
        visited.append(display_name.get(current, current))
        for neighbor in reversed(binary_tree.get(current, [])):
            stack.append(neighbor)
    return visited


if __name__ == "__main__":
    print("=== BINARY TREE TRAVERSALS ===")
    print("BFS Traversal:", " -> ".join(tree_bfs('R')))
    print("DFS Traversal:", " -> ".join(tree_dfs('R')))