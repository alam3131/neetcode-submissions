class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        stack.append('2')
        matchMap = {')' : '(', '}' : '{', ']' : '['}

        for i in s:
            if i in matchMap:
                if stack and stack.pop() != matchMap[i]:
                    return False
            else:
                stack.append(i)

        if stack.pop() == '2':
            return True
        else:
            return False
