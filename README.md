# File Protection Utility

## Description
This Python project protects file content by converting it into a protected format and restores it when required.

It demonstrates basic data protection concepts using Base64 encoding and decoding.

## Features
- Encode file content into a protected format
- Restore original content through decoding
- Simple and beginner-friendly
- Uses Python's built-in Base64 module

## Technologies Used
- Python 3
- Base64 Module

## How to Run

1. Open the project in VS Code.
2. Open the terminal.
3. Run:

```bash
py file_protection_utility.py
```

## Example

### Protect Content

Input:
Hello World

Output:
SGVsbG8gV29ybGQ=

### Restore Content

Input:
SGVsbG8gV29ybGQ=

Output:
Hello World

## Learning Outcome
This project introduces the concept of safeguarding data and controlled access through encoding and decoding techniques.
