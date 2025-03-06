def min_k(arr: [], k: int, l=0):
    length_of_arr = len(arr)
    if not arr:
        return "Array is empty"
    if length_of_arr + l == 1:
        return arr[0]
    if length_of_arr + l < k:
        return "Array is smaller then k"
    else:
        pivot = arr[length_of_arr // 2]

        left = [x for x in arr if x < pivot]
        right = [x for x in arr if x > pivot]
        new_arr = left + [pivot] + right
        new_pivot_index = new_arr.index(pivot)
        if k == new_pivot_index + l + 1:
            return pivot
        elif k > new_pivot_index + l + 1:
            return min_k(right, k, new_pivot_index + l + 1)
        else:
            return min_k(left, k, l)
