
from csv import reader

def find_na_values(filename):
    """
    Reads the zipped CSV data, finds and counts NA values for each question.
    Args:
        filename (str): The path to the zipped CSV file.
    """
    na_count = {}
    with open(filename, 'r') as file:
        csv_reader = reader(file)
        header_row = next(csv_reader)  # Get the header row
        for row in csv_reader:
            zipped_data = zip(header_row, row)  # Zip header with data row
            for resp in zipped_data:
                question = resp[0].split(" ", 1)[1] if " " in resp[0] else resp[0]  # Get descriptive question part
                answer = resp[1]
                if answer.strip().upper() == 'NA':  # Case-insensitive check for "NA"
                    na_count[question] = na_count.get(question, 0) + 1
    
    # Print the results
    print("NA Value Counts:")
    for question, count in na_count.items():
        print(f"{question}: {count}")

if __name__ == "__main__":
    find_na_values('/content/mn_zipped.csv')

print("Code saved to /content/find_na_values.py")
