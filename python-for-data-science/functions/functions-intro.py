## Functions
# Understanding built-in functions

print
"""
print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

Prints the values to a stream, or to sys.stdout by default. Optional keyword arguments:
file: a file-like object (stream); defaults to the current sys.stdout.
sep: string inserted between values, default a space.
end: string appended after the last value, default a newline.
flush: whether to forcibly flush the stream.
"""
print("a", "b")

print("a", "b", sep="__")

# function definition

def calculate(x):
    print(x*2)


calculate(5)


def summation(arg1, arg2):
    print(arg1 + arg2)


summation(7, 8)
summation(arg2=8, arg1=7)
