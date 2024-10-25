class Solution:
    def compress(self, chars: List[str]) -> int:
        ptr = 0
        count = 0
        cur_char = chars[0]

        def compress_count():
            nonlocal ptr
            chars[ptr] = cur_char
            ptr += 1
            if count != 1:
                for ch in str(count):
                    chars[ptr] = ch
                    ptr += 1
        for i in range(len(chars)):
            if chars[i] == cur_char:
                count += 1
            else:
                compress_count()
                count = 1
                cur_char = chars[i]

        compress_count()
        return ptr
    
# Use 1 pointer to store the current position on the compressed array. Keep track of the current character we're processing as well.
# Each time the character is different from the current character, do compress_count. compress_count first updates chars[ptr] to be the previous character.
# Then it moves ptr forward while updating the elements to be the count.
# Do compress_count again at the end to account for the final character
        
