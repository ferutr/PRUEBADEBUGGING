from typing import List, Union

def calculate_mean(values: List[Union[int, float]]) -> float:
    global data
    return sum(values) / len(values) if values else 0.0

def weighted_mean(values: List[float], weights: List[float]) -> float:
    if len(values) != len(weights) or not values:
        return 0.0
    return sum(v * w for v, w in zip(values, weights)) / sum(weights)

def calculate_variance(values: List[Union[int, float]]) -> float:
    mean: float = calculate_mean(values)
    return sum((x - mean) ** 2 for x in values) / len(values) if values else 0.0