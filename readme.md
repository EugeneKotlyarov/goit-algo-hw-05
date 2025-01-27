# Performance Analysis of Substring Search Algorithms

## Overview
This document provides a comparison of three substring search algorithms—Boyer-Moore, Knuth-Morris-Pratt (KMP), and Rabin-Karp—evaluated on two text files for two types of substrings: one that exists in the text and one that does not.

The algorithms were measured using the `timeit` module to determine their execution times.

## Results

### Article 1
- **Boyer-Moore**:
  - Existing substring: 0.000090 seconds
  - Fabricated substring: 0.001896 seconds
- **Knuth-Morris-Pratt**:
  - Existing substring: 0.000243 seconds
  - Fabricated substring: 0.010746 seconds
- **Rabin-Karp**:
  - Existing substring: 0.000505 seconds
  - Fabricated substring: 0.021680 seconds

### Article 2
- **Boyer-Moore**:
  - Existing substring: 0.004831 seconds
  - Fabricated substring: 0.002806 seconds
- **Knuth-Morris-Pratt**:
  - Existing substring: 0.015427 seconds
  - Fabricated substring: 0.015265 seconds
- **Rabin-Karp**:
  - Existing substring: 0.030045 seconds
  - Fabricated substring: 0.029794 seconds

## Conclusions

### Per-Article Analysis
1. **Article 1**:
   - The fastest algorithm for the existing substring was **Boyer-Moore**.
   - The fastest algorithm for the fabricated substring was also **Boyer-Moore**.

2. **Article 2**:
   - The fastest algorithm for the existing substring was **Boyer-Moore**.
   - The fastest algorithm for the fabricated substring was **Boyer-Moore**.

### Overall Analysis
- **Boyer-Moore** consistently outperformed the other algorithms for both existing and fabricated substrings in both articles.
- **Knuth-Morris-Pratt** demonstrated moderate performance but was slower than Boyer-Moore.
- **Rabin-Karp** was the slowest algorithm across all tests, particularly for fabricated substrings.