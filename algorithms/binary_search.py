


def binary_search(numbers_list, number_to_find):
    left_index = 0
    right_index = len(numbers_list) - 1
    mid_index = 0

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = numbers_list[mid_index]

        if mid_number == number_to_find:
            return mid_index
        if mid_number < number_to_find:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1

    return -1

def binary_search_recursive(numbers_list, number_to_find, left_index, right_index):

    if left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = numbers_list[mid_index]
        if mid_number == number_to_find:
            return mid_index
        if mid_number < number_to_find:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1

        return binary_search_recursive(numbers_list, number_to_find, left_index, right_index)
    else:
        return -1
    
def find_occurances(numbers_list, number_to_find):
    index = binary_search(numbers_list, number_to_find)
    results = [index]

    #check left side
    i = index - 1
    while i >= 0:
        if numbers_list[i] == number_to_find:
            results.append(i)
        else:
            break
        i -= 1
    
    #check right side
    i = index + 1
    while i < len(numbers_list):
        if numbers_list[i] == number_to_find:
            results.append(i)
        else:
            break
        i += 1
    
    return sorted(results)
    

    



if __name__ == '__main__':
    numbers_list = [12, 15, 17, 19, 21, 24, 45, 67]
    number_to_find = 21

    index = binary_search(numbers_list, number_to_find)
    print(f"Number found at index {index} using binary search")
    index = binary_search_recursive(numbers_list, 12, 0, len(numbers_list)-1)
    print(f"Number found at index {index} using binary search")
    numbers = [1,4,6,9,11,15,15,15,17,21,34,34,56]
    number_to_find = 15 
    print(find_occurances(numbers, 15))