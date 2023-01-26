# Leetcode 787 Cheapest Flights Within K Stops
"""
There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.

 Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
Output: 700
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.
"""


class Solution:
    def findCheapestPrice(self, n: int, flights, src: int, dst: int, k: int) -> int:
        # Price to reach every city node set to infinity initially
        prices = [float("inf")] * n
        # Price to reach source node is 0
        prices[src] = 0

        # Iterate thru all graph edges k+1 times since we can have k stops in btwn
        for i in range(k+1):
            # Temp copy
            tmp = prices.copy()

            # All edges
            for src, dest, cost in flights:
                # If reaching src costs inf, skip this edge
                if prices[src] == float("inf"):
                    continue
                # If reaching dest thru src costs lesser than what it does right now, update it
                if prices[src] + cost < tmp[dest]:
                    tmp[dest] = prices[src] + cost

            # Update Prices
            prices = tmp
        return -1 if prices[dst] == float("inf") else prices[dst]
