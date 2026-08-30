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
    words = user_input.lower().split()

    numbers = []

    number_words = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "ten": 10,
        "eleven": 11,
        "twelve": 12,
        "thirteen": 13,
        "fourteen": 14,
        "fifteen": 15,
        "sixteen": 16,
        "seventeen": 17,
        "eighteen": 18,
        "nineteen": 19,
        "twenty": 20,
        "thirty": 30,
        "forty": 40,
        "fifty": 50,
        "sixty": 60,
        "seventy": 70,
        "eighty": 80,
        "ninety": 90,
        "hundred": 100
    }

    current = 0

    for word in words:
        clean_word = word.strip("?!.,")

        if clean_word in number_words:
            value = number_words[clean_word]

            if value == 100:
                current *= 100
            else:
                current += value
        elif clean_word in ["and","from","by","to"]:
            if current != 0:
                  numbers.append(current)
                  current = 0

        else:
            try:
                number = int(clean_word)
                numbers.append(number)

            except ValueError:
                try:
                    number = float(clean_word)
                    numbers.append(number)

                except ValueError:
                    pass

    if current != 0:
        numbers.append(current)

    operation = None

    for word in words:
        if word in ["multiply", "multiplied"]:
            operation = "multiply"
        elif word in ["divide", "divided"]:
            operation = "divide"
        elif word in ["add", "plus"]:
            operation = "add"
        elif word in ["subtract", "minus"]:
            operation = "subtract"

    relationship = None

    for word in words:
        if word in ["from", "by", "and", "to"]:
            relationship = word

    return {
        "operation": operation,
        "numbers": numbers,
        "relationship": relationship
    }


def agent(user_input):
    parsed_data = parser(user_input)

    operation = parsed_data["operation"]
    number = parsed_data["numbers"]
    relationship = parsed_data["relationship"]

    if operation is None:
        return "I don't understand the operation"

    if len(number) < 2:
        return "I need two numbers"

    if operation == "divide" and number[1] == 0:
        return "I can't divide by zero"

    if relationship == "from":
        return calculator(number[1], number[0], operation)

    elif relationship in ["by", "and", "to", None]:
        return calculator(number[0], number[1], operation)


tests = [
    "what is the sum of 10 and 20",
    "what is 10 plus 20",
    "what is 10 times 5",
    "what is the difference between 50 and 20",
    "what is 100 divided by 4",
]

for test in tests:
    print(test, "->", parser(test))