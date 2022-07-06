#############################
# Loops
#############################

# For Loop
students = ["John", "Mark", "Venessa", "Mariam"]

students[0]
students[1]
students[2]

for student in students:
    print(student)

for student in students:
    print(student.upper())


salaries = [1000, 2000, 3000, 4000, 5000]

for salary in salaries:
    print(salary)

for salary in salaries:
    print(salary * 20 / 100  + salary)

for salary in salaries:
    print(int(salary * 20 / 100  + salary))        

def new_salary(salary, rate):
    return int(salary * rate / 100 + salary)

new_salary(1500, 10)
