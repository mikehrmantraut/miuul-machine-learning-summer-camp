###############################
# Dictionary
###############################

# key-value pair
dictionary = {"REG": "Regression",
              "LOG": "Logistic Regression",
               "CART": "Classification and Reg"}

dictionary["REG"]
dictionary.get("REG")

dictionary = {"REG": ["RMSE", 10],
              "LOG": ["MSE", 20],
               "CART": ["SSE", 30]}

dictionary["REG"][1]

# querying key

"REG" in dictionary
"YSA" in dictionary

# changing value
dictionary["REG"] = ["YSA", 10]

# accessing all keys
dictionary.keys()

# accessing all values
dictionary.values()

# accessing all key-value pairs
dictionary.items()

# updating key-value 
dictionary.update({"REG": 11})
