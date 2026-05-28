class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        '''
        Second attempt here, will see if I can build out constraints, then BF, then find optimal solution
        '''
        op = ["+", "-", "*", "/"]
        stack = []
        for c in tokens:
            print(stack)
            if c in op:
                print(c)
                x2 = stack.pop()
                x1 = stack.pop()
                if c == "+":
                    stack.append(x1+x2)
                elif c == "-":
                    stack.append(x1-x2)
                elif c == "*":
                    stack.append(x1*x2)
                elif c == "/":
                    res = int(x1/x2)
                    stack.append(res)
            else:
                stack.append(int(c))
            
        return stack[0]

                