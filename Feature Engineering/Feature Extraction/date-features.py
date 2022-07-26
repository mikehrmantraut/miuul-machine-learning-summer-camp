##############################
# Feature Extraction / Date Features
##############################
import pandas as pd
from datetime import date

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.float_format', lambda x: '%.3f' % x)
pd.set_option('display.width', 500)

dff = pd.read_csv("datasets/course_reviews.csv")
dff.head()
dff.info()

dff['Timestamp'] = pd.to_datetime(dff['Timestamp'], format="%Y-%m-%d")

# year
dff['year'] = dff["Timestamp"].dt.year

# month
dff['month'] = dff["Timestamp"].dt.month

# year difference
dff['year_diff'] = date.today().year - dff['Timestamp'].dt.year

# month difference
dff['month_diff'] = (date.today().year - dff["Timestamp"].dt.year) * 12 + date.today().month - dff["Timestamp"].dt.month

# day name
dff['day_name'] = dff['Timestamp'].dt.day_name()
