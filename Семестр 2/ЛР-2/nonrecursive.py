def gen_bin_tree(root: int, height: int) -> dict:
    if height == 0:
        return {root: []}
    
    tree = {}
    stack = [(root, height, False, None)]
    node_dicts = {}
    
    while stack:
        node, h, processed, parent = stack.pop()
        
        if h == 0:
            node_dicts[node] = {node: []}
            continue
            
        if not processed:
            left = node * 2
            right = node + 3
            stack.append((node, h, True, parent))
            stack.append((right, h-1, False, node))
            stack.append((left, h-1, False, node))
        else:
            left = node * 2
            right = node + 3
            node_dict = {node: [
                node_dicts.get(left, left),
                node_dicts.get(right, right)
            ]}
            node_dicts[node] = node_dict
            
            if parent is None:
                tree.update(node_dict)
    
    return tree