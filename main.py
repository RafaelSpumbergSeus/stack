from src.calculator import Calculator

if __name__ == "__name__":
    calc = Calculator()
    
    expression = input("Digite a expressão: ")
    try:
        result = calc.evaluate_postfix(expression)
        print(f"Resultado: {result}")
    except Exception as e:
        print(f"Erro: {e}")