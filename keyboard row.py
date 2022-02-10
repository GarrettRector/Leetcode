class Solution:
    def findWords(self, words):
        firstRow, secondRow, thirdRow = set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')
        ans = []
        for each in words:
            letters = set(each.lower())
            if len(letters - firstRow) == 0 or len(letters - secondRow) == 0 or len(letters - thirdRow) == 0:
                ans.append(each)
        return ans


if __name__ == "__main__":
    s = Solution()
    s.findWords(["qwertyuiop", "dad", "hello world"])
