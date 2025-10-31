import math


# Task 1.1: Student Grade Manager

def add_student(names: list, grades: list, name: str, grade: int):
    """Adds a student's name and grade to the respective lists.

    Args:
        names (list): The list of student names.
        grades (list): The list of student grades.
        name (str): The name of the student to add.
        grade (int): The grade of the student to add.
    """
    names.append(name)
    grades.append(grade)
    print(f"Added {name} with grade {grade}")

def calculate_average_grade(grades: list) -> float:
    """Calculates the average of a list of grades.

    Args:
        grades (list): A list of integer or float grades.

    Returns:
        float: The average grade, or 0.0 if the list is empty.
    """
    if not grades:
        return 0.0
    return sum(grades) / len(grades)

def find_highest_grade(grades: list) -> int | None:
    """Finds the highest grade in a list.

    Args:
        grades (list): A list of integer grades.

    Returns:
        int | None: The highest grade, or None if the list is empty.
    """
    if not grades:
        return None
    return max(grades)

def display_all_grades(names: list, grades: list):
    """Displays all students and their corresponding grades.

    Args:
        names (list): The list of student names.
        grades (list): The list of student grades.
    """
    print("\nStudent Grades:")
    for name, grade in zip(names, grades):
        print(f"{name}: {grade}")

def student_grade_manager_demo():
    """Demonstrates the full functionality of the Student Grade Manager."""
    print("--- Task 1.1: Student Grade Manager ---")
    student_names = []
    student_grades = []

    # Add sample students and grades
    add_student(student_names, student_grades, "Alice", 85)
    add_student(student_names, student_grades, "Bob", 92)
    add_student(student_names, student_grades, "Charlie", 78)

    # Display all students and grades
    display_all_grades(student_names, student_grades)

    # Calculate and display the average grade
    average = calculate_average_grade(student_grades)
    print(f"Average Grade: {average:.1f}")

    # Find and display the highest grade
    highest = find_highest_grade(student_grades)
    print(f"Highest Grade: {highest}")


# Task 1.2: List Operations Practice


def list_operations_demo():
    """Demonstrates various fundamental list operations."""
    print("\n--- Task 1.2: List Operations Practice ---")
    numbers = [5, 2, 8, 1, 9, 3]
    print(f"Original list: {numbers}")

    # Sort the list
    sorted_numbers = sorted(numbers)
    print(f"Sorted list: {sorted_numbers}")

    # Calculate the sum
    total_sum = sum(numbers)
    print(f"Sum of elements: {total_sum}")

    # Calculate the average
    average = sum(numbers) / len(numbers) if numbers else 0
    print(f"Average of elements: {average:.2f}")

    # Find maximum and minimum values
    max_val = max(numbers)
    min_val = min(numbers)
    print(f"Maximum value: {max_val}")
    print(f"Minimum value: {min_val}")

    # Find the list length
    length = len(numbers)
    print(f"Length of the list: {length}")



# Main execution block

if __name__ == "__main__":
    student_grade_manager_demo()
    list_operations_demo()