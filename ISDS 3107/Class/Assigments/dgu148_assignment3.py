# Note: you must use python for loops for this assignment.
student_name = "Don Nguyen"

# List of vehicle milage
mpg = [18,21,20,21,16,18,18,18,16,20,19,15,17,17,15,15,17,16,14,11,14,13,12,16,15,16,15,15,14,11,11,14,19,22]

num_items = 0
sum_items = 0
avg_num = 0
smallest_num = mpg[0]
largest_num = mpg[0]

# Write your for loop and conditional logic here:
for n in mpg:
     sum_items = sum_items + n
     num_items = num_items + 1

     avg_num = sum_items / num_items

     if n < smallest_num:
         smallest_num = n

     if n > largest_num:
        largest_num = n



# Output the results
print("The number of items: ", num_items)
print("The sum of the items: ", sum_items)
print("The average of the items: ", avg_num)
print("The smallest number :", smallest_num)
print("The largest number :", largest_num)



# Dictiory of employees
employees = {123: 'Bob', 124: 'Susan', 128: 'Abby', 125: 'Henry', 126: 'Edward', 127: 'James'}

emp_numbers = []
emp_names = []

# Write your for loop here:
for key, value in employees.items():
    emp_numbers.append(key)

    emp_numbers = list(employees.keys())
    emp_names = list(employees.values())

# Output the results
print("List of employee numbers: ", emp_numbers)
print("List of employee names: ", emp_names)
