def merge_sort(A):
    # base case of recursion : return A
    if len(A) < 2:
        return A
    # divide array into 2 arrays, left and right
    left = A[:len(A) / 2]
    right = A[len(A) / 2:]
    # divide to smaller part via recursion
    left = merge_sort(left)
    right = merge_sort(right)

    # return merge result
    combined = merge(left, right)
    return combined

def merge(left, right):
    combined_array = []
    # let left_counter be the tracker for # of element left placed into combined
    # let right_counter be the tracker for # of element right placed into combined

    left_counter = 0
    right_counter = 0

    # while loop if there are element in both left and right array
    while left_counter < len(left) and right_counter < len(right):
        if left[left_counter] < right[right_counter]:
            combined_array.append(left[left_counter])
            left_counter += 1
        else:
            combined_array.append(right[right_counter])
            right_counter += 1

    while left_counter < len(left):
        combined_array.append(left[left_counter])
        left_counter += 1

    while right_counter < len(right):
        combined_array.append(right[right_counter])
        right_counter += 1
    return combined_array

original_array = [9, 7, 12, 6, 5, 3, 1]
new_array = merge_sort(original_array)
print new_array
