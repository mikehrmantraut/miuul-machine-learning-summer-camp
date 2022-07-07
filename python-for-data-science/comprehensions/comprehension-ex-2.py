#############################################
# List & Dict Comprehension Exercices - 2
#############################################

# We want to add 'FLAG' to the beginning of the variables with 'INS' in the name and 'NO_FLAG' to the others

# before:

# ['TOTAL',
#  'SPEEDING',
#  'ALCOHOL', 
#  'NOT_DISTRACTED', 
#  'NO_PREVIOUS', 
#  'INS_PREMIUM',
#  'INS_LOSSES',
#  'ABBREV']

# after:

# ['NO_FLAG_TOTAL',
#  'NO_FLAG_SPEEDING',
#  'NO_FLAG_NO_DISTRACTED',
#  'NO_FLAG_NO_PREVIOUS',
#  'FLAG_INS_PREMIUM',
#  'FLAG_INS_LOSSES',
#  'NO_FLAG_ABBREV']

import seaborn as sns
df = sns.load_dataset('car_crashes')

[col for col in df.columns if "INS" in col]

["FLAG_" + col for col in df.columns if "INS" in  col]

["FLAG_" + col if "INS" in col else "NO_FLAG_" + col for col in df.columns]

df_columns = ["FLAG_" + col if "INS" in col else "NO_FLAG_" + col for col in df.columns]
