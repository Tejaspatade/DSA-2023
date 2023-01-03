# 3/1
# Smallest Difference Between a pair from two arrays. AlgoExpert Medium Arrays

def smallestDifference(array1, array2):
    # Sort both arrays TC: O(nlogn + mlogm)
    array1.sort()
    array2.sort()

    # Pointers for traversal
    ptr1 = 0
    ptr2 = 0
    # Store best possible ans at any instance
    ans = []
    # Store smallest possible diff to compare with any newer differences we get
    bestDiffYet = float("inf")
    currentDiff = float("inf")

    # Iterate while both ptrs are valid indices of arrays
    while ptr1 < len(array1) and ptr2 < len(array2):
        num1 = array1[ptr1]
        num2 = array2[ptr2]
        if num1 < num2:
            currentDiff = num2 - num1
            ptr1 += 1
        elif num2 < num1:
            currentDiff = num1 - num2
            ptr2 += 1
        else:
            # Both nums are equal -> diff is 0
            return [num1, num2]
        if currentDiff < bestDiffYet:
            bestDiffYet = currentDiff
            ans = [num1, num2]

    return ans
