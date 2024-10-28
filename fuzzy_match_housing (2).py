
from fuzzywuzzy import fuzz
import pandas as pd

def find_column_fuzzy(df, target_column, threshold=80):
    """
    Finds a column in a DataFrame using fuzzy matching.
    Args:
        df (pd.DataFrame): The DataFrame to search.
        target_column (str): The target column name to find.
        threshold (int, optional): The similarity threshold for a match. Defaults to 80.
    Returns:
        str or None: The matched column name if found, otherwise None.
    """
    for column in df.columns:
        similarity = fuzz.ratio(target_column.lower(), column.lower())
        if similarity >= threshold:
            return column
    return None  # Return None if no match is found

if __name__ == "__main__":
    # Load the DataFrame
    df = pd.read_csv('/content/sample_data/california_housing_test.csv')

    # Find the column using fuzzy matching with "median age" as the target
    matched_column = find_column_fuzzy(df, target_column="median age")  

    # Print the result
    if matched_column:
        print(f"Found match: '{matched_column}'")
    else:
        print("No match found.")

print("Code saved to /content/fuzzy_match_housing.py")
