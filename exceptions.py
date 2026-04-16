
#! Divisor cannot divide by Zero.
def divide (divided, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be a 0.")
    return (divided/divisor)

grades = []
# grade = input("Enter grades: ")
try:
    average = divide(sum(grades), len(grades))
    print(f"the average grade is {average}")

except ZeroDivisionError:
    print("THere are no grades in your list yet.")
        
except ValueError:
    print("Please enter valid number.")
        
finally:
    print("End of calculations.")
        
students = [
{"name": "Bob", "grades": [80, 85]},
{"name": "Rolf", "grades": []},
{"name": "Jen", "grades": [90, 95]}
]
    
for student in students:
    try:
        average = divide(sum(student["grades"]), len(student["grades"]))
        print(student["name"], "average:", average)
    except ZeroDivisionError as e:
        print(f"There are no grades yet in {student["name"]}'s list", e)
    else:
        print("Processed successfully.")
    finally:
        print("Finished processing", student["name"])