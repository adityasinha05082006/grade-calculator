# Name: Your Name
# Project: Student Grade Calculator
# Description: This program calculates student grades, comments, and class statistics.

def calculate_grade(avg):
    """Return grade and comment based on average"""
    if avg >= 90:
        return 'A', 'Excellent! 🔥'
    elif avg >= 80:
        return 'B', 'Very Good 👍'
    elif avg >= 70:
        return 'C', 'Good 🙂'
    elif avg >= 60:
        return 'D', 'Needs Improvement ⚠️'
    else:
        return 'F', 'Failed ❌'


def get_valid_number(prompt):
    """Input validation for marks"""
    while True:
        try:
            value = float(input(prompt))
            if 0 <= value <= 100:
                return value
            else:
                print("❌ Enter marks between 0-100")
        except ValueError:
            print("❌ Invalid input! Enter a number.")


def main():
    print("=" * 50)
    print("     STUDENT GRADE CALCULATOR")
    print("=" * 50)

    # Number of students
    while True:
        try:
            n = int(input("Enter number of students: "))
            if n > 0:
                break
            else:
                print("❌ Must be greater than 0")
        except ValueError:
            print("❌ Enter a valid number")

    students = []

    # Collect data
    for i in range(n):
        print(f"\n--- Student {i+1} ---")

        name = input("Enter name: ").strip()
        while name == "":
            print("❌ Name cannot be empty")
            name = input("Enter name: ").strip()

        m1 = get_valid_number("Math: ")
        m2 = get_valid_number("Science: ")
        m3 = get_valid_number("English: ")

        avg = (m1 + m2 + m3) / 3
        grade, comment = calculate_grade(avg)

        students.append({
            "name": name,
            "marks": [m1, m2, m3],
            "avg": avg,
            "grade": grade,
            "comment": comment
        })

    # Display results
    print("\n" + "=" * 60)
    print("              RESULTS")
    print("=" * 60)
    print(f"{'Name':<15} {'Avg':<6} {'Grade':<6} Comment")
    print("-" * 60)

    for s in students:
        print(f"{s['name']:<15} {s['avg']:<6.1f} {s['grade']:<6} {s['comment']}")

    # Statistics
    averages = [s['avg'] for s in students]
    class_avg = sum(averages) / len(averages)
    highest = max(averages)
    lowest = min(averages)

    high_student = students[averages.index(highest)]['name']
    low_student = students[averages.index(lowest)]['name']

    print("\n" + "=" * 60)
    print("          CLASS STATISTICS")
    print("=" * 60)
    print(f"Total Students : {n}")
    print(f"Class Average  : {class_avg:.1f}")
    print(f"Highest        : {highest:.1f} ({high_student})")
    print(f"Lowest         : {lowest:.1f} ({low_student})")

    print("\n✨ Program Finished Successfully!")


if __name__ == "__main__":
    main()