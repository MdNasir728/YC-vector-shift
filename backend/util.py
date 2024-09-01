from collections import defaultdict, deque

def is_dag(edges):
    # Create adjacency list and in-degree count
    adj_list = defaultdict(list)
    in_degree = defaultdict(int)
    
    # Build the graph
    for source, target in edges:
        adj_list[source].append(target)
        in_degree[target] += 1
        if source not in in_degree:
            in_degree[source] = 0
    
    # Initialize the queue with nodes that have zero in-degrees
    queue = deque(node for node in in_degree if in_degree[node] == 0)
    
    count = 0
    
    while queue:
        node = queue.popleft()
        count += 1
        
        for neighbor in adj_list[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # Check if the number of nodes processed equals the number of unique nodes
    unique_nodes = set(in_degree.keys()) | set(neighbor for neighbors in adj_list.values() for neighbor in neighbors)
    return count == len(unique_nodes)


