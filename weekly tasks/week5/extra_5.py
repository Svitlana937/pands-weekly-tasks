# Ask for the student's name
name = input("Enter student's name: ")

# List to store module and grade info
modules = []

# Collect module names and grades until the user presses Enter without typing a module
while True:
    module = input("Enter module name (or press Enter to stop): ")
    if not module:
        break  # Stop when input is empty
    grade = input(f"Enter grade for {module}: ")
    modules.append((module, grade))  # Store as a tuple for simplicity

# Print the student info
print("\nStudent Information:")
print(f"Name: {name}")
print("Modules and Grades:")
for module, grade in modules:
    print(f"  {module}: {grade}")
