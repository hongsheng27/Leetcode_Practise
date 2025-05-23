## Brute force - O(n^3)

- Files: try1.py

- Compute the area of every possible rantangle in the historgram using two nested loops.
- for each pair (i, j), calculate the minimum height within heights[i:j] using min(heights[i:j])

## Problem

- min(heights[i:j]) takes O(j - i) time inside a double loop → total time complexity is O(n³).

- This approach is too slow for large inputs.

## Brute force 2 - Precomputed Minimums (O(n²) Time / O(n²) Space)

- Files: try2.py

## Problem

- Optimize the bottleneck by precomputing the minimum value in each range [i, j].
- Build a 2D table min_table[i][j] = min(heights[i:j+1]).
- Reduces time complexity from O(n³) to O(n²).
- Requires O(n²) space, which causes Memory Limit Exceeded (MLE) on large test cases in LeetCode.

## Brute force 3 - On-the-fly Minimum Tracking (O(n²) Time / O(1) Space)

- Files: try4.py

## Problem

- Further optimize space by eliminating the 2D table.
- Use a single variable min_val to track the current minimum height from i to j.
- Calculate area immediately within the inner loop.

- Benefits: Maintains O(n²) time complexity.

## Monotonic Stack – Optimal Solution (O(n) Time / O(n) Space)

- Files: 0084-largest-rectangle-in-histogram

## Problem

- The optimal solution uses a monotonic increasing stack to keep track of bar indices.

When a shorter bar is found, the stack is popped and areas are calculated.

Each bar can extend until a shorter bar is found to its left or right.
