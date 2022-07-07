##############################
# Interview Question - 2
##############################

# write a function called divide_students
# add students with even indexes to a list
# add students with odd indexes to another list
# return these two list as a single list

def divide_students(students):
    groups = [[], []]
    for i, student in enumerate(students):
        if i % 2 == 0:
            groups[0].append(student)
        else:
            groups[1].append(student)
    return groups

students = ["John", "Mark", "Venessa", "Mariam"]
divide_students(students)
        
