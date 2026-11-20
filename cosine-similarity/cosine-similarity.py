import numpy as np
import math

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    mag_a = mag(a)
    mag_b = mag(b)

    return 0.0 if mag_a == 0 or mag_b == 0 else dot(a, b) / (mag_a*mag_b)

def dot(a: list, b: list):
    sum = 0.0
    for i, v in enumerate(a):
        sum += v * b[i]
    return sum

def mag(vec: list):
    d = 0.0
    for i, v in enumerate(vec):
        d += v*v
    return math.sqrt(d)