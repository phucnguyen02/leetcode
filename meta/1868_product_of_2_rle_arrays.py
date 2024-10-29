class Solution:
    def findRLEArray(self, encoded1, encoded2):
        ptr1 = ptr2 = 0
        res =  []
        prev_prod = None
        count = 0
        while ptr1 < len(encoded1) and ptr2 < len(encoded2):
            prod = encoded1[ptr1][0] * encoded2[ptr2][0]
            min_count = min(encoded1[ptr1][1], encoded2[ptr2][1])
            if encoded1[ptr1][1] == encoded2[ptr2][1]:
                ptr1 += 1
                ptr2 += 1
            
            elif min_count == encoded2[ptr2][1]:
                ptr2 += 1
                encoded1[ptr1][1] -= min_count

            else:
                ptr1 += 1
                encoded2[ptr2][1] -= min_count
            
            if prev_prod and prod != prev_prod:
                res.append([prev_prod, count])
                count = 0

            prev_prod = prod
            count += min_count
        
        res.append([prev_prod, count])
        return res
    
# Store 2 pointers to traverse through both arrays.
# If the count in 1 array is smaller than the other, then increment the pointer of that array, and subtract the count of the other by the count.
# If both counts are equal then increment both pointers.
# Once we have the min count, that's the number of times that product will be in the final array.
# If we encounter a different product than the one from before, reset the count and append the previous product and its count into the result

             