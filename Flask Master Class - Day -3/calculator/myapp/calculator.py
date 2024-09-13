import operator

def safe_eval(expression):
    """
    Safely evaluate a mathematical expression.
    Supports addition, subtraction, multiplication, and division.
    """
    # Define allowed operators
    operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }
    
    def parse_expression(expr):
        # Remove all whitespace
        expr = ''.join(expr.split())
        
        # Tokenize the expression
        tokens = []
        current_token = ''
        for char in expr:
            if char in operators or char in '()':
                if current_token:
                    tokens.append(float(current_token))
                    current_token = ''
                tokens.append(char)
            else:
                current_token += char
        if current_token:
            tokens.append(float(current_token))
        
        return tokens

    def evaluate(tokens):
        if len(tokens) == 1:
            return tokens[0]
        
        # Find the last operator (to respect order of operations)
        for i in range(len(tokens) - 1, -1, -1):
            if tokens[i] in operators:
                left = evaluate(tokens[:i])
                right = evaluate(tokens[i+1:])
                return operators[tokens[i]](left, right)
        
        # If we get here, we have parentheses
        if tokens[0] == '(' and tokens[-1] == ')':
            return evaluate(tokens[1:-1])
        
        raise ValueError("Invalid expression")

    try:
        tokens = parse_expression(expression)
        result = evaluate(tokens)
        return result
    except Exception as e:
        raise ValueError(f"Error evaluating expression: {str(e)}")