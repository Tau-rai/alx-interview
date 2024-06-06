# README

This document provides an overview of the lockbox concept and its implementation in Python. The main function, `canUnlockAll`, is used to determine if all boxes in a given list can be opened. Each box may contain keys to other boxes, and the unlocking process starts with box 0 being unlocked.

The `canUnlockAll` function utilizes a set to keep track of the opened boxes and a stack (implemented using LifoQueue) to manage the boxes that need to be processed. By iteratively opening boxes and adding new keys to the stack, the function checks if the total number of opened boxes matches the total number of boxes. If all boxes can be opened, the function returns True; otherwise, it returns False.

This approach ensures efficient handling of the unlocking process and takes into account various edge cases.

## Usage

To use the `canUnlockAll` function, follow these steps:

1. Import the function into your Python script or interactive session.
2. Create a list of boxes, where each box is represented by a list of keys.
3. Call the `canUnlockAll` function, passing in the list of boxes as an argument.
4. The function will return True if all boxes can be opened, and False otherwise.
