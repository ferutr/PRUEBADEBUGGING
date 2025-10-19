def format_data(data):
    # Function to format data for display
    return str(data)

def validate_input(data):
    # Function to validate input data
    if data is None:
        raise ValueError("Input data cannot be None")
    return True

def log_message(message):
    # Function to log messages
    print(f"[LOG]: {message}")