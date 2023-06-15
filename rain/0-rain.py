#!/usr/bin/python3
"""
Rain
"""


def rain(walls):
    """
    Calculates how many square units of water will be retained after it rains.

    Args:
        walls (list): A list of non-negative integers representing the heights of walls.

    Returns:
        int: The total amount of rainwater retained.
    """
    if not walls or len(walls) < 3:
        return 0

    water = 0

    for i in range(1, len(walls) - 1):
        left = walls[i]
        for j in range(i):
            left = max(left, walls[j])

        right = walls[i]
        for j in range(i + 1, len(walls)):
            right = max(right, walls[j])

        water += min(left, right) - walls[i]

    return water

