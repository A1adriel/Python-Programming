def gen_bin_tree(root: int, height: int, _memo=None) -> dict:
    if height == 0:
        return {root: []}
    
    if _memo is None:
        _memo = {}
    
    key = (root, height)
    if key in _memo:
        return _memo[key]
    
    left = root * 2
    right = root + 3
    
    result = {
        root: [
            gen_bin_tree(left, height-1, _memo),
            gen_bin_tree(right, height-1, _memo)
        ]
    }
    
    _memo[key] = result
    return result