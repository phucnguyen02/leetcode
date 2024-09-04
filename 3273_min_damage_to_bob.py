import math
import functools

class Solution:
    def compare(self, en1, en2):
        if (en1[0] + en2[0]) * en1[1] + en2[0] * en2[1] > (en1[0] + en2[0]) * en2[1] + en1[0] * en1[1]:
            return 1
        elif (en1[0] + en2[0]) * en1[1] + en2[0] * en2[1] < (en1[0] + en2[0]) * en2[1] + en1[0] * en1[1]:
            return -1
        return 0
    
    def minDamage(self, power: int, damage, health) -> int:
        enemies = [(dmg, math.ceil(hp / power)) for (dmg, hp) in zip(damage, health)]
        enemies = sorted(enemies, key = functools.cmp_to_key(self.compare) )
        res = 0
        total_dmg = sum(damage)
        for (dmg, time) in enemies:
            res += total_dmg * time
            total_dmg -= dmg
        
        return res

if __name__ == "__main__":
    sol = Solution()
    print(sol.minDamage(4, [1,2,3,4], [4,5,6,8]))
    print(sol.minDamage(1, [1, 1, 1, 1], [1, 2, 3, 4]))
    print(sol.minDamage(8, [40], [59]))

# When choosing which to kill between 2 enemies, consider the time and damage you'll take when killing 1 before the other.
# We're comparing (dmg[0] + dmg[1]) * time[0] + dmg[1] * time[1] against (dmg[0] + dmg[1]) * time[1] + dmg[0] * time[0].
# Use this as a custom comparator to figure out the optimal order of killing.