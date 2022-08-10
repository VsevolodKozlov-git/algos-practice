class Solution:
    def isValid(self, s: str) -> bool:
        unclosed_braces_stack = []
        open_braces = '([{'
        close_braces = ')]}'
        for char in s:
            if char in open_braces:
                unclosed_braces_stack.append(char)
            elif (brace_index := close_braces.find(char)) != -1:
                if unclosed_braces_stack:
                    correspond_parent = unclosed_braces_stack.pop()
                else:
                    return False
                if correspond_parent != open_braces[brace_index]:
                    return False
        return len(unclosed_braces_stack) == 0

if __name__ == '__main__':
    s = "()[]{}"
    print(Solution().isValid(s))