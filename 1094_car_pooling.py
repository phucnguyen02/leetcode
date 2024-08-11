import heapq

class Solution:
    def carPooling(self, trips, capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])
        space = []

        passengers = trips[0][0]
        space.append((trips[0][2], passengers))

        for trip in trips[1:]:
            if passengers > capacity:
                return False
            
            while space and trip[1] >= space[0][0]:
                popped = heapq.heappop(space)
                passengers -= popped[1]
            
            passengers += trip[0]
            heapq.heappush(space, (trip[2], trip[0]))
        
        return passengers <= capacity

if __name__ == "__main__":
    sol = Solution()
    print(sol.carPooling([[2,1,5],[3,3,7]], 4))
    print(sol.carPooling([[2,1,5],[3,3,7]], 5))


# First sort the trips by the start time. Use a heap to then push the first trip's end time into it.
# The heap keeps track of the trips that can occur at the same time as each other, with a passenger count attached.

# Iterate through every trip after that. If at one point we come across a trip whose start time is greater than the earliest trip's end time, then
# we start popping every trip in the heap whose start time is less than the current trip's end time, and update the passenger count.

# Append the trip to the heap and update the passenger count. If at any point the passenger count exceeds the capacity, we return false.