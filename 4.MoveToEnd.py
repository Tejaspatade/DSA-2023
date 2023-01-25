# AlgoExpert Medium Arrays

def moveElementToEnd(arr, target):
    end = len(arr) - 1

    # Traversing from end to start of array TC:O(n)
    for i in range(end, -1, -1):
        # If arr[i] is the num to be moved to end of array
        if arr[i] == target:
            # Swap them in place
            arr[i], arr[end] = arr[end], arr[i]
            # Decremenet end
            end -= 1
    return arr
