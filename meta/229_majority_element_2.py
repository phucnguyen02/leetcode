class Solution:

    def majorityElement(self, nums):
        if not nums:
            return []
        
        # 1st pass
        count1, count2, candidate1, candidate2 = 0, 0, None, None
        for n in nums:
            if candidate1 == n:
                count1 += 1
            elif candidate2 == n:
                count2 += 1
            elif count1 == 0:
                candidate1 = n
                count1 += 1
            elif count2 == 0:
                candidate2 = n
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        
        # 2nd pass
        result = []
        for c in [candidate1, candidate2]:
            if nums.count(c) > len(nums)//3:
                result.append(c)

        return result
    
# Majority Element 1 / Boyer Moore
# The idea is to have two variables, one holding a potential candidate for majority element and a counter to keep track of 
# whether to swap a potential candidate or not. Why can we get away with only two variables? Because there can be at most one majority element which is 
# more than ⌊n/2⌋ times. Therefore, having only one variable to hold the only potential candidate and one counter is enough.

# While scanning the array, the counter is incremented if you encounter an element which is exactly same as the potential candidate but decremented otherwise. 
# When the counter reaches zero, the element which will be encountered next will become the potential candidate. Keep doing this procedure while scanning the array. 
# However, when you have exhausted the array, you have to make sure that the element recorded in the potential candidate variable is the majority element by checking 
# whether it occurs more than ⌊n/2⌋ times in the array.