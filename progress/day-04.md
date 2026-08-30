# Day 4 — Input Validation & Error Handling

## What I Built

Today I improved the agent's ability to handle invalid or incomplete user input without crashing.

### V1.3 Improvements

The agent can now detect:

* Missing operations
* Missing numbers
* Division by zero

Examples:

```text
hello
→ I don't understand the operation

add 10
→ I need two numbers

divide 10 by 0
→ I can't divide by zero
```

Valid input still works:

```text
add 10 and 20
→ 30

divide 10 by 2
→ 5.0
```

## What I Learned

I learned the importance of validating data before using it.

For example, accessing `number[1]` before checking that two numbers exist causes an `IndexError`.

The validation flow is now:

```text
Parser
  ↓
Check operation
  ↓
Check numbers
  ↓
Check division by zero
  ↓
Calculator
  ↓
Result
```

## Version

**V1.3 — Input Validation & Error Handling**

## Next

Build V1.4 by identifying the next limitation of the agent and solving it through a small experiment.
