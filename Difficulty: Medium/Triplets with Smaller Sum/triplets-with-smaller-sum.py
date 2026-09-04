class Solution:
    def countTriplets(self, target, nums):

        nums.sort()
        count = 0

        for i in range(len(nums) - 2):

            left = i + 1
            right = len(nums) - 1

            while left < right:

                total = nums[i] + nums[left] + nums[right]

                if total < target:
                    count += right - left
                    left += 1

                else:
                    right -= 1

        return count