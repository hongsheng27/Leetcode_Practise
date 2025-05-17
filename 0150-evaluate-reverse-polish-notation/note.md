## Recursion

- Files: try1.py

- Start from the the end of the tokens list and apply recursion evaluate the expression.
- Step:

1. Pop the last element from tokens
2. if it's a nums, return it directly
3. if it's an ioeratir, recursively evaluate the next two values "left" and "right"

### Challanges

- The problem states: "The division between two integers always truncates toward zero.", which means I can not use A // B in Python, as it performs floor division(round down).
- Assign right first, then left, because the tokens are processed from the end.

## Stack
