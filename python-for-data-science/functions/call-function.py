########################################
# Call a function inside a function
########################################

def calculate(warm, moisture, charge):
    return int((warm + moisture) / charge)


calculate(90, 12, 12) * 10

def standardization(a, p):
    return a * 10 / 100 * p* p


standardization(45, 1)

def all_calculation(warm, moisture, charge, p):
    a = calculate(warm, moisture, charge)
    b = standardization(a, p)
    print(b * 10)


all_calculation(1, 3, 5, 12)
