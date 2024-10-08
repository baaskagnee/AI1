
def match(input_expression):
    try:
        # Evaluate the input expression
        result = eval(input_expression)
        return(result)
    except Exception as e:
        print(f"Error evaluating expression: {e}")

input_expression = "4*95+1"
match(input_expression)
