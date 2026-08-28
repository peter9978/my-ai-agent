def calculator(a, b, operation):
    if operation == "multiply":
        return a * b
    elif operation == "divide":
        return a / b
    elif operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b

def parser(user_input):
    words = user_input.split()

    numbers = []

    for word in words:
        clean_word = word.strip("?!.,")
        if  clean_word.isdigit():
            numbers.append(int(clean_word))

    for word in words:
        if word in ["multiply","multiplied"]:
            operation = "multiply"
        elif word in ["divide","divided"]:
            operation = "divide"
        elif word in ["add","plus"]:
            operation = "add"
        elif word in ["subtract","minus"]:
            operation = "subtract"

    return {
        "operation": operation,
        "numbers": numbers
    }


def agent(user_input):
    parsed_data = parser(user_input)

    operation = parsed_data["operation"]
    number = parsed_data["numbers"]

    return calculator(number[0],number[1],operation)


result = agent("subtract 100 from 35")
print(result)

user_input = input("User: ")

result = agent(user_input)

print("Agent:", result)