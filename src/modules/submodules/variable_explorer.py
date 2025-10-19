from typing import Dict, Any

def explore_variables(data: Dict[str, Any]) -> None:
    for key, value in data.items():
        print(f"Exploring {key}: {value} (type: {type(value)})")