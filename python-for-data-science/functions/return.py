#############################
# Return
#############################

def calculate(warm, moisture, charge):
    print((warm + moisture) / charge)


#calculate(98, 12, 78)

def calculate(warm, moisture, charge):
    return (warm + moisture) / charge


calculate(98, 12, 78) * 10

def calculate(warm, moisture, charge):
    warm = warm * 2
    moisture = moisture * 2
    charge = charge * 2
    output = (warm + moisture) / charge

    return warm, moisture, charge, output

calculate(98, 12, 78)
