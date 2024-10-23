# """
# This is GridMaster's API interface.
# You should not implement it, or speculate about its implementation
# """
#class GridMaster(object):
#    def canMove(self, direction: str) -> bool:
#        
#
#    def move(self, direction: str) -> bool:
#        
#
#    def isTarget(self) -> None:
#        
#

class Solution(object):
    def findShortestPath(self, master: 'GridMaster') -> int:
        visited = set()
        inverse = {"U": "D", "D": "U", "L": "R", "R": "L"}
        directions = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
        target = None
        def dfs(r, c):
            nonlocal target
            if master.isTarget():
                target = (r, c)
            
            visited.add((r, c))

            for d in directions:
                new_r, new_c = r + directions[d][0], c + directions[d][1]
                if (new_r, new_c) not in visited and master.canMove(d):
                    master.move(d)
                    dfs(new_r, new_c)
                    master.move(inverse[d])
        dfs(0, 0)
        if not target: return -1

        queue = [(0, 0, 0)]
        while queue:
            r, c, dist = queue.pop(0)
            
            if (r, c) == target: return dist
            for d in directions:
                new_r, new_c = r + directions[d][0], c + directions[d][1]
                if (new_r, new_c) in visited:
                    visited.remove((new_r, new_c))
                    queue.append((new_r, new_c, dist + 1))
        return -1

                
# First do DFS to mark every grid the robot can traverse to and make sure it can reach the target
# Then do BFS to go through every traverseable cell until you reach the target