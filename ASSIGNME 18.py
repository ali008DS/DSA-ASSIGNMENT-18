def is_level_order_bst(arr):
    if not arr:
        return True

    queue = []
    queue.append((arr[0], float('-inf'), float('inf')))

    i = 1
    while i < len(arr):
        node_val, min_val, max_val = queue.pop(0)

        if min_val < node_val < max_val:
            if i < len(arr):
                if arr[i] < node_val:
                    queue.append((arr[i], min_val, node_val))
                else:
                    queue.append((arr[i], node_val, max_val))
                i += 1
        else:
            return False

    return True

# Examples
arr1 = [7, 4, 12, 3, 6, 8, 1, 5, 10]
arr2 = [11, 6, 13, 5, 12, 10]

print(is_level_order_bst(arr1))  # Output: True
print(is_level_order_bst(arr2))  # Output: False
