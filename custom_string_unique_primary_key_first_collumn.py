# import libraries
import pandas as pd
import numpy as np

# Select Names
csv_name_primary_key = "YOUR_FILE_NAME.csv"
custom_first_column_name = 'CUSTOM_FIRST_COLUMN'

# load csv
df = pd.read_csv( csv_name_primary_key )

##############################################
# Create Simple New First Column (Row Number)
##############################################

# custom_string is the csv_name_primary_key
custom_string = csv_name_primary_key[:-4] + "_"

# Create an initial simple new row containing row numbers:
df[ custom_first_column_name ] = np.arange(df.shape[0]) + 1

#######################################
# Add Custom Name to your first column
#######################################

# function to make a new name for each row
def make_new_name(old_name):
    return custom_string + str(old_name)

# use .apply() to change each first row name
df[ custom_first_column_name ] = df[ custom_first_column_name ].apply(make_new_name)

##################################################
# Move your new row to the front of the Dataframe
##################################################

# Select new row to be moved to the front (made the first column)
new_first_column = df.pop( custom_first_column_name )
  
# Move new row to the front (make it the first column)
df.insert(0,  custom_first_column_name , new_first_column)




# inspection
df.head()
