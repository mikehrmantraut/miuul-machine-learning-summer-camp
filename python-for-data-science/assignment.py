## Task 1: Examine the data structures of the given values. Use the Type() method.
x = 8
type(x)

y = 3.2
type(y)

z = 8j + 18
type(z)

a = "Hello World"
type(a)

b = True
type(b)

c = 23 < 22
type(c)

l = [1, 2, 3, 4]
type(l)

d  = {"Name": "Baran"}
type(d)

t = ("Machine", "Learning")
type(t)

s = {"Python", "Machine Learning"}
type(s)

## Task 2: Convert all letters of the given string expression to uppercase.
text = "The goal is to turn data into information, and information into insight."
text = text.upper()
text = text.replace(",", " ")
text = text.replace(".", " ")
text = text.split()

# or 
text = "The goal is to turn data into information, and information into insight."
text.upper().replace(","," ").replace(".", " ").split()


## Task 3 
lst = ["D", "A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]

#1
len(lst)

#2
lst[0]
lst[10]

#3
lst[:4]

#4
lst.pop(8)

#5
lst.append("X")

#6
lst.insert(8, "N")


## Task 4
dict = {'Christian': ["America", 18],
        'Daisy': ["England", 12],
        'Antonio': ["Spain", 22],
        'Dante': ["Italy", 25]}

# 1
dict.keys()

# 2
dict.values()

# 3
dict["Daisy"][1]

# 4
dict["Ahmet"] = ["Turkey", 24]

# 5
dict.pop('Antonio')

## Task 5 
l = [2, 13, 18, 93, 22]

def sep(lst):
    even_list = [i for i in lst if i % 2 == 0]
    odd_list = [j  for j in lst if j % 2 != 0]
    return even_list, odd_list

## Task 6
import seaborn as sns
df = sns.load_dataset("car_crashes")

["NUM_" + col.upper() if df[col].dtype != "O" else col.upper() for col in df.columns]

## Task 7
import seaborn as sns
df = sns.load_dataset("car_crashes")

[col.upper() + "_FLAG" if "no" not in col else col.upper() for col in df.columns]

## Task 8
import seaborn as sns
df = sns.load_dataset("car_crashes")

og_list = ["abbrev", "no_previous"]
new_cols = [col for col in df.columns if col not in og_list]
df = df[new_cols]
