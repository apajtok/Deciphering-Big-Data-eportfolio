
from csv import reader, writer

# Open the data and header files
with open('/content/mn.csv', 'r') as data_file, open('/content/mn_headers.csv', 'r') as header_file:
    data_reader = reader(data_file)
    header_reader = reader(header_file)

    # Get the header row 
    header_row = next(header_reader) 

    # Open a new file to write the zipped data
    with open('/content/mn_zipped.csv', 'w', newline='') as output_file:
        data_writer = writer(output_file)

        # Write the header row to the output file
        data_writer.writerow(header_row)

        # Zip and write the data rows
        for data_row in data_reader:
            zipped_row = zip(header_row, data_row)
            # Convert zipped row to a dictionary and get values in header order
            row_dict = dict(zipped_row)
            data_writer.writerow([row_dict.get(header, '') for header in header_row])

print("Code saved to /content/zip_csv_data.py")
