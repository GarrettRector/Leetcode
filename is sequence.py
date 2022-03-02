class Solution(object):
    def isSubsequence(self, s, t):
        for c in t:
            if len(s) == 0: return True
            if s[0] == c: s = s[1:]
        return len(s) == 0


if __name__ == "__main__":
    s = Solution()
    s.isSubsequence("aaaaaa", "bbaaaa")
