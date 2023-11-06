class Solution:
    def increment_arbitrary_interger(self, num):
        if not num: return []
        spare = 1
        for i in range(len(num) - 1, -1, -1):
            spare, num[i] = divmod(num[i] + spare, 10)
        return num if not spare else [1] + num


if __name__ == "__main__":
    sol = Solution()
    print(sol.increment_arbitrary_interger([1,2,3]))
    print(sol.increment_arbitrary_interger([1,2,9]))
    print(sol.increment_arbitrary_interger([9,9,9]))

# Iterate the array backwards. Increment the last element by 1. If an element incremented is equal to 10,
# we return its modulo with 10 and save the additional incrementation for the element before it.
# We keep doing so until the last element. If there's still incrementation to do, prepend 1 to the array.
# Otherwise, return the normal array


# Pseudocode:
# spare = 1
# for i = n - 1, ..., 0
# num[i] += spare
# spare = num[i] / 10 and num[i] %= 10
# if spare == 1 then return [1] prepend into num
# otherwise return num