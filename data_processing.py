
"""
Processes structured records and generates summary statistics.
"""

from statistics import mean, median
from collections import Counter


# Sample structured dataset: fictional student records
records = [
    {"id": "S101", "name": "Arun", "department": "Computer Science", "age": 20, "marks": 85},
    {"id": "S102", "name": "Priya", "department": "Data Science", "age": 21, "marks": 92},
    {"id": "S103", "name": "Rahul", "department": "AI", "age": 19, "marks": 76},
    {"id": "S104", "name": "Sneha", "department": "Computer Science", "age": 22, "marks": 68},
    {"id": "S105", "name": "Kiran", "department": "Data Science", "age": 20, "marks": 81},
    {"id": "S106", "name": "Ananya", "department": "Electronics", "age": 18, "marks": 95},
    {"id": "S107", "name": "Vikram", "department": "Computer Science", "age": 23, "marks": 74},
    {"id": "S108", "name": "Meera", "department": "AI", "age": 21, "marks": 88},
]


def display_records(data):
    """Display records in a readable table."""
    if not data:
        print("No records to display.")
        return

    print("-" * 82)
    print(f"{'ID':<8}{'Name':<12}{'Department':<23}{'Age':>8}{'Marks':>10}")
    print("-" * 82)

    for record in data:
        print(
            f"{record['id']:<8}"
            f"{record['name']:<12}"
            f"{record['department']:<23}"
            f"{record['age']:>8}"
            f"{record['marks']:>10}"
        )

    print("-" * 82)
    print(f"Total records: {len(data)}")


def calculate_statistics(data, field):
    """Calculate numerical summary statistics for a field."""
    values = [record[field] for record in data]

    if not values:
        return None

    return {
        "count": len(values),
        "total": sum(values),
        "average": mean(values),
        "median": median(values),
        "minimum": min(values),
        "maximum": max(values),
        "range": max(values) - min(values),
    }


def department_summary(data):
    """Count records in each department."""
    return Counter(record["department"] for record in data)


def find_top_students(data, limit=3):
    """Return the top students based on marks."""
    return sorted(
        data,
        key=lambda record: record["marks"],
        reverse=True
    )[:limit]


def print_statistics(title, stats):
    """Print numerical statistics."""
    print(f"\n{title}")
    print("-" * 40)

    for key, value in stats.items():
        if isinstance(value, float):
            print(f"{key.title():<12}: {value:.2f}")
        else:
            print(f"{key.title():<12}: {value}")


def main():
    print("=" * 55)
    print("          PYTHON DATA PROCESSING SYSTEM")
    print("=" * 55)

    # 1. Display original records
    print("\n1. ORIGINAL DATASET")
    display_records(records)

    # 2. Calculate marks statistics
    marks_stats = calculate_statistics(records, "marks")
    print_statistics("2. MARKS SUMMARY STATISTICS", marks_stats)

    # 3. Calculate age statistics
    age_stats = calculate_statistics(records, "age")
    print_statistics("3. AGE SUMMARY STATISTICS", age_stats)

    # 4. Count students by department
    print("\n4. DEPARTMENT SUMMARY")
    print("-" * 40)
    for department, count in sorted(department_summary(records).items()):
        print(f"{department:<25}: {count} student(s)")

    # 5. Display top three students
    print("\n5. TOP THREE STUDENTS BY MARKS")
    display_records(find_top_students(records, 3))

    # 6. Demonstrate processed records
    print("\n6. PROCESSED RECORDS: STUDENTS WITH MARKS >= 80")
    high_performers = [
        record for record in records
        if record["marks"] >= 80
    ]
    display_records(high_performers)

    # 7. Summary
    print("\n7. OVERALL SUMMARY")
    print("-" * 40)
    print(f"Total students       : {len(records)}")
    print(f"Average marks        : {marks_stats['average']:.2f}")
    print(f"Highest marks        : {marks_stats['maximum']}")
    print(f"Lowest marks         : {marks_stats['minimum']}")
    print(f"Students scoring >=80: {len(high_performers)}")

    print("\nData processing completed successfully.")


if __name__ == "__main__":
    main()
