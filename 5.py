class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # # generate the prefixes
        # prefixes = {
        #     # prefix
        #     # count
        # }
        # if "" in strs: return ""
        # for st in strs:
        #     for i in range(len(st)):
        #         pr = st[0:i+1]
        #         if pr in prefixes: prefixes[pr] += 1
        #         else: prefixes[pr] = 1

        # if not prefixes: return ""
        # highest_count = max(prefixes.values())
        # if highest_count != len(strs): return ""
        # longest_prefix = ""
        # for k, v in prefixes.items():
        #     if v == highest_count:
        #         if len(k) > len(longest_prefix): longest_prefix = k
        # return longest_prefix

        pre = ""
        for i in range(len(strs[0])):
            for st in strs:
                if i >= len(st) or st[i] != strs[0][i]:
                    return pre
            pre += strs[0][i]
        return pre

'''
space analysis: O(1)
    not storing anything except worst case, the shortest string

time analysis: O(n*m)
    going through each element O(1) operations

notes:
alternate approach is hashmap count of each prefix and returning
the longest prefix which has the highest count (equal to the len of strs)
hashmap complex: time O(n*m) space O(n*m)

https://leetcode.com/problems/longest-common-prefix/
'''
