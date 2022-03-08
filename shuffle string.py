class Solution(object):
    def restoreString(self, s, indices):
        ans = list(range(len(s)))
        for i, indice in enumerate(indices):
            ans[indice] = s[i]
        return "".join(ans)


if __name__ == "__main__":
    s = Solution()
    print(s.restoreString("codeleet", [4, 5, 6, 7, 0, 2, 1, 3]))
