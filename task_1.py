def min_max(arr: []) -> ():
    if not arr:
        return ()
    if len(arr) == 1:
        return arr[0], arr[0]
    if len(arr) == 2:
        if arr[0] > arr[1]:
            return arr[1], arr[0]
        else:
            return tuple(arr)
    middle = len(arr) // 2
    left = min_max(arr[:middle])
    right = min_max(arr[middle:])
    return min(left[0], right[0]), max(left[1], right[1])
