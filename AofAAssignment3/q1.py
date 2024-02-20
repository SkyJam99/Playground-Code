

def merge(A, left, mid, right):
    if left >= right: return 0

    inversions = 0
    i = 0
    j = 0
    k = left
    ALeft = A[left:mid]
    ARight = A[mid+1:right]
    print(ALeft)
    lengthL = len(ALeft)
    lengthR = len(ARight)

    while i < lengthL and j < lengthR:
        if ALeft[i] <= ARight[j]:
            A[k] = ALeft[i]
            i += 1
        else:
            A[k] = ARight[j]
            j += 1
            inversions += (lengthL - i + 1)

        k += 1

    while i < lengthL:
        A[k] = ALeft[i]
        i += 1
        k += 1

    while j < lengthR:
        A[k] = ARight[j]
        j += 1
        k += 1

    return inversions



def countInversions(A, left, right):
    totalInversions = 0
    if left < right:
        print("Going Deeper")
        mid = (left + right) // 2
        totalInversions += countInversions(A, left, mid)
        totalInversions += countInversions(A, mid+1, right)
        totalInversions += merge(A, left, mid, right)
    else:
        print("Array length 1")

    return totalInversions







A = [5, 4, 3, 2, 1]
B = [1, 3, 2]
C = [1, 2, 3]

print(countInversions(A, 0, len(A)-1))
print(countInversions(B, 0, len(B)-1))
print(countInversions(C, 0, len(C)-1))