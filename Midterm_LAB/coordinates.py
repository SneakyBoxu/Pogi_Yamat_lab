import math
import re
from collections import Counter

# Task 2.1: Coordinate System with Tuples

def calculate_distance(p1: tuple[float, float], p2: tuple[float, float]) -> float:
    """Calculates the Euclidean distance between two points.

    Args:
        p1 (tuple): The first coordinate (x1, y1).
        p2 (tuple): The second coordinate (x2, y2).

    Returns:
        float: The distance between p1 and p2.
    """
    # Distance Formula: sqrt((x2 - x1)^2 + (y2 - y1)^2)
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

def find_midpoint(p1: tuple[float, float], p2: tuple[float, float]) -> tuple[float, float]:
    """Finds the midpoint between two points.

    Args:
        p1 (tuple): The first coordinate (x1, y1).
        p2 (tuple): The second coordinate (x2, y2).

    Returns:
        tuple: The midpoint coordinate (x, y).
    """
    # Midpoint Formula: ((x1 + x2)/2, (y1 + y2)/2)
    mid_x = (p1[0] + p2[0]) / 2
    mid_y = (p1[1] + p2[1]) / 2
    return (mid_x, mid_y)

def coordinate_system_demo():
    """Demonstrates tuple-based coordinate calculations and immutability."""
    print("--- Task 2.1: Coordinate System with Tuples ---")

    # Define points as tuples
    point_a = (1, 2)
    point_b = (4, 6)
    point_c = (-2, 5)

    # Create a tuple containing all points
    all_points = (point_a, point_b, point_c)
    print(f"Defined points: {all_points}")

    # Test distance and midpoint functions
    distance_ab = calculate_distance(point_a, point_b)
    midpoint_ab = find_midpoint(point_a, point_b)
    print(f"Distance between {point_a} and {point_b}: {distance_ab:.2f}")
    print(f"Midpoint of {point_a} and {point_b}: {midpoint_ab}")

    # Demonstrate tuple immutability
    print("\nAttempting to modify a tuple to demonstrate immutability...")
    try:
        point_a[0] = 10  # This will raise a TypeError
    except TypeError as e:
        print(f"Successfully caught expected error: {e}")
        print("This confirms that tuples are immutable.")



# Task 2.2: Unique Word Counter with Sets


def unique_word_counter_demo():
    """Analyzes text to find and count unique words using a set."""
    print("\n--- Task 2.2: Unique Word Counter with Sets ---")
    sample_text = "Python is a programming language. Python is easy to learn. Python is powerful."
    print(f"Original Text: \"{sample_text}\"")

    # Clean and split the text into words
    # Convert to lowercase and remove punctuation
    clean_text = re.sub(r'[^\w\s]', '', sample_text).lower()
    words = clean_text.split()

    # Create a set of unique words
    unique_words = set(words)

    # Count total and unique words
    total_word_count = len(words)
    unique_word_count = len(unique_words)

    # Find the most common words using collections.Counter
    word_counts = Counter(words)
    most_common = word_counts.most_common(3)

    # Display results
    print(f"Total words: {total_word_count}")
    print(f"Unique words: {unique_word_count}")
    print(f"Set of unique words: {unique_words}")
    print(f"Top 3 most common words: {most_common}")



# Main execution block


if __name__ == "__main__":
    coordinate_system_demo()
    unique_word_counter_demo()