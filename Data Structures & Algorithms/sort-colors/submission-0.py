class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0] * 3
        for num in nums:
            counts[num] += 1;
        j = 0
        for index, num in enumerate(counts):
            for i in range(num):
                nums[j] = index
                j += 1

        