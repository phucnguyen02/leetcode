from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums) -> str:
        def compare(str1, str2):
            combine_1 = str1 + str2
            combine_2 = str2 + str1
            if combine_1 > combine_2:
                return -1
            elif combine_1 < combine_2:
                return 1
            return 0
        
        str_nums = sorted([str(num) for num in nums], key=cmp_to_key(compare))
        res = "".join(str_nums)
        trail_zero = -1
        for i in range(len(res) - 1):
            if res[i] == "0":
                trail_zero = i
            else:
                break
        return res[trail_zero + 1:]
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.largestNumber([10,2]))
    print(sol.largestNumber([3,30,34,5,9]))

# First convert all of the numbers into strings for easier comparison and we want to return a string at the end anywya
# When comparing between 2 strings and seeing what should be put first, just compare the results from combining both strings with 1 before the other and
# use that as the custom comparator function