#############################################
# List & Dict Comprehension Exercises - 1
#############################################

# Changing variable names in a dataset

# before:
# ['total', 'speeding', 'alcohol', 'not_distracted', 'no_previous', 'ins_premium', 'ins_losses', 'abbrev']

# after:
# ['TOTAL', 'SPEEDING', 'ALCOHOL', 'NOT_DISTRACTED', 'NO_PREVIOUS', 'INS_PREMIUM', 'INS_LOSSES', 'ABBREV']

import seaborn as sns

df = sns.load_dataset("car_crashes")
df.columns

for col in df.columns:
    print(col.upper())

A = []
for col in df.columns:
    A.append(col.upper())

df_columns = A

df = sns.load_dataset("car_crashes")
df_columns = [col.upper() for col in df.columns]
