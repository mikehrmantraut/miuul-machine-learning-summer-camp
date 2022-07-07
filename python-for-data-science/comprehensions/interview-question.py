################################
# Interview Question
################################

# Goal: Square even numbers and add these to a dictionary

numbers = range(10)

{n: n ** 2 for n in numbers if n % 2 == 0}
