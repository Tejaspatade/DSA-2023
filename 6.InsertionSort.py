# AlgoExpert Insertion Sort Easy

def insertionSort(arr):
    # Iterate from 1 to last index
    # i denotes start of unsorted subarray's start index
    for i in range(1, len(arr)):
        # Find i's correct place to be inserted in sorted subarr
        j = i
        while j > 0 and arr[j] < arr[j-1]:
            # Swap
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1
    return arr
