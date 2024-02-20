def majorityElement(A):
    tempMajority = A[0]
    countMajority = 1

    for i in range(1, len(A)):
        if A[i] == tempMajority:
            countMajority += 1
        elif countMajority == 0:
            tempMajority = A[i]
            countMajority = 1
        else:
            countMajority -= 1

    return tempMajority


if __name__ == "__main__":
    B = [2, 2, 2, 2, 2, 3, 3, 3, 3]
    print(majorityElement(B))