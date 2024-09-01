class Solution:
    def hammingDistanceString(self, word1: str, word2: str) -> int:
        str1 = ''.join(format(ord(i), '08b') for i in word1)
        str2 = ''.join(format(ord(i), '08b') for i in word2)
        if len(str1) < len(str2):
            str1 = "0"*(len(str2)-len(str1)) + str1
        else:
            str2 = "0"*(len(str1)-len(str2)) + str2
        return sum([1 if str1[i] != str2[i] else 0 for i in range(len(str1))])

if __name__ == "__main__":
    sol = Solution()
    print(sol.hammingDistanceString("this is a test", "wokka wokka!!!"))