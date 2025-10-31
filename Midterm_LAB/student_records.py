import pickle


# Task 4.1: Student Records File System


def save_records_pickle(data: dict, filename: str):
    """Saves a data structure to a file using pickle.

    Args:
        data (dict): The student records to save.
        filename (str): The name of the file (e.g., 'students.pkl').
    """
    try:
        with open(filename, 'wb') as file:  # 'wb' for write binary
            pickle.dump(data, file)
        print(f"Successfully saved records to {filename}")
    except IOError as e:
        print(f"Error saving file {filename}: {e}")

def load_records_pickle(filename: str) -> dict | None:
    """Loads a data structure from a pickle file.

    Args:
        filename (str): The name of the file to load.

    Returns:
        dict | None: The loaded data, or None if an error occurs.
    """
    try:
        with open(filename, 'rb') as file:  # 'rb' for read binary
            data = pickle.load(file)
        print(f"Successfully loaded records from {filename}")
        return data
    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
        return None
    except (pickle.UnpicklingError, IOError) as e:
        print(f"Error loading file {filename}: {e}")
        return None

def export_records_text(data: dict, filename: str):
    """Exports student records to a human-readable text file.

    Args:
        data (dict): The student records to export.
        filename (str): The name of the text file (e.g., 'students.txt').
    """
    try:
        with open(filename, 'w') as file:
            file.write("--- Student Records ---\n")
            for student_id, info in data.items():
                file.write(f"ID: {student_id}\n")
                file.write(f"  Name: {info['name']}\n")
                file.write(f"  Grade: {info['grade']}\n")
                file.write(f"  Major: {info['major']}\n")
                file.write("-" * 20 + "\n")
        print(f"Successfully exported records to {filename}")
    except IOError as e:
        print(f"Error exporting to {filename}: {e}")

def student_records_demo():
    """Demonstrates saving, loading, and exporting student records."""
    print("--- Task 4.1: Student Records File System ---")
    
    # Create sample student data
    sample_data = {
        201: {'name': 'Dana', 'grade': 'A', 'major': 'Biology'},
        202: {'name': 'Eve', 'grade': 'C+', 'major': 'History'},
        203: {'name': 'Frank', 'grade': 'B', 'major': 'Chemistry'}
    }
    
    pickle_filename = 'students.pkl'
    text_filename = 'students.txt'
    
    # Test saving, loading, and exporting
    save_records_pickle(sample_data, pickle_filename)
    loaded_data = load_records_pickle(pickle_filename)
    
    if loaded_data:
        print("\nData loaded from pickle file:")
        print(loaded_data)
        export_records_text(loaded_data, text_filename)



# Task 4.2: File Operations Practice


def file_operations_demo():
    """Demonstrates writing, reading, and appending to a file."""
    print("\n--- Task 4.2: File Operations Practice ---")
    filename = "practice.txt"
    
    # 1. Writing to a new file ('w' mode)
    try:
        with open(filename, 'w') as f:
            f.write("This is the first line.\n")
            f.write("This is the second line.\n")
        print(f"Wrote initial content to {filename}.")
    except IOError as e:
        print(f"Error writing to file: {e}")

    # 2. Reading from a file ('r' mode)
    try:
        with open(filename, 'r') as f:
            content = f.read()
            print(f"\nContent of {filename}:\n---\n{content.strip()}\n---")
    except FileNotFoundError:
        print(f"Error: {filename} not found when trying to read.")
    except IOError as e:
        print(f"Error reading file: {e}")
        
    # 3. Appending to a file ('a' mode)
    try:
        with open(filename, 'a') as f:
            f.write("This line was appended.\n")
        print(f"Appended a new line to {filename}.")
    except IOError as e:
        print(f"Error appending to file: {e}")
        
    # 4. Reading again to show the appended content
    try:
        with open(filename, 'r') as f:
            content = f.read()
            print(f"\nFinal content of {filename}:\n---\n{content.strip()}\n---")
    except FileNotFoundError:
        print(f"Error: {filename} not found.")



# Main execution block


if __name__ == "__main__":
    student_records_demo()
    file_operations_demo()