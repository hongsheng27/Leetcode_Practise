## Problem

- need a way to group anagrams like "act" and "cat" together, regardless of the order of the letters.

## Challenges

1. Dictionary Keys: Sets can't be used as dictionary keys because they are mutable, and tuple have an order problem(e.g., (1, 2, 3) is not the same as (3, 2, 1))
2. ASCLL combinations: using ASCLL codes to create keys might cause collisions for some combinations of letters.

## Solution:

- Letter Frequency: count how many times each letter appears in a word. if two words have the same letter frequency, they are anagrams and can be grouped together

## Optimized Approaach and Takeaway

1. use defaultdict(list): this simplifies adding word to groups without needing extra checks.
2. use list(res.values()): directly return the value of the dictionary, which are the anagram groups.
