def merge_and_count(arr, temp, left, mid, right):
    i, j, k = left, mid + 1, left
    inv_count = 0
    
    # Merge the two halves while counting inversions
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            k += 1
            i += 1
        else:
            # There are (mid - i + 1) inversions, as the left and right sub-arrays are sorted
            temp[k] = arr[j]
            inv_count += (mid - i + 1)
            k += 1
            j += 1
    
    # Copy the remaining elements of left subarray (if there are any)
    while i <= mid:
        temp[k] = arr[i]
        k += 1
        i += 1
    
    # Copy the remaining elements of right subarray (if there are any)
    while j <= right:
        temp[k] = arr[j]
        k += 1
        j += 1
    
    # Copy back the merged elements to original array
    for i in range(left, right + 1):
        arr[i] = temp[i]
    
    return inv_count

def merge_sort_and_count(arr, temp, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right) // 2
        
        # Count inversions in the left half
        inv_count += merge_sort_and_count(arr, temp, left, mid)
        
        # Count inversions in the right half
        inv_count += merge_sort_and_count(arr, temp, mid + 1, right)
        
        # Count cross inversions
        inv_count += merge_and_count(arr, temp, left, mid, right)
    
    return inv_count

def count_inversions(arr):
    n = len(arr)
    temp = [0] * n  # Temporary array to be used for merging
    return merge_sort_and_count(arr, temp, 0, n - 1)

# Test cases
test_cases = [
    [1, 20, 6, 4, 5],  # Example from the explanation
    [1, 3, 5, 2, 4, 6],  # Mixed inversions
    [5, 4, 3, 2, 1],  # Descending order, maximum inversions
    [1, 2, 3, 4, 5],  # Ascending order, no inversions
    [],  # Empty array, no inversions
    [10],  # Single element, no inversions
]

# Running the test cases
results = [count_inversions(tc) for tc in test_cases]
print(results)
