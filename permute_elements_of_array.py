class Solution:
    def permute_elements(self, perm, arr):
        if not perm or not arr or len(perm) != len(arr): return arr
        for i in range(len(arr)):
            while perm[i] != i and 0 <= perm[i] < len(arr):
                arr[i], arr[perm[i]] = arr[perm[i]], arr[i]
                perm[perm[i]], perm[i] = perm[i], perm[perm[i]]
        return arr

if __name__ == "__main__":
    sol = Solution()
    print(sol.permute_elements([2, 0, 1, 3], ["a", "b", "c", "d"]))
    print(sol.permute_elements([2, 0, 5, 3], ["a", "b", "c", "d"]))
    print(sol.permute_elements([], ["a", "b", "c", "d"]))
    print(sol.permute_elements([2, 0, 5, 3], []))


#[a, b, c, d]
#[2, 0, 1, 3]

#[c,b,a,d]
#[1,0,2,3]

#[b,c,a,d]
#[0,1,2,3]

#Swap the elements of the array while also swapping the values of the permutations array.
#We keep doing the swapping until a permutation value matches the current index

#for i = 0, ..., n-1:
#   while perm[i] != i then:
#       swap arr[i] and arr[perm[i]]
#       swap perm[i] and perm[perm[i]]

