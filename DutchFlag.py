def swap(letters, i, j):
    temp = letters[i]
    letters[i] = letters[j]
    letters[j] = temp
    return letters

def DutchFlag(letters):
    front = 0
    back = len(letters) - 1
    i = 0
    while i <= back:
        if(letters[i] == "W"):
            i += 1
            continue
        elif(letters[i] == "R"):
            letters = swap(letters, i, front)
            i += 1
            front += 1
        else:
            letters = swap(letters, i, back)
            back -= 1

    return letters

test1 = ["B", "R", "W", "W", "B", "R", "W", "W", "B", "B", "R"]
print(test1)
print(DutchFlag(test1))