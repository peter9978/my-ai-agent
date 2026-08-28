# Day 2 - V1.1

## What I Built

Improved the parser so it can:

* Extract numbers from user input
* Remove basic punctuation
* Detect arithmetic operations
* Return parsed data using a dictionary
* Connect the parser to the calculator through the agent

## What I Learned

* `split()`
* `strip()`
* `isdigit()`
* Lists
* Dictionaries
* Functions
* `return`
* Basic parsing

## Example

```text
What is 10 multiplied by 64?
```

Parser result:

```python
{
    "operation": "multiply",
    "numbers": [10, 64]
}
```

Calculator result:

```text
640
```

## Bug Discovered

```text
subtract 100 from 35
```

The current parser calculates:

```text
100 - 35 = 65
```

But the correct meaning is:

```text
35 - 100 = -65
```

## Next Step

Improve the parser so it can understand the relationship and order of numbers in natural language.
