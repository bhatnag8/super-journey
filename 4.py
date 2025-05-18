class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {
            # target
            # index
        }
        for i, num in enumerate(nums):
            check = target - num
            if check in hashmap: return [hashmap[check], i]
            else: hashmap[num] = i

'''
space analysis: O(n)
    worst case, stores each element in nums

time analysis: O(n)
    going through each element O(1) operations

notes:
brute force would be O(n^2) time and O(1) space
https://leetcode.com/problems/two-sum/
'''
