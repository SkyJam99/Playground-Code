def findMissing(A, front, back):
    mid = (int) (front + back) // 2
    print("Front:" + str(A[front]) + " Mid:" + str(A[mid]) + " Back:" + str(A[back]))
    
    #End Case
    if front >= back:
        print("Back!")
        return A[back] + 1

    #Front Case
    if(A[front] != (front+1)):
        print("Front!")
        return A[front]-1
    
    #Mid Case
    if (A[mid]+1) != (A[mid+1]):
        return A[mid]+1
    
    #Missing Integer is in Right side
    if A[mid] == (mid+1) :
        return findMissing(A, mid+1, back)
    #Missing Int is in left side
    else:
        return findMissing(A, front, mid-1)
    

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

print(findMissing(A, 0, len(A)-1))