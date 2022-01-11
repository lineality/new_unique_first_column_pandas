import pandas as pd
import numpy as np

# load dataset
df = pd.read_csv("sm_salary6.csv")

# Create a new row containing row numbers:
df['Row_Number'] = np.arange(df.shape[0]) + 1

# Select new row to be moved to the front (made the first column)
new_first_column = df.pop('Row_Number')
  
# Move new row to the front (make it the first column)
df.insert(0, 'Row_Number', new_first_column)
