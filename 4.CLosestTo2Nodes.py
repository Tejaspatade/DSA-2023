# Leetcode 2359 Find Closest Node to Given Two Nodes Medium
"""
You are given a directed graph of n nodes numbered from 0 to n - 1, where each node has at most one outgoing edge.

The graph is represented with a given 0-indexed array edges of size n, indicating that there is a directed edge from node i to node edges[i]. If there is no outgoing edge from i, then edges[i] == -1.

You are also given two integers node1 and node2.

Return the index of the node that can be reached from both node1 and node2, such that the maximum between the distance from node1 to that node, and from node2 to that node is minimized. If there are multiple answers, return the node with the smallest index, and if no possible answer exists, return -1.

Note that edges may contain cycles.

Input: edges = [2,2,3,-1], node1 = 0, node2 = 1
Output: 2
Explanation: The distance from node 0 to node 2 is 1, and the distance from node 1 to node 2 is 1.
The maximum of those two distances is 1. It can be proven that we cannot get a node with a smaller maximum distance than 1, so we return node 2.

Input: edges = [1,2,-1], node1 = 0, node2 = 2
Output: 2
Explanation: The distance from node 0 to node 2 is 2, and the distance from node 2 to itself is 0.
The maximum of those two distances is 2. It can be proven that we cannot get a node with a smaller maximum distance than 2, so we return node 2.
"""

import collections


class Solution:
    def closestMeetingNode(self, edges, n1: int, n2: int) -> int:
        # Create Adjacency List of the Graph
        adj = collections.defaultdict(list)
        # Each index in edges arr is src node and its value is the dest node
        for src, dest in enumerate(edges):
            # Add Dest as a neighbour to src in adj list
            adj[src].append(dest)

        # Create HashMaps from both nodes that denote dist to all nodes in graph
        n1Dist = {}
        n2Dist = {}
        # bfs for a src to all adjacents

        def bfs(src, distMap):
            # Queue for bfs
            q = collections.deque()
            # Add src to q
            q.append([src, 0])
            # Add src to distMap
            distMap[src] = 0
            # While queue isnt empty
            while q:
                # Pop front of q
                node, dist = q.popleft()
                # Loop thru neighbours for node
                for nei in adj[node]:
                    if nei not in distMap:
                        # Add to queue nei with distance of dist + 1
                        q.append([nei, dist + 1])
                        # Add to distMap
                        distMap[nei] = dist + 1
        # Perform dfs for n1 & n2 & populate the Hashmaps
        bfs(n1, n1Dist)
        bfs(n2, n2Dist)

        # Select nodes that can be reached by both n1 & n2,
        # take max dist of both distances & compare it with currently found closest node
        # to both nodes
        # Output
        res = -1
        resMinDist = float("inf")
        # Iterate all node nums
        for i in range(len(edges)):
            # Select nodes that can be reached by both n1 & n2
            if i in n1Dist and i in n2Dist:
                if resMinDist > max(n1Dist[i], n2Dist[i]):
                    res = i
                    resMinDist = max(n1Dist[i], n2Dist[i])

        return res
