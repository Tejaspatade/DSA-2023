# 3/1
# First Non-Constructible Change From Coins AlgoExpert Medium Arrays

def nonConstructibleChange(coins):
    # Edge Case
    if not coins:
        return 1
    # Sort Coins TC:O(nlogn)
    coins.sort()

    # variable storing min change we can make at any instance
    # SC:O(1)
    curChange = 0
    # Iterate through our coins TC:O(n)
    for coin in coins:
        # Check if coin is greater that curChange + 1
        # This indicates that we can't make the value curChange + 1
        if coin > curChange + 1:
            return curChange + 1
        # if the coin is curChange + 1 or lower...
        # that means we can make curChange + 1 by just using that coin
        # This also means that we can make coin + curChange and any value in between as well
        curChange += coin
    # If we reached end of array, this means we can make all change from 1 to curChange
    # So our ans would be curChange + 1 again
    return curChange + 1
