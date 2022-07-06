#############################
# Local & Global Variables
#############################

# global scope
list_store = [1, 2]

def add_element(a, b):
    # local scope
    c = a * b
    list_store.append(c)
    print(list_store)

add_element(2, 3)
