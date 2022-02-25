class Solution(object):
    def generate(self, numRows):
        pt = []
        for row_num in range(numRows):
            row = [1] * (row_num + 1)
            for index in range(1, len(row) - 1):
                row[index] = pt[row_num - 1][index - 1] + pt[row_num - 1][index]
            pt.append(row)
        return pt


if __name__ == "__main__":
    s = Solution()
    s.generate(5)
