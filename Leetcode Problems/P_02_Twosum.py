class Solution(object):
    def twoSum(self, nums, target):
        indexed_nums = [(num, i) for i, num in enumerate(nums)]
        indexed_nums.sort()

        left, right = 0, len(nums) - 1
        while left < right:
            curr_sum = indexed_nums[left][0] + indexed_nums[right][0]

            if curr_sum == target:
                return [indexed_nums[left][1], indexed_nums[right][1]]
            elif curr_sum < target:
                left += 1
            else:
                right -= 1

        return -1

    


sol = Solution()
nums= [1,4,6,7,10]
target= 11
last = sol.twoSum(nums,target)
print(last)
    
    