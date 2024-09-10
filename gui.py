import dearpygui.dearpygui as dpg
from models import Student, Teacher
from error import *
from pydantic import ValidationError
from random import randint

# Lists to store teacher and student objects
teachers = []
students = []

def submit_student(sender, data):
    # Retrieve values from the input fields
    name = dpg.get_value("##student_name")
    email = dpg.get_value("##student_email")
    age = dpg.get_value("##student_age")
    address = dpg.get_value("##student_address")
    sex = dpg.get_value("##student_gender")

    try:
        # Create a Student object and add it to the list
        student = Student(id=randint(1, 1000), name=name, email=email, age=int(age), address=address, sex=sex)
        students.append(student)
        update_student_list()  
        dpg.set_value("##student_error", "")  
        print(f"Student added: {student}")
    except (InvalidAgeError, InvalidNameError) as e:
        # Handle custom validation errors for student
        dpg.set_value("##student_error", str(e))
        print(f"Failed to add student: {e}")
    except ValidationError as e:
        # Handle Pydantic validation errors
        dpg.set_value("##student_error", str(e))
        print(f"Validation failed: {e}")

def submit_teacher(sender, data):
    # Retrieve values from the input fields
    name = dpg.get_value("##teacher_name")
    subjects = dpg.get_value("##teacher_subject")
    
    try:
        # Create a Teacher object and add it to the list
        teacher = Teacher(id=len(teachers) + 1, name=name, subjects=subjects)
        teachers.append(teacher)
        update_teacher_list() 
        dpg.set_value("##teacher_error", "")  
        print(f"Teacher added: {teacher}")
    except Exception as e:
        # Handle any general exceptions
        dpg.set_value("##teacher_error", str(e))
        print(f"Failed to add teacher: {e}")

def update_student_list():
    # Clear existing items in the student list display
    dpg.delete_item("##student_list", children_only=True)
    # Add each student to the display
    for student in students:
        dpg.add_text(f"ID: {student.id}, Name: {student.name}, Age: {student.age}, Address: {student.address}, Sex: {student.sex}", parent="##student_list")

def update_teacher_list():
    # Clear existing items in the teacher list display
    dpg.delete_item("##teacher_list", children_only=True)
    # Add each teacher to the display
    for teacher in teachers:
        dpg.add_text(f"ID: {teacher.id}, Name: {teacher.name}, Subjects: {teacher.subjects}", parent="##teacher_list")

def close_window(sender, data):
    # Close the DearPyGui window
    dpg.close_viewport()

def main():
    # Initialize DearPyGui context
    dpg.create_context()

    # Create the main window
    with dpg.window(label="Student and Teacher Management", width=1400, height=900):
        # Section for adding students
        dpg.add_text("Add Student")
        dpg.add_input_text(label="Name", tag="##student_name")
        dpg.add_input_int(label="Age", tag="##student_age")
        dpg.add_input_text(label="Email", tag="##student_email")
        dpg.add_input_text(label="Address", tag="##student_address")
        dpg.add_combo(label="Gender", items=["male", "female", "other"], tag="##student_gender")
        dpg.add_button(label="Submit Student", callback=submit_student)
        
        dpg.add_text("", tag="##student_error", color=(255, 0, 0))  

        dpg.add_separator()
        dpg.add_text("Students List")
        dpg.add_child_window(tag="##student_list", width=480, height=150) 

        dpg.add_spacing(count=10)  

        # Section for adding teachers
        dpg.add_text("Add Teacher")
        dpg.add_input_text(label="Name", tag="##teacher_name")
        dpg.add_input_text(label="Subjects", tag="##teacher_subject")
        dpg.add_button(label="Submit Teacher", callback=submit_teacher)

        dpg.add_text("", tag="##teacher_error", color=(255, 0, 0))  

        dpg.add_separator() 
        dpg.add_text("Teachers List")
        dpg.add_child_window(tag="##teacher_list", width=480, height=150)  

    # Set up and show the DearPyGui viewport
    dpg.create_viewport(title='Student and Teacher Management')
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()

# Entry point of the script
if __name__ == "__main__":
    main()

