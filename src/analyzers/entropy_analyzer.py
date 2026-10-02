import math
from collections import Counter


def calculate_entropy(data):

    if not data:
        return 0

    counts = Counter(data)
    total = len(data)

    entropy = 0

    for count in counts.values():

        probability = count / total

        entropy -= probability * math.log2(probability)

    return entropy


def analyze_entropy(path):

    with open(path, "rb") as f:
        data = f.read()

    return calculate_entropy(data)