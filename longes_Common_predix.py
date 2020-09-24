# A Fucntion to find the string having the
# minimum length and returns that length

def findMinLength(strList):
    print(len(min(arr, key=len)))
    return len(min(arr, key=len))


def allContainsPrefix(strList, str, start, end):
    for i in range(start, end + 1):
        word = strList[i]
        print(word)
        for j in range(start, end + 1):
            if word[j] != str[j]:
                return False
    return True


# A Function that returns the longest
# common prefix from the array of strings
def CommonPrefix(strList):
    index = findMinLength(strList)
    prefix = ""  # our resuktant string

    # Binary search
    # on the first string of the array
    # in the range 0 to index
    low, high = 0, index - 1
    while low <= high:

        mid = int(low + (high - low) / 2)
        if allContainsPrefix(strList, strList[0],
                             low, mid):

            prefix = prefix + strList[0][low:mid + 1]

            low = mid + 1
        else:
            high = mid - 1

    return prefix


arr = ["aabbb", "aabaa", "aabbbbaa"]

lcp = CommonPrefix(arr)

if len(lcp) > 0:
    print("The longest common prefix is " + str(lcp))
else:
    print("There is no common prefix")
