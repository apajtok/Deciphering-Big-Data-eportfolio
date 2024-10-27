
# Your code here (paste the code from the previous response)
import pandas as pd

# Load the header file
headers_df = pd.read_csv('/content/mn_headers.csv')

# Create a dictionary mapping 'Name' to 'Label'
name_to_label = dict(zip(headers_df['Name'], headers_df['Label']))

# Load the data file
data_df = pd.read_csv('/content/mn.csv')

# Replace 'Name' values in the data file with corresponding 'Label' values
data_df.columns = data_df.columns.map(name_to_label.get)

# Save the updated data file to a new CSV file
data_df.to_csv('/content/mn_headers_updated.csv', index=False)

print("File saved to: /content/mn_headers_updated.csv")
