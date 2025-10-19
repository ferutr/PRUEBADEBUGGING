from typing import Any, Mapping, Sequence

def log_variable(var: Any) -> None:
    print(f"Logging variable: {var}")

def print_type(var: Any) -> None:
    print(f"Type of variable: {type(var)}")

def inspect_dict(d: Mapping[str, Any]) -> None:
    print("--- Inspecting Dictionary ---")
    for key, value in d.items():
        print(f"  Key: {key}, Value: {value}, Type: {type(value)}")
    print("---------------------------")

def inspect_list(lst: Sequence[Any]) -> None:
    print("--- Inspecting List ---")
    for i, item in enumerate(lst):
        print(f"  Index {i}: {item}, Type: {type(item)}")
    print("-----------------------")

def log_intermediate(name: str, value: Any) -> None:
    """
    Logs the name, value, and type of an intermediate variable for debugging.
    Using 'Any' for the value makes this function flexible for strict type checking.
    """
    print(f"DEBUG - {name}: {value} (Type: {type(value)})")

# def log_variables(variables):
#     for name, value in variables.items():
#         log_variable(name, value)

# def display_message(message):
#     print(f"DEBUG: {message}")