#############################################
# List & Dict Comprehension Exercises - 3
#############################################

# Goal: Creating a dictionary whose key values ​​are strings and whose values ​​are as follows
# Just for integer variables

# Output:
# {'total': ['mean', 'min', 'max', 'var'],
#  'speeding': ['mean', 'min', 'max', 'var'],
#  'alcohol': ['mean', 'min', 'max', 'var'],
#  'not_distracted': ['mean', 'min', 'max', 'var'],
#  'no_previous': ['mean', 'min', 'max', 'var'],
#  'ins_premium': ['mean', 'min', 'max', 'var'], 
#  'ins_losses': ['mean', 'min', 'max', 'var']}


import seaborn as sns

df = sns.load_dataset('car_crashes')

num_cols = [col for col in df.columns if df[col].dtype != "O"]

dictionary = {}
agg_list = ['mean', 'min', 'max', 'var']

for col in num_cols:
    dictionary[col] = agg_list

# short way
{col: agg_list for col in num_cols}

new_dict = {col: agg_list for col in num_cols}

df[num_cols].head()
# !! IMPORTANT
# **********************************
df[num_cols].agg(new_dict)
# **********************************
