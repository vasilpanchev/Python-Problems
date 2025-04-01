employee_1 = int(input())
employee_2 = int(input())
employee_3 = int(input())
students_to_help = int(input())
productivity = employee_1 + employee_2 + employee_3
hours = 0
while students_to_help > 0:
    hours += 1
    if hours % 4 == 0:
        continue
    students_to_help -= productivity

print(f"Time needed: {hours}h.")
