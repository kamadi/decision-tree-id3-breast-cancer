import math


def calculate_entropy(positive, negative):
    if positive == negative:
        return 1

    p_positive = positive / (positive + negative)

    p_negative = negative / (positive + negative)

    if p_positive > 0 and p_negative > 0:
        return - p_positive * math.log2(p_positive) - p_negative * math.log2(p_negative)

    return 0


def calculate_total_entropy(positive, negative, total):
    if total == 0:
        return 0
    return ((positive + negative) / total) * calculate_entropy(positive, negative)
