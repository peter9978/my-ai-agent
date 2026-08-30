## Current Version

**V1.3 — Input Validation & Error Handling**

The agent can currently:

* Perform addition, subtraction, multiplication, and division
* Parse natural-language mathematical requests
* Handle different relationships such as `and`, `by`, `from`, and `to`
* Recognize integers, decimals, and negative numbers
* Recognize English number words from zero to ten
* Handle uppercase and lowercase input
* Detect missing operations
* Detect missing numbers
* Prevent division by zero


## Version History

### V1
- Built basic calculator agent
- Supports addition, subtraction, multiplication, and division

### V1.1
- Built flexible natural-language parser
- Detects operations and relationships such as `and`, `from`, `by`, and `to`

### V1.2
- Added English number-word recognition
- Supports numbers from zero to ten and later extended to larger number words

### V1.3
- Added input validation
- Handles missing operations
- Handles missing numbers
- Prevents division by zero
- Prevents common parser crashes

### V1.4
- Added composed English number parsing
- Supports numbers such as:
  - `one hundred` → `100`
  - `three hundred fifty` → `350`
  - `one hundred twenty five` → `125`
- Added support for separating composed numbers around relationships such as `and`, `from`, `by`, and `to`

## Progress

Daily development notes are stored in the `progress/` directory.

Next milestone:

**V1.4 — Next agent capability**

## Current Version

**V1.4 — Advanced English Number Parser**

The agent can now understand numeric expressions written in both digit and basic English-number form and convert them into structured numbers before calculation.