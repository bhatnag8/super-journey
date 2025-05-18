class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for num in nums:
            if num in hashset: return True
            hashset.add(num)
        return False

'''
space analysis: O(n)
    hashset worst case is n elements so O(n)

time analysis: O(n)
    O(1) operation (add) n times

notes:
other methods:
- sorting O(n log n) time O(1) space
- brute force O(n^2) time O(1) space
- 1 liner length comparision O(n) time O(n) space

https://leetcode.com/problems/contains-duplicate/
'''
