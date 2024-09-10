# Student_Teacher_Management

## Description
**Student_Teacher_Management** is a Python-based management system that allows users to manage student and teacher information via both a Command Line Interface (CLI) and a Graphical User Interface (GUI). This project uses Pydantic for data validation, custom exceptions for specific error handling, and DearPyGui for creating the GUI. It supports adding student and teacher details, validating inputs such as name, age, and email, and managing the data through lists displayed in the GUI.

## Features
- **Student Management**: Add student details such as name, email, age, address, and gender with validations.
- **Teacher Management**: Add teacher details like name and subjects taught.
- **Validation**: Uses Pydantic and custom exceptions for data validation (e.g., age must be 18 or older, name must be at least 3 characters).
- **CLI Support**: Add students and teachers via the command line.
- **GUI Support**: Add and display students and teachers in a graphical interface using DearPyGui.

## Project Structure
```bash
Student_Teacher_Management/
├── models.py         # Contains Student and Teacher classes with validation logic
├── error.py          # Custom exception classes for validation errors
├── cli.py            # CLI implementation for adding students and teachers
├── gui.py            # GUI implementation using DearPyGui
├── README.md         # Project documentation
└── requirements.txt  # Python dependencies
