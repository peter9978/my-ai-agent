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
        "hundred": 100,
        "thousand": 1000,
        "million": 1000000,
        "billion": 1000000000
    }
    
    
def parse_number_phrase(words):
    current = 0
    total = 0

    for word in words:

        if word == "and":
            continue

        value = number_words[word]

        if value == 100:
            current *= 100

        elif value >= 1000:
            total += current * value
            current = 0

        else:
            current += value

    return total + current




print(parse_number_phrase(["one", "thousand"]))
print(parse_number_phrase(["two", "thousand"]))
print(parse_number_phrase(["one", "million"]))
print(parse_number_phrase(["two", "hundred", "fifty", "thousand"]))
print(parse_number_phrase(["one", "hundred", "and", "twenty"]))


    
    
def split_operands(words):
    operands = []
    current_phrase = []



    for i, word in enumerate(words):
        if word == "and":
            next_word = words[i + 1] if i + 1 < len(words) else None

            if (
                current_phrase
                and next_word in number_words
                and "hundred" in current_phrase
            ):
                current_phrase.append(word)
            else:
                if current_phrase:
                    operands.append(current_phrase)
                    current_phrase = []
        else:
            current_phrase.append(word)

    if current_phrase:
        operands.append(current_phrase)

    return operands
    

print(split_operands(
    ["one", "hundred", "and", "twenty"]
))

print(split_operands(
    ["one", "hundred", "and", "twenty", "and", "thirty"]
))

print(split_operands(
    ["one", "thousand", "and", "two", "thousand"]
))
    
    
    

def parser(user_input):
    words = user_input.lower().split()

    numbers = []

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
    total = 0
    for word in words:
        clean_word = word.strip("?!.,")

        if clean_word in number_words:
            value = number_words[clean_word]

            if value == 100:
                current *= 100
            elif value >= 1000:
                total += current * value
                current = 0                
            else:
                current += value
        elif clean_word in ["and","from","by","to"]:
            if current != 0 or total != 0:
                  numbers.append(current + total)
                  current = 0
                  total = 0

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

    if current != 0 or total != 0:
        numbers.append(current + total)

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
    "multiply one hundred and twenty by two"
]

for test in tests:
    print(test, "->", agent(test))