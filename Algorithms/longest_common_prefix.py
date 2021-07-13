from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = ""
        if len(strs) == 1: return strs[0]

        strs = sorted(strs)
        for first, last in zip(strs[0], strs[-1]):
            if first == last: lcp+=first
            else: break
        return lcp

if __name__ == '__main__':
    print(Solution().longestCommonPrefix(["flower","flow","flight"]))