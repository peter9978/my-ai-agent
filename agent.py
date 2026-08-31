def calculator(a, b, operation):
    if operation == "multiply":
        return a * b
    elif operation == "divide":
        return a / b
    elif operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "difference":
        return abs(a - b)

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


    operation_words = {
    "add": "add",
    "plus": "add",
    "sum": "add",
    "total": "add",

    "subtract": "subtract",
    "minus": "subtract",
    "difference": "difference",

    "multiply": "multiply",
    "multiplied": "multiply",
    "times": "multiply",
    "product": "multiply",

    "divide": "divide",
    "divided": "divide",
    "over": "divide",
    "quotient": "divide",

    "+": "add",
    "-": "subtract",
    "*": "multiply",
    "/": "divide"
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
        if word in operation_words:
            operation = operation_words[word]


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

    if relationship == "from":
        number.reverse()

    if operation == "divide":
        for next_number in number[1:]:
            if next_number == 0:
                return "I can't divide by zero"

    result = number[0]

    for next_number in number[1:]:
        result = calculator(result, next_number, operation)

    return result




tests = [
    "add 10 and 20 and 30",
    "multiply 2 by 3 and 4",
    "subtract 100 from 50",
    "divide 100 by 5",
    "divide 100 by 5 and 2",
    "divide 100 by 5 and 0",
]

for test in tests:
    print(test, "->", agent(test))