class Solution:
    def multiply_two_integers(self, nums1, nums2):
        if nums1 == [0] or nums2 == [0]: return [0]
        if nums1 == [1]: return nums2
        if nums2 == [1]: return nums1

        len1, len2 = len(nums1), len(nums2)
        res = 0
        for i in range(len1 - 1, -1, -1):
            digit1 = nums1[i]
            inner_sum = 0
            for j in range(len2 - 1, -1, -1):
                digit2 = nums2[j]
                inner_sum += digit1*digit2*pow(10, len2 - j - 1)
            res += inner_sum * pow(10, len1 - i - 1)
        return [int(x) for x in str(res)]

if __name__ == "__main__":
    sol = Solution()
    print(sol.multiply_two_integers([1,2,3], [4,5,6]))
    print(sol.multiply_two_integers([1,2,3,4], [4,5,6]))
    print(sol.multiply_two_integers([1,2,3], [0]))
    print(sol.multiply_two_integers([1,2,3], [1]))

#[4,5,6]
#[1,2,3]

#inner_sum = 18
#inner_sum = 120 + 18
#inner_sum = 600 + 120 + 18
#res += inner_sum * 1

#inner_sum = 12
#inner_sum = 10*10 + 12
#inner_sum = 4*2*100 + 10*10 + 12
#res += inner_sum * 10


#For a digit in array 1 moving backwards, multiply it by every digit in array 2, 
# multiply that product by 10 to the iteration count
#Add up all the sums together multiplied by the iteration count.

#Edge cases:
#If either of the arrays is 0, return 0
#If either of the arrays is 1, return the other

# Pseudocode:
# res = 0
# for i = len(arr1) - 1, ..., 0
    # inner_sum = 0
    # for j = len(arr2) - 1, ..., 0
        # inner_sum += arr1[i]*arr2[j]*10^(len(arr2)-j-1)
    # res += inner_sum*10^(len(arr1)-i-1)
#return res
