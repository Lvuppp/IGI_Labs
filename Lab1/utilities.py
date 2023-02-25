
def make_math_operation(first_number, second_number, operation):
    if operation == "add":
        return first_number + second_number
    elif operation == "sub":
        return first_number - second_number
    elif operation == "mul":
        return first_number * second_number
    elif operation == "div":
        return first_number / second_number
    else:
        return "Unknown operation"
