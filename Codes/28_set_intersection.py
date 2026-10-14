def set_intersection(first, second):
    result = set()

    for item in first:
        if item in second:
            result.add(item)

    return result