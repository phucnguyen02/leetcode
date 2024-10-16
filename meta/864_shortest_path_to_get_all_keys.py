class Solution:
    def is_lock(self, value):
        return "A" <= value <= "F"
    
    def is_key(self, value):
        return "a" <= value <= "f"
    
    def unlockable(self, lock, keys):
        return keys & (1 << self.key_table[lock])

    def get_key(self, key_name, keys):
        return keys | (1 << self.key_table[key_name.upper()])
    
    def shortestPathAllKeys(self, grid) -> int:
        queue = []
        m, n = len(grid), len(grid[0])
        key_count = 0
        visited = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '@':
                    queue.append((i, j, 0, 0))
                    visited.add((i, j, 0))
                elif self.is_key(grid[i][j]):
                    key_count += 1

        self.key_table = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5}
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while queue:
            r, c, keys, dist = queue.pop(0)
            for (dr, dc) in directions:
                new_r = r + dr
                new_c = c + dc
                if not (0 <= new_r < m and 0 <= new_c < n):
                    continue

                if (new_r, new_c, keys) in visited:
                    continue
                
                new_cell = grid[new_r][new_c]
                if new_cell in ".@":
                    queue.append((new_r, new_c, keys, dist + 1))
                    visited.add((new_r, new_c, keys))

                elif self.is_lock(new_cell) and self.unlockable(new_cell, keys):
                    queue.append((new_r, new_c, keys, dist + 1))
                    visited.add((new_r, new_c, keys))
                
                elif self.is_key(new_cell):
                    new_keys = self.get_key(new_cell, keys)
                    queue.append((new_r, new_c, new_keys, dist + 1))
                    visited.add((new_r, new_c, new_keys))

                    if new_keys == (1 << key_count) - 1:
                        return dist + 1
        return -1

if __name__ == "__main__":
    sol = Solution()
    print(sol.shortestPathAllKeys(["@.a..","###.#","b.A.B"]))
    print(sol.shortestPathAllKeys(["@..aA","..B#.","....b"]))
    print(sol.shortestPathAllKeys(["@Aa"]))
    print(sol.shortestPathAllKeys(["@...a",".###A","b.BCc"]))

# Do BFS with a (r, c, keys) state. We store the keys we've picked up through a bitmask. We can go to the same (r, c) multiple times as
# long as we have a different set of keys each time.
# Every time we pick up a key, we update the bit for that respective key. Each letter has an index/bit corresponding to it.
# Every time we see a lock, we need to have the appropriate key for it. We can always look it up based on our hash table of indices.
# If we visit the final key, we return the distance we took to get there. Getting all keys would be the equivalent of all key bits being 1, or 2 ^ (key count) - 1.
