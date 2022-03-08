class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        ans = [stone for stone in stones if stone in jewels]
        return len(ans)


if __name__ == "__main__":
    s = Solution()
    s.numJewelsInStones("aA", "aAAbbbb")
