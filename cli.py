import argparse
from models import Teacher, Student
from error import *
from pydantic import EmailStr, ValidationError

def main():
    # Create an ArgumentParser object to handle command-line arguments
    parser = argparse.ArgumentParser(description="CLI for Student data")

    # Define command-line arguments
    parser.add_argument('--teacher', action='store_true', help='Add a teacher')
    parser.add_argument('--student', action='store_true', help='Add a student')

    # Arguments specific to the teacher or student
    parser.add_argument('--email', type=EmailStr, help='Adding email')
    parser.add_argument('--subjects', type=str, help='Add Multiple subjects')
    parser.add_argument('--id', type=int, help='Adding Student ID')
    parser.add_argument('--age', type=int, help='Adding Student age')
    parser.add_argument('--name', type=str, help='Adding Student or teacher name')
    parser.add_argument('--address', type=str, help='Adding address of the student')
    parser.add_argument('--sex', choices=['male', 'female', 'other'], help='Adding gender of Student')

    # Parse the command-line arguments
    args = parser.parse_args()

    # Handle case when the --teacher argument is provided
    if args.teacher:
        try:
            # Create a Teacher object with the provided arguments
            teacher = Teacher(id=args.id, name=args.name, subjects=args.subjects)
            print(teacher)
        except ValueError as e:
            # Print error message if there is a ValueError
            print(e)

    # Handle case when the --student argument is provided
    if args.student:
        try:
            # Create a Student object with the provided arguments
            student = Student(
                id=args.id, 
                name=args.name, 
                email=args.email, 
                age=args.age, 
                address=args.address, 
                sex=args.sex
            )
            print(student)
        except (ValidationError, InvalidEmailError) as e:
            # Print error message if there is a ValidationError or InvalidEmailError
            print(e)

# Entry point of the script
if __name__ == "__main__":
    main()
