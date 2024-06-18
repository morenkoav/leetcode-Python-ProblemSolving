class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        answer = []
        two_sum = 0
        for i in range(0,len(nums)):
            for j in range(i+1, len(nums)):
                two_sum = nums[i]+nums[j]
                if two_sum == target:
                    answer = [i,j]
                    break
                else:
                    continue
        return answer