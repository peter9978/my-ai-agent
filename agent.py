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
    "ten": 10
}


    for word in words:
        clean_word = word.strip("?!.,")
        
        try:
            number = int(clean_word)
            numbers.append(number)
        except ValueError:
              try :
                    number = float(clean_word)
                    numbers.append(number)

              except ValueError:
                    if clean_word in number_words:
                        numbers.append(number_words[clean_word])

    



    for word in words:
        if word in ["multiply","multiplied"]:
            operation = "multiply"
        elif word in ["divide","divided"]:
            operation = "divide"
        elif word in ["add","plus"]:
            operation = "add"
        elif word in ["subtract","minus"]:
            operation = "subtract"



    relationship = None
    for word in words:
      if word in ["from", "by", "and", "to"]:
          relationship = word


    
   



    return {
        "operation": operation,
        "numbers": numbers,
        "relationship" : relationship
    }





def agent(user_input):
    parsed_data = parser(user_input)

    operation = parsed_data["operation"]
    number = parsed_data["numbers"]
    relationship = parsed_data["relationship"]

    if relationship == "from":
        return calculator (number[1],number[0],operation)
    elif relationship == "by":
        return calculator (number[0],number[1],operation)
    elif relationship == "and":
        return calculator (number[0],number[1],operation)
    elif relationship == "to":
        return calculator(number[0],number[1],operation)



print(agent("subtract ten from two"))




# user_input = input("User: ")

# result = agent(user_input)

# print("Agent:", result)


tests = [
    "add five and ten",
    "multiply three by four",
    "subtract ten from two",
    "divide ten by two",
    "add 10.5 and 2",
    "ADD 10 AND 20",
    "subtract -5 from 10"
]

for test in tests:
    try:
        print(test, "->", agent(test))
    except Exception as e:
        print(test, "-> ERROR:", e)