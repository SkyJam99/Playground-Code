def countInversions(A, front, back):
    inversions = 0
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
    
    inversions += countInversions(A, front, (back / 2) - 1)
    inversions += countInversions(A, back / 2, back)
    

    

A = [3, 2, 1]
B = [1, 3, 2]
C = [1, 2, 3]

print(countInversions(A, 0, len(A)-1))
print(countInversions(B, 0, len(B)-1))
print(countInversions(C, 0, len(C)-1))