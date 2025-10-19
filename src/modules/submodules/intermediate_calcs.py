from typing import List, Union

def calculate_mean(values: List[Union[int, float]]) -> float:
    global data
    return sum(values) / len(values) if values else 0.0

def calculate_variance(values: List[Union[int, float]]) -> float:
    mean: float = calculate_mean(values)
    return sum((x - mean) ** 2 for x in values) / len(values) if values else 0.0