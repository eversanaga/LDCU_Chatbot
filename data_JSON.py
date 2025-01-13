import json

def create_or_load_json(filename):
    """Load an existing JSON file or create a new dictionary."""
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            print(f"Loaded data from {filename}.")
    except FileNotFoundError:
        print(f"{filename} not found. Creating a new JSON file.")
        data = {}
    return data

def save_to_json(filename, data):
    """Save the current dictionary to a JSON file."""
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
    print(f"Data saved to {filename}.")

def add_key_value(data):
    """Add a key-value pair to the dictionary."""
    key = input("Enter the key: ")
    value = input("Enter the value: ")
    try:
        # Attempt to convert numeric inputs to int/float
        value = eval(value)
    except:
        pass  # Keep the input as a string if conversion fails
    data[key] = value
    print(f"Added {key}: {value}")

def navigate_or_add_nested_dict(data):
    """Navigate to an existing nested dictionary or create a new one."""
    key = input("Enter the key for the nested dictionary: ")
    if key in data:
        if isinstance(data[key], dict):
            print(f"Navigating to the existing nested dictionary at key '{key}'.")
        else:
            print(f"The key '{key}' exists but is not a dictionary. Overwriting it with a new dictionary.")
            data[key] = {}
    else:
        print(f"Creating a new nested dictionary at key '{key}'.")
        data[key] = {}
    return data[key]

def main():
    filename = input("Enter the JSON filename to work with: ")
    data = create_or_load_json(filename)

    current_dict = data
    navigation_stack = []

    while True:
        print("\nMenu:")
        print("1. Add key-value pair")
        print("2. Navigate to or add a nested dictionary")
        print("3. Go back to the parent dictionary")
        print("4. View current dictionary")
        print("5. Save and exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_key_value(current_dict)
        elif choice == '2':
            navigation_stack.append(current_dict)
            current_dict = navigate_or_add_nested_dict(current_dict)
        elif choice == '3':
            if navigation_stack:
                current_dict = navigation_stack.pop()
                print("Returned to the parent dictionary.")
            else:
                print("Already at the top-level dictionary.")
        elif choice == '4':
            print("\nCurrent Dictionary:")
            print(json.dumps(current_dict, indent=4))
        elif choice == '5':
            save_to_json(filename, data)
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
