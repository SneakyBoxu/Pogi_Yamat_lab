
# Task 3.1: Student Database


def add_student(db: dict, student_id: int, name: str, grade: str, major: str):
    """Adds a new student to the database dictionary.

    Args:
        db (dict): The student database.
        student_id (int): The unique ID of the student.
        name (str): The name of the student.
        grade (str): The student's grade (e.g., 'A').
        major (str): The student's major.
    """
    if student_id in db:
        print(f"Error: Student ID {student_id} already exists.")
        return
    db[student_id] = {'name': name, 'grade': grade, 'major': major}
    print(f"Added student {name} with ID {student_id}.")

def get_student_info(db: dict, student_id: int) -> dict | None:
    """Retrieves a student's information by their ID.

    Args:
        db (dict): The student database.
        student_id (int): The ID of the student to retrieve.

    Returns:
        dict | None: The student's data dictionary or None if not found.
    """
    return db.get(student_id)

def update_student_grade(db: dict, student_id: int, new_grade: str):
    """Updates the grade for a specific student.

    Args:
        db (dict): The student database.
        student_id (int): The ID of the student to update.
        new_grade (str): The new grade.
    """
    if student_id in db:
        db[student_id]['grade'] = new_grade
        print(f"Updated grade for student ID {student_id} to '{new_grade}'.")
    else:
        print(f"Error: Student ID {student_id} not found.")

def display_all_students(db: dict):
    """Displays all students and their information in the database.

    Args:
        db (dict): The student database.
    """
    print("\n--- Student Database ---")
    if not db:
        print("Database is empty.")
        return
    for student_id, info in db.items():
        print(f"ID: {student_id}, Name: {info['name']}, Grade: {info['grade']}, Major: {info['major']}")

def student_database_demo():
    """Demonstrates the full functionality of the dictionary-based student database."""
    print("--- Task 3.1: Student Database Demo ---")
    students_db = {}

    # Add sample students
    add_student(students_db, 101, 'Paul', 'A', 'Computer Science')
    add_student(students_db, 102, 'Carl', 'B', 'Information Technology')
    add_student(students_db, 103, 'Jen', 'A-', 'Data Science')

    # Display all students
    display_all_students(students_db)

    # Retrieve specific student information
    print("\nRetrieving info for student 102:")
    bob_info = get_student_info(students_db, 102)
    if bob_info:
        print(bob_info)

    # Update a student's grade
    update_student_grade(students_db, 102, 'B+')
    display_all_students(students_db)



# Task 3.2: Word Frequency Counter


def word_frequency_counter_demo():
    """Counts and displays the frequency of each word in a text."""
    print("\n--- Task 3.2: Word Frequency Counter ---")
    sample_text = "His palms are sweaty, knees weak, arms are heavy There's vomit on his sweater already, mom's spaghetti"
    print(f"Original Text: \"{sample_text}\"")

    # Pre-process text: lowercase and remove punctuation
    words = sample_text.lower().replace('.', '').replace(',', '').split()

    # Count word frequencies using a dictionary
    frequency_map = {}
    for word in words:
        frequency_map[word] = frequency_map.get(word, 0) + 1

    # Sort words by frequency in descending order
    sorted_words = sorted(frequency_map.items(), key=lambda item: item[1], reverse=True)

    print("\nWord Frequencies (sorted):")
    for word, count in sorted_words:
        print(f"'{word}': {count}")

    # Identify the most common word
    if sorted_words:
        most_common_word = sorted_words[0]
        print(f"\nMost common word: '{most_common_word[0]}' (appeared {most_common_word[1]} times)")



# Main execution block


if __name__ == "__main__":
    student_database_demo()
    word_frequency_counter_demo()