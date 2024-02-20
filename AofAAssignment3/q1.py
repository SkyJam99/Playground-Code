def merge(A, temp, left, mid, right):
    inversions = 0
    i = left
    j = mid + 1
    k = left
    

    while i <= mid and j <= right:
        if A[i] <= A[j]:
            temp[k] = A[i]
            i += 1
        else:
            temp[k] = A[j]
            j += 1
            #print(mid - i + 1)
            inversions += (mid - i + 1)

        k += 1

    while i <= mid:
        temp[k] = A[i]
        i += 1
        k += 1

    while j <= right:
        temp[k] = A[j]
        j += 1
        k += 1

    for i in range(left, right+1):
        A[i] = temp[i]

    return inversions



def countInversions(A, temp, left, right):
    totalInversions = 0
    if left < right:
        #print("Going Deeper")
        mid = (left + right) // 2
        totalInversions += countInversions(A, temp, left, mid)
        totalInversions += countInversions(A, temp, mid+1, right)
        totalInversions += merge(A, temp, left, mid, right)

    return totalInversions



def countInv(A):
    n = len(A)
    temp = [0] * n
    return countInversions(A, temp, 0, n-1)



A = [5, 4, 3, 2, 1]
B = [1, 3, 2]
C = [1, 2, 3]

print(countInv(A))
print(countInv(B))
print(countInv(C))

test_cases = [
    [1, 20, 6, 4, 5],  # Example from the explanation
    [1, 3, 5, 2, 4, 6],  # Mixed inversions
    [5, 4, 3, 2, 1],  # Descending order, maximum inversions
    [1, 2, 3, 4, 5],  # Ascending order, no inversions
    [],  # Empty array, no inversions
    [10],  # Single element, no inversions
]

# Running the test cases
results = [countInv(tc) for tc in test_cases]
print(results)