def calculator(a, b, operation):
    if operation == "multiply":
        return a * b
    elif operation == "divide":
        return a / b
    elif operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b


def agent(user_input):
    new = user_input.split()

    operation = new[0]
    a = int(new[1])
    b = int(new[3])

    result = calculator(a, b, operation)
    return result


user_input = input("User: ")

result = agent(user_input)

print("Agent:", result)