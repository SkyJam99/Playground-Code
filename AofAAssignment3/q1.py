def countInversions(A):
    inversions = 0
    front = 0
    mid = len(A) // 2
    back = len(A) - 1
    #Base case, one element in array
    if len(A) == 1:
        return inversions
    
    ALeft = A[0:mid - 1]
    ARight = A[mid:len(A)-1]

    inversions += countInversions(ALeft)
    inversions += countInversions(ARight)

    


def countInversionsOld(A, front, back):
    inversions = 0
    mid = (front+back) // 2

    if (back - front) < 2: 
        if A[front] > A[back]: 
            return 1
        else:
            return 0
    if (back - front) == 2:
        if A[front] > A[front+1]: inversions += 1
        if A[front] > A[back]: inversions += 1
        if A[front+1] > A[back]: inversions += 1
        return inversions
    
    inversions += countInversions(A, front, mid)
    inversions += countInversions(A, mid+1, back)
    
    i = front
    j = mid+1


    while i < mid+1 and j < back+1:
        if A[i] > A[j]:
            inversions += 1
            i += 1
        else:
            j += 1

    #
    

    

A = [3, 2, 1]
B = [1, 3, 2]
C = [1, 2, 3]

print(countInversions(A, 0, len(A)-1))
print(countInversions(B, 0, len(B)-1))
print(countInversions(C, 0, len(C)-1))