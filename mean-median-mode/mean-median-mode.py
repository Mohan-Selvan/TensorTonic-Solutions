from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    return {
        "mean": mean(x),
        "median": median(x),
        "mode": mode(x)
    }

def mean(x: list):
    return sum(x)/len(x)

def median(l: list):
    x = sorted(l)
    mid = len(x) // 2
    if len(x) % 2 == 0:
        return (x[mid-1]+x[mid])/2
    else:
        return float(x[mid])

def mode(x: list):
    counts = Counter(x)
    return float(max(counts, key=counts.get))

    