from scr.stack import Stack

class Calculator:
    def __init__(self):
        self.stack = Stack()
    
    def evaluate_postfix(self, expression):
        tokens = expression.split()

        for token in tokens:
            if token.isdigit():
                self.stack.push(int(token))
            elif token in "+-*/":
                if self.stack.size() < 2:
                    raise ValueError("Faltam operandos")  

                b = self.stack.pop()
                a = self.stack.pop() 
                self.stack.push(result)
            else:
                raise ValueError(f"Token inválido")
            
        if self.stack.size() != 1:
            raise ValueError("Faltam operandos")

        return self.stack.pop()
    
    def apply_operator(self, a, b, operator):
        if operator == '+':
            return a + b
        elif operator == '-':
            return a - b
        elif operator == '*':
            return a * b
        elif operator == '/':
            if b == 0:
                raise ZeroDivisionError("Divisão por zero")
            return a / b
        else:
            raise ValueError(f"Operador inválido: {operator}")
         