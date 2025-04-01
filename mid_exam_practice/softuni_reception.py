from math import ceil

employee1 = int(input())
employee2 = int(input())
employee3 = int(input())
employees_to_answer = int(input())

employees_per_hour = employee1 + employee2 + employee3

sessions = ceil(employees_to_answer / employees_per_hour)
breaks_needed = (sessions - 1) // 3
time_needed = sessions + breaks_needed
print(f"Time needed: {time_needed}h.")
