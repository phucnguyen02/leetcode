import heapq

class Solution:
    def merge_sorted_files(self, files):
        res = []
        pq = []
        for (i, file) in enumerate(files):
            heapq.heappush(pq, (file[0], i, 0))
        
        while pq:
            (elem, set_id, set_idx) = heapq.heappop(pq)
            res.append(elem)
            set_idx += 1
            if set_idx < len(files[set_id]):
                heapq.heappush(pq, (files[set_id][set_idx], set_id, set_idx))
        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.merge_sorted_files([(3, 5, 7), (0, 6), (0, 6, 28)]))


#Obvious solution:
#Put all the elements into an array, sort the array. TC is O(nlogn)

#Better solution:
#All of the sets are sorted, meaning that we can theoretically "iterate" through each set to get a sorted order of files
#Store the first elements of the k sets into a priority queue of size k using a tuple (elem, set_id, set_index)
#Elem being the element in each set, set_id being the current set number, and set_index being the index of the element in that set
#Pop the heap and store that element into the result array, increment the set_index of the corresponding set and insert the next element of that set
#TC is O(klogk)

# For i = 0, ..., k - 1
# Push the first element of k sets into the priority queue as (set[i], i, 0).
#While pq is not empty:
#Pop the first element of pq, get (elem, set_id, set_idx)
#Append elem into result
#Set_idx += 1
#If set_idx < len(set[set_id]) then add (set[set_id][set_idx], set_id, set_idx) into the pq
#Return result