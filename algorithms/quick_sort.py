def partitions(arr, start, end):
    archor_index = start
    archor = arr[archor_index]

    while start < end:
        while start < len(arr) and arr[start] <= archor:
            start += 1

        while arr[end] > archor:
            end -= 1

        if start < end and start != end:
            arr[start], arr[end] = arr[end], arr[start]
    
    arr[end], arr[archor_index] = archor, arr[end]
    return end

def quick_sort(arr, start, end):
    if start < end:
        pi = partitions(arr, start, end)
        #sort left side
        quick_sort(arr, start, pi - 1)
        #sort right side
        quick_sort(arr, pi + 1, end)


     



if __name__ == '__main__':
    elements = [11,9,29,7,2,15,28]
    # elements = ["mona", "dhaval", "aamir", "tina", "chang"]
    partitions(elements, 0, len(elements)-1)
    print(elements)

    tests = [
        [11,9,29,7,2,15,28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]

    for elements in tests:
        quick_sort(elements, 0, len(elements)-1)
        print(f'sorted array: {elements}')