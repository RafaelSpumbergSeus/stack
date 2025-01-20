def is_valid_postfix(expression):
    tokens = expression.split()
    operand_count = 0
    
    for token in tokens:
        if token.isdigit():
            operand_count += 1
        elif token in "+-*/":
            operand_count -=1
            if operand_count <1:
                return False
        else:
            return False
        
    return operand_count == 1
                