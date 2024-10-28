
from csv import reader

def print_formatted_questions_answers(filename):
    """
    Reads the zipped CSV data, extracts questions and answers, 
    and prints them with formatted questions.
    Args:
        filename (str): The path to the zipped CSV file.
    """
    with open(filename, 'r') as file:
        csv_reader = reader(file)
        header_row = next(csv_reader)  # Get the header row
        for row in csv_reader:
            zipped_data = zip(header_row, row)  # Zip header with data row
            for item in zipped_data:
                if item[0] and item[1]:  # Check if both question and answer are present
                    # Format the question using the descriptive part (
