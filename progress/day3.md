# Day 3 — Parser Improvements & V1.2

## What I Built

Today I improved the calculator agent's parser and made it more flexible.

### 1. Case normalization

The parser now converts user input to lowercase:

```python
words = user_input.lower().split()
```

This allows inputs like:

```text
ADD 10 AND 20
```

to work correctly.

### 2. Decimal and negative numbers

The parser can now recognize:

```text
10
10.5
-5
-2.75
```

It tries `int()` first and then `float()`.

### 3. English number words

Added a dictionary that maps English number words to numeric values:

```python
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
```

The parser can now understand inputs such as:

```text
add five and ten
multiply three by four
subtract ten from two
```

## What I Learned

I learned that parsing natural language is mainly about identifying and converting different representations of the same information.

For example:

```text
"10" → 10
"10.5" → 10.5
"-5" → -5
"five" → 5
```

I also learned to debug by testing different inputs, finding what fails, understanding why it fails, and making the smallest change necessary.

## Testing

The agent successfully handled:

```text
What is 10 multiplied by 64? → 640
please add 10 and 20 → 30
subtract 20 from 50? → 30
what's 100 divided by 4 → 25.0
ADD 10 AND 20 → 30
multiply 10.5 by 2 → 21.0
subtract 5 from 100!!! → 95
subtract ten from two → -8
```

## Version

Current version:

**V1.2 — English Number Parser**

### Version history

* V1.0 — Basic calculator agent
* V1.1 — Flexible natural-language parser
* V1.2 — English number understanding

## Next

V1.3 will focus on validation and graceful error handling.

The goal is not only to calculate correctly, but also to recognize invalid or incomplete user input and respond appropriately.
