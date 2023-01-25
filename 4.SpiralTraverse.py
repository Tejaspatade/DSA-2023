# AlgoExpert Medium Arrays

def spiralTraverse(arr):
    res = []

    # Dimensions
    sRow = 0
    sCol = 0
    lRow = len(arr) - 1
    lCol = len(arr[0]) - 1

    while sRow <= lRow and sCol <= lCol:
        # Loop 1 start row
        for col in range(sCol, lCol + 1):
            res.append(arr[sRow][col])

        # Loop 2 last col
        for row in range(sRow + 1, lRow + 1):
            res.append(arr[row][lCol])

        # Loop 3 last Row
        for col in reversed(range(sCol, lCol)):
            if sRow == lRow:
                break
            res.append(arr[lRow][col])

        # Loop 4 start col
        for row in reversed(range(sRow + 1, lRow)):
            if sCol == lCol:
                break
            res.append(arr[row][sCol])

        # Increments
        sCol += 1
        sRow += 1
        lCol -= 1
        lRow -= 1
    return res
