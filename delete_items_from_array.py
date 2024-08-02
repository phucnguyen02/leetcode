class Solution:
    def removeElement(self, nums, val: int) -> int:
        for ptr1 in range(len(nums)):
            if nums[ptr1] == val:
                for ptr2 in range(ptr1 + 1, len(nums)):
                    if nums[ptr2] != val:
                        nums[ptr1], nums[ptr2] = nums[ptr2], nums[ptr1]
                        break
        
        res = 0
        for num in nums:
            if num != val: res += 1
        
        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.removeElement([3,2,2,3], 3))
    print(sol.removeElement([0,1,2,2,3,0,4,2], 2))

# Every time we come across the element we want to delete, swap it with the nearest element that's not the deleted one. Keep doing it until the
# first part of the array is filled with non-deleteable elements.