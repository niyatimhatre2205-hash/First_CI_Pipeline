def rotate_list(items, k):
    if len(items) == 0:
        return []

    n = len(items)
    k = k % n

    return items[n - k:] + items[:n - k]