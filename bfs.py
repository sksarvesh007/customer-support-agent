from collections import deque

def bfs(graph, start_node):
    visited = set()  # To keep track of visited nodes
    queue = deque([start_node])  # Queue for BFS

    while queue:
        node = queue.popleft()  # Dequeue a node
        if node not in visited:
            print(node, end=' ')  # Process the node
            visited.add(node)  # Mark the node as visited

            # Enqueue all adjacent, unvisited nodes
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

bfs(graph, 'A')
