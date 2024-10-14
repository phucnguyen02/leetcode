from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        degrees = defaultdict(int)
        neighbors = defaultdict(list)
        for (start, end) in prerequisites:
            degrees[end] += 1
            neighbors[start].append(end)

        queue = [i for i in range(numCourses) if i not in degrees]
        res = []
        while queue:
            node = queue.pop(0)
            for neighbor in neighbors[node]:
                degrees[neighbor] -= 1
                if degrees[neighbor] == 0: queue.append(neighbor)

            res.append(node)

        return len(res) == numCourses
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.canFinish(2, [[1,0]]))
    print(sol.canFinish(2, [[1,0],[0,1]]))
    print(sol.canFinish(3, [[2,0], [1,0],[0,1]]))

# We want to find if there exists a topological sort order for the vertices in the graph.
# Use Kahn's algorithm to see if that's true.
# Store the degrees of every node (how many edges point to it)
# Add nodes with degree 0 to the queue.
# Pop the queue, reduce the degree of every node that the current popped node points to. If the degrees reduce to 0, add the nodes to the queue
# Repeat until the queue is empty
# The topological ordering is the popped nodes, provided every node is popped
# If it exists and is equal to the number of courses, return true. Otherwise, there is a cycle and we return false