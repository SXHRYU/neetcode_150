class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        operators = ("+", "-", "*", "/")
        
        for token in tokens:
            a = None
            b = None
            c = None
            
            if token in operators:
                a = stack.pop()
                b = stack.pop()
                c = self.operation(a, b, token)
                stack.append(c)
            else:
                stack.append(int(token))
        return stack.pop()
    
    def operation(self, a: int, b: int, operator: str) -> int:
        if operator == "+":
            return b + a
        elif operator == "-":
            return b - a
        elif operator == "*":
            return b * a
        elif operator == "/":
            return int(b / a)
