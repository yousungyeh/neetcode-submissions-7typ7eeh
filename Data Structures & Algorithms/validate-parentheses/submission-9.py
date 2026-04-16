class Solution:
    def isValid(self, s: str) -> bool:
        # Using stack
        stack = []
        for c in s:
            if c!='}' and c!=']' and c!= ')':
                stack.append(c)
            else:
                if not stack:
                    return False
                else:
                    c_p = stack.pop()
                    if c=='}' and c_p=='{':
                        continue
                    elif c==']' and c_p=='[':
                        continue
                    elif c==')' and c_p=='(':
                        continue
                    else:
                        return False
        
        return stack == []
        