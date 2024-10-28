
import os
import time

def automate_task():
    """Performs a simple automated task: creates a directory, lists files, waits, and prints a message."""
    
    # Create a directory (if it doesn't exist)
    directory_name = "my_automated_directory"
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)
        print(f"Directory '{directory_name}' created.")
    else:
        print(f"Directory '{directory_name}' already exists.")

    # List files in the current directory
    print("Files in the current directory:")
    for file in os.listdir():
        print(file)

    # Wait for 5 seconds
    print("Waiting for 5 seconds...")
    time.sleep(5)

    # Print a message
    print("Automated task completed!")

if __name__ == "__main__":
    automate_task()
