## Engineering Calculator CLI + Unit Tests

This project is a Python-based command-line engineering calculator that performs basic arithmetic and scientific operations including power, roots, and trigonometric functions (sine, cosine, tangent). It includes a complete unit test suite using Python’s unittest module to ensure reliability and correctness of calculations.

## Modules to Test

1. **Arithmetic operations**
   - Addition
   - Subtraction
   - Multiplication
   - Division (including division by zero handling)

2. **Scientific operations**
   - Power (exponentiation)
   - Root (square root, nth root)
   - Trigonometric functions: `sin`, `cos`, `tan` (with radians input)

## Unit Testing Strategy

- Use `unittest` module as recommended in Python documentation.
- Group tests by function (e.g., test arithmetic separately from trigonometric).
- Include both normal cases and edge cases (e.g., negative inputs, division by zero, invalid roots).
