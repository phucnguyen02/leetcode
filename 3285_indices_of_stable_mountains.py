class Solution:
    def stableMountains(self, height, threshold: int):
        return [i for i in range(1, len(height)) if height[i - 1] > threshold]

if __name__ == "__main__":
    sol = Solution()
    print(sol.stableMountains([1,2,3,4,5], 2))
    print(sol.stableMountains([10,1,10,1,10], 3))
    print(sol.stableMountains([10,1,10,1,10], 10))