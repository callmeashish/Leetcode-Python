class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows >= len(s) or numRows == 1:
            return s
        str_list = [""] * numRows
        counter = 0
        forward = True
        for value in s:
            if forward:
                str_list[counter] += value
                counter += 1
                if counter == numRows - 1:
                    forward = False
            else:
                str_list[counter] += value
                counter -= 1
                if counter == 0:
                    forward = True

        return "".join(str_list)


if __name__ == "__main__":
    print("PINALSIGYAHRPI" == Solution().convert("PAYPALISHIRING", 4))
