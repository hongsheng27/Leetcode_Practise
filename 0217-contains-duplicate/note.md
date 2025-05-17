## Brute Force
- doc: 1.py

- j = i + 1 avoids:
    - comparing the same element with itself.
    - rechecking already compared pairs (e.g. (i=1, j=3), (i = 3, j = 1))
- still too slow for large input

## Hash Set

- early return on firts duplicate
- check if the number already exists in the list before adding it.