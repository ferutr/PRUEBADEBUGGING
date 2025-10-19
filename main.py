from typing import List
from src.modules.debug_utils import log_intermediate
from src.modules.submodules.variable_explorer import explore_variables
from src.modules.submodules.intermediate_calcs import calculate_mean, calculate_variance

def main() -> None:
    # Example data for exploration
    # data: Dict[str, int] = {
    data = {
        'a': 10,
        'b': 20,
        'c': 30,
    }
    
    # Log the initial variables
    log_intermediate("Initial data", data)

    # Explore the variables
    explore_variables(data)

    # Perform some calculations
    values: List[int] = [data['a'], data['b'], data['c']]
    
    # Convert to float list to match function signature
    float_values: List[float] = [float(v) for v in values]

    mean_value: float = calculate_mean(float_values)
    variance_value: float = calculate_variance(float_values)

    # Log the results
    log_intermediate("Calculation results", {'mean': mean_value, 'variance': variance_value})

if __name__ == "__main__":
    main()