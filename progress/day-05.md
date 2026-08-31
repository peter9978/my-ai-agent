# Day 5 - V1.5 Semantic & Multi-Number Handling

## Goal

Improve the agent's ability to understand different representations of mathematical operations and handle more than two numbers.

## What I Built

### 1. Operation Normalization

Added an `operation_words` dictionary to map different representations to canonical operations.

Examples:

- `plus` → `add`
- `sum` → `add`
- `times` → `multiply`
- `over` → `divide`
- `+` → `add`
- `-` → `subtract`
- `*` → `multiply`
- `/` → `divide`

The parser converts different user representations into one internal operation.

### 2. Semantic Difference

Added support for the difference operation.

- `subtract 20 from 50` → `30`
- `what is the difference between 20 and 50` → `30`

The calculator handles the difference using absolute distance.

### 3. Multiple Numbers

The agent can now process more than two numbers.

Example:

`add 10 and 20 and 30` → `60`

`multiply 2 by 3 and 4` → `24`

The agent uses an accumulator:

1. Start with the first number.
2. Calculate with the next number.
3. Store the result.
4. Continue with the next number.
5. Return the final result.

### 4. Division-by-Zero Validation

The agent checks every divisor before performing a multi-number division.

Example:

`divide 100 by 5 and 0`

→ `I can't divide by zero`

## Architecture

```text
User Input
    ↓
Parser
    ↓
Structured Data
    ↓
Agent
    ↓
Validation + Decision + Orchestration
    ↓
Calculator
    ↓
Result