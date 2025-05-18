class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(2):
            for num in nums:
                ans.append(num)
        return ans

'''
space analysis: O(n)
    excess memory apart from nums is O(n) which is the output array

time analysis: O(n)
    O(1) operation n times, twice

notes:
if i assigned ans = nums then that would exceed output memory
because it would be making a pointer to nums called ans
and i would be modifying nums while iterating over it basically.
the cleaner way would be ans = nums.copy() or ans = list(nums)

returning nums + nums or nums * 2 would also be acceptable

https://leetcode.com/problems/concatenation-of-array/
'''
