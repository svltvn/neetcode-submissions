class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = ['+','-','*','/']
        for c in tokens:
            if c not in op:
                stack.append(int(c))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                if c == '+':
                    stack.append(num1+num2)
                elif c == '-':
                    stack.append(num1-num2)
                elif c == '*':
                    stack.append(num1*num2)
                elif c=='/':
                    if num1<0 or num2<0:
                        stack.append((abs(num1)//abs(num2))*-1)
                        stack
                    else:
                        stack.append(num1//num2)
                print (num1, c, num2)
                print(stack[-1])        
        return stack[0]
