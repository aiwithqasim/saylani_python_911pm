# Function to read student records from the text file
def read_student_records(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            student_data = [line.strip().split(', ') for line in lines]
            return student_data
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        return None

# Function to calculate the average grade
def calculate_average_grade(student_data):
    total_grades = 0
    valid_students = 0
    for name, grade in student_data:
        try:
            grade = float(grade)
            total_grades += grade
            valid_students += 1
        except ValueError:
            print(f"Invalid grade for student '{name}'. Skipping...")

    if valid_students > 0:
        average_grade = total_grades / valid_students
        print(f"Average grade: {average_grade:.2f}")
    else:
        print("No valid grades found.")

# Main function
def main():
    file_name = 'student_records.txt'
    student_data = read_student_records(file_name)
    if student_data:
        calculate_average_grade(student_data)

if __name__ == "__main__":
    main()
