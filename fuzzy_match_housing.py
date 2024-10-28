
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
