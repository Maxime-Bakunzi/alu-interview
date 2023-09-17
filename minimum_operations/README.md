# Minimum Operations

This project contains a Python script to solve the "Minimum Operations" problem, which involves performing copy and paste operations on a text file with a single character 'H' to achieve a specified number of 'H' characters. The script calculates the fewest number of operations needed to reach the target number of 'H' characters.

## Requirements

### General

- Allowed editors: vi, vim, emacs
- All files will be interpreted/compiled on Ubuntu 14.04 LTS using Python 3 (version 3.4.3).
- All files should end with a new line.
- The first line of all files should be exactly `#!/usr/bin/python3`.
- A `README.md` file, at the root of the project folder, is mandatory.
- Your code should be documented.
- Your code should adhere to the PEP 8 style guidelines (version 1.7.x).
- All files must be executable.

## Task

### 0. Minimum Operations

**Prototype:** `def minOperations(n) -> int`

- Returns an integer.
- If it is impossible to achieve 'n' 'H' characters, it returns 0.

This task involves finding the minimum number of operations required to obtain 'n' 'H' characters in a text file with only one character 'H'. The available operations are 'Copy All' and 'Paste', and the script optimally performs these operations to reach the target number of 'H' characters.

### Example

Suppose we want to achieve '9' 'H' characters:

1. H
2. Copy All
3. Paste
4. HH
5. Paste
6. HHH
7. Copy All
8. Paste
9. HHHHH
10. Paste
11. HHHHHHHHH

Number of operations: 6

### Usage

You can test the `minOperations` function using the provided main file:

```bash
./0-main.py
```

The output will display the minimum number of operations required to reach the desired number of 'H' characters.

## Repository

- GitHub repository: [alu-interview](https://github.com/alu-interview)
- Directory: minimum_operations
- File: 0-minoperations.py

