class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num_stack = []
        operators = ['+', '-', '*', '/']
        for t in tokens:
            if t == '+':
                num2 = num_stack.pop()
                num1 = num_stack.pop()
                num_stack.append(num1+num2)
            elif t == '-':
                num2 = num_stack.pop()
                num1 = num_stack.pop()
                num_stack.append(num1-num2)
            elif t == '*':
                num2 = num_stack.pop()
                num1 = num_stack.pop()
                num_stack.append(num1*num2)
            elif t == '/':
                num2 = num_stack.pop()
                num1 = num_stack.pop()
                num_stack.append(int(num1/num2))
            else:
                num_stack.append(int(t))
        return int(num_stack[-1])

        