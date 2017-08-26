class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest = 0

        nums_set = set(nums)

        for num in nums_set:
            if not num - 1 in nums_set:
                nxt = num + 1

                while nxt in nums_set:
                    nxt += 1

                longest = max(longest, nxt - num)

        return longest