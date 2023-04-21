def evalRPN(self, tokens: List[str]) -> int:
        token_stack = []

        op = {'+': lambda x, y: x + y,
              '-': lambda x, y: x - y,
              '*': lambda x, y: x * y,
              '/': lambda x, y: x / y}

        for val in tokens:

            if len(val) > 1:
                token_stack.append(int(val))
            elif ord(val) >= 48:
                token_stack.append(int(val))
            else:
                second = token_stack.pop()
                first = token_stack.pop()
                equation = op[val](first, second)
                token_stack.append(int(equation))

        return token_stack[0]
