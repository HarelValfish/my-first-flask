def get_age() -> int:
    age = input("Enter your age: ")
    if not age.isdigit():
        raise ValueError(f"{age} has to be a number.")
    return int(age)

try:
    age = get_age()
    print("Your age is:", age)
    
except ValueError as e:
    print(f"Invalid input: {e}")