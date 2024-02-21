def findMissing(A, left, right):
    mid = (int) (left + right) // 2
    print("Front:" + str(A[left]) + " Mid:" + str(A[mid]) + " Back:" + str(A[right]))
    
    #End Case
    if left >= right:
        print("Back!")
        return A[right] + 1

    #Front Case
    if(A[left] != (left+1)):
        print("Front!")
        return A[left]-1
    
    #Mid Case
    if (A[mid]+1) != (A[mid+1]):
        return A[mid]+1
    
    #Missing Integer is in Right side
    if A[mid] == (mid+1) :
        return findMissing(A, mid+1, right)
    #Missing Int is in left side
    else:
        return findMissing(A, left, mid-1)
    

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

print(findMissing(A, 0, len(A)-1))