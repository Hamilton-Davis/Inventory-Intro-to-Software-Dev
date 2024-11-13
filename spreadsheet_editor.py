# This file will read thru an excel file
# find its location
# pull data from excel file to store here in program 
# Then write to a new excel spreadsheet
# this will add a whole bunch of new sheets as time goes on though....
# 


import glob
### Think we can use pandas to create a dataframe and store that way
## like in stats (CS2020) with R
import os

import pandas as pd

# this filepathing is catered to be inside the main branch (ie. outside of the inventory folder so it can navigate there)


# Get the current script directory
script_dir = os.path.dirname(os.path.realpath(__file__))

# Define the relative path to the Excel sheets folder
folderPath = os.path.join(script_dir, 'Inventory', 'Excel Sheets', '*')

# Function to find the most recent file in the folder
def getNewestFile(folderPath):
    # Use glob to get a list of all files matching the folder path
    files = glob.glob(folderPath)
    
    # Print the list of files for debugging
   # print("Files found:", files)
    
    # Ensure the list is not empty before applying max
    if files:
        newestfile = max(files, key=os.path.getctime)
      #  print("Most recent file:", newestfile)
    else:
        print("No files found in the specified folder.")
    return newestfile


inventoryList = pd.read_csv(getNewestFile(folderPath))

pass
print(inventoryList)



#ADDING NEW ITEMS TO FILE
# take new entries 
# Additional rows as a DataFrame
new_rows = pd.DataFrame({
    'Category': ['furniture', 'toy'],
    'Item Name': ['sofa', 'puzzle'],
    'Stock': [10, 30],
    'Number on Order': [15, 60],
    'Is Available': ['O', 'X']
})

# Concatenate
inventoryList = pd.concat([inventoryList, new_rows], ignore_index=True)

print(inventoryList)

#EDITING EXISTING ITEMS
# Update 'Stock' for the row where 'Item Name' is 'apples'
# this can be done for any specific item name
inventoryList.loc[inventoryList['Item Name'] == 'apples', 'Stock'] = 82

print(inventoryList)
