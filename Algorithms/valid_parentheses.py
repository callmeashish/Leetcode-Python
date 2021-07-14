class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        end_dict = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in end_dict.values():
                stack.append(char)
            else:
                if stack == []:
                    return False
                prev = stack.pop()
                if not end_dict[char] == prev:
                    return False
        if stack == []:
            return True
        return False

if __name__ == '__main__':
    print(Solution().isValid("{[]}"))