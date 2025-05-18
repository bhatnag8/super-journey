class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmaps = {}
        hashmapt = {}

        for c in s:
            if c in hashmaps: hashmaps[c] += 1
            else: hashmaps[c] = 0
        for c in t:
            if c in hashmapt: hashmapt[c] += 1
            else: hashmapt[c] = 0
        return hashmaps == hashmapt

'''
space analysis: O(1)
    technically worst case is O(26) * 2: two hashmaps, 26 characters

time analysis: O(n + m)
    O(n + m) n = len(s), m = len(t)

notes:
another alternate solution would be to sort the strings and if they are equal,
then s and t are anagrams. O(nlogn + mlogm) time and O(1) space
ask interviewer if sorting algorithm should take extra space or nah

https://leetcode.com/problems/valid-anagram/
'''
