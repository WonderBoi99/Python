def merge_sort(arr):
    if len(arr) <= 1:
        return
    
    mid = len(arr) // 2

    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    merge_two_sorted_lists(left, right, arr)

def merge_two_sorted_lists(left, right , arr):
    l = r = o = 0

    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            arr[o] = left[l]
            l += 1
        else:
            arr[o] = right[r]
            r += 1
        o += 1

    while l < len(left):
        arr[o] = left[l]
        l += 1
        o += 1

    while r < len(right):
        arr[o] = right[r]
        r += 1
        o += 1






if __name__ == '__main__':
    test_cases = [
        [10, 3, 15, 7, 8, 23, 98, 29],
        [],
        [3],
        [9,8,7,2],
        [1,2,3,4,5]
    ]

    for arr in test_cases:
        merge_sort(arr)
        print(arr)