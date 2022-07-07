#############################
# Interview Question
#############################

# Goal : We want to write a function that replaces the string as follows.

# before : "hi my name is john and i am learning python"
# after : "Hi mY NaMe iS JoHn aNd i aM LeArNiNg pYtHoN"

## My Solution
def change(string):
    a = list(string)
    str1 = ""
    for i in range(len(a)):
        if i%2==0:
            a[i] = a[i].capitalize()
    for j in a:
        str1 += j
    print(str1)

change("hi my name is john and i am learning python")

## Teacher's Solution
def alternating(string):
    new_string = ""
    for string_index in range(len(string)):
        if string_index % 2 == 0:
            new_string += string[string_index].upper()
        else:
            new_string += string[string_index].lower()
    print(new_string)
