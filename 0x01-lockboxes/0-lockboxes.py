#!/usr/bin/python3
"""This module contains the canUnlockAll function"""


from queue import LifoQueue


def canUnlockAll(boxes):
    """
    Determines if all the boxes in the list can be unlocked.

    Args:
        boxes (list): A list of lists representing the lockboxes and their keys

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    """

    # Initialize variables
    n = len(boxes)  # Total number of boxes
    opened_boxes = set()  # Set to keep track of opened boxes
    to_open = LifoQueue()  # Stack to store boxes to be opened

    to_open.put(0)  # Start with the first box

    # Open the First Box
    while not to_open.empty():
        current_box = to_open.get()

        if current_box not in opened_boxes:
            opened_boxes.add(current_box)

            # Add keys from the current box to the stack/queue
            for key in boxes[current_box]:
                if key not in opened_boxes:
                    to_open.put(key)

    # Check if all boxes are opened
    return len(opened_boxes) == n
