class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(2):
            for num in nums: 
                ans.append(num)
        return ans

'''
space complexity: O(n)
time complexity: O(n)

notes:
if i assigned ans = nums then that would exceed output memory
probably since it the final answer would be O(3n) instead of O(2n)

returning nums + nums or nums * 2 would also be acceptable
'''

