import numpy as np

def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """
    # Write code here
    sum = 0.0
    for idx, i in enumerate(x):
        sum += i * y[idx]
    return sum
    