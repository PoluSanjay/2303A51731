"""class solution:
    def two_sum(self,nums,target):
        n={}
        for i,num in enumerate(nums):
            if target - num in n:
                return [n[target - num],i]
            n[num]=i
#input
nums = [2,7,11,15]
target = 9
#output
s = solution()
print(s.two_sum(nums,target))
"""

"""class Solution:
    def remove_duplicates(self, nums):
        updated = list(set(nums))
        return updated

nums = [1, 2, 3, 4, 5, 1, 2]
s = Solution()
print(s.remove_duplicates(nums))  # → [1, 2, 3, 4, 5]"""

#binary search
class Solution:
    def binary_search(self, nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1
nums = [1, 2, 3, 4, 5]
target = 3
s = Solution()
print(s.binary_search(nums, target))  # → 2

