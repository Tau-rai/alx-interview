# README

This README provides an overview of UTF-8 encoding, the basics of character encoding, and details about the `validUTF8` function that checks for valid UTF-8 encoding.

## UTF-8 Encoding

- **UTF-8 (Unicode Transformation Format 8-bit)**:
  - A character encoding standard representing Unicode characters using variable-length sequences of bytes.
  - Efficient storage of characters from various scripts and languages.
  - Characters are encoded using one to four bytes, depending on their Unicode code point.

## Character Encoding Basics

- **In UTF-8**:
  - **Single-byte characters** (ASCII characters) are represented using one byte (e.g., 'A' or '7').
  - **Multi-byte characters** (non-ASCII characters) use two to four bytes.
  - The first byte of a multi-byte character indicates its length and structure.

## Algorithm Overview

- **`validUTF8` Function**:
  - Checks if a given data set adheres to valid UTF-8 encoding rules.
  - Iterates through the data and verifies:
    - If the first byte starts with `0`, it's a single-byte character.
    - If the first byte starts with `110`, it's a two-byte character.
    - If the first byte starts with `1110`, it's a three-byte character.
    - If the first byte starts with `11110`, it's a four-byte character.
    - Subsequent bytes (if any) must start with `10`.

## Masking and Bitwise Operations

- **Bitwise Operations**:
  - Used to extract relevant bits from each byte.
  - Example: `num & 0b10000000` checks if the first bit of `num` is set.
  - Example: `num & 0b01000000` checks if the second bit is not set.

## Error Handling

- **Valid and Invalid Cases**:
  - If the data violates UTF-8 rules, the function returns `False`.
  - Otherwise, it returns `True`.

## Usage Example

To use the `validUTF8` function, pass your data as a list of integers representing byte values.

Example:
```python
data = [197, 130, 1]  # Represents the UTF-8 encoding for 'Ç' (U+00C7)
result = validUTF8(data)
print(f"Is valid UTF-8? {result}")
```
