student_name = input("Enter student's name: ")

modules = []

while True:
    module_name = input("Enter module name (or press Enter to stop): ")
    
    if module_name == "":  # Stop when a blank module name is entered
        break
    
    grade = input(f"Enter grade for {module_name}: ")  # Read grade
    modules.append({"module": module_name, "grade": grade})  # Store module and grade

student = {
    "name": student_name,
    "modules": modules
}

print("\nStudent Information:")
print(f"Name: {student['name']}")
print("Modules and Grades:")

for module in student["modules"]:
    print(f"  {module['module']}: {module['grade']}")