class Solution:
    def removeDuplicates(self, nums) -> int:
        if not nums: return 0
        pointer = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[pointer]:
                pointer += 1
                nums[pointer] = nums[i]
        return pointer + 1

if __name__ == "__main__":
    sol = Solution()
    print(sol.removeDuplicates([1,1,2,3]))
    print(sol.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))

# Use a pointer for the beginning elements of the array. Every time there's an element different from it, move it up and change it to be the different element.