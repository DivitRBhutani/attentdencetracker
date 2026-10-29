📋 Simple Attendance Tracker

A simple web-based Student Attendance Management System built using Python, Streamlit, and MySQL. This application allows users to add students, mark their daily attendance as Present or Absent, and view attendance records through an easy-to-use interface.

🚀 Features
Add Student: Add a student's name and roll number to the database.
Mark Attendance: Select a student and mark them as Present or Absent.
View Attendance: Display attendance records, including student names, dates, and attendance status.
MySQL Database: Store student details and attendance records persistently.
Duplicate Attendance Handling: Update the attendance status if a record already exists for the same student and date, provided the database has the required unique constraint.
Interactive UI: Navigate between features using the Streamlit sidebar.
🛠️ Technologies Used
Python – Application logic
Streamlit – Web-based user interface
MySQL – Database management
PyMySQL – Python library for connecting to MySQL
📁 Project Structure
text
Simple-Attendance-Tracker/
│
├── app.py              # Main Streamlit application
├── README.md           # Project documentation
└── requirements.txt    # Python dependencies (optional)

⚙️ Prerequisites

Make sure you have installed:

Python 3.9 or later
MySQL Server
pip (Python package installer)
📦 Installation and Setup
1. Clone the Repository
bash
git clone <your-repository-url>
cd Simple-Attendance-Tracker


Alternatively, download the project and open its folder in your terminal.

2. Install Dependencies
bash
pip install streamlit pymysql

3. Create the MySQL Database

Open MySQL and execute the following SQL commands:

sql
CREATE DATABASE attendance_db6;

USE attendance_db6;

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    roll_no VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE attendance (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    date DATE NOT NULL,
    status ENUM('Present', 'Absent') NOT NULL,
    FOREIGN KEY (student_id) REFERENCES students(id),
    UNIQUE KEY unique_student_date (student_id, date)
);


The unique constraint on student_id and date ensures that each student has only one attendance record per day. The application can then update the existing status using ON DUPLICATE KEY UPDATE.

4. Configure the Database Connection

In app.py, configure the MySQL connection settings:

python
def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="root",
        database="attendance_db6"
    )


Replace the username and password with your own MySQL credentials.

Security note: For a real deployment, store database credentials in environment variables or Streamlit secrets rather than hardcoding them in the source code.

5. Run the Application

Navigate to the project directory and run:

bash
streamlit run app.py


Streamlit will provide a local URL, usually:

text
http://localhost:8501


Open the URL in your browser to use the application.

📖 How to Use
1. Add Student
Select Add Student from the sidebar.
Enter the student's name.
Enter the student's roll number.
Click Add to save the student details.
2. Mark Attendance
Select Mark Attendance from the sidebar.
Choose a student from the dropdown list.
Select Present or Absent.
Click Submit to save the attendance record.
3. View Attendance
Select View Attendance from the sidebar.
View saved attendance records, including the student's name, attendance date, and status.
Records are displayed with the latest dates first.
🗄️ Database Tables
Students Table
Column	Description
id	Unique student ID
name	Student's name
roll_no	Student's roll number
Attendance Table
Column	Description
id	Unique attendance record ID
student_id	References the student
date	Date of attendance
status	Present or Absent
📋 Requirements File

You can create a requirements.txt file with the following contents:

text
streamlit
PyMySQL


Install all dependencies using:

bash
pip install -r requirements.txt

🔮 Future Enhancements
Search students by name or roll number.
Edit and delete student records.
Filter attendance by date or student.
Calculate student attendance percentages.
Export attendance reports to CSV or Excel.
Add authentication for administrators and teachers.
Improve error handling and input validation.
👨‍💻 Author

Developed as a Python-based student attendance management project using Streamlit and MySQL.

📄 License

This project is available for educational and learning purposes. Add a license file if you intend to distribute it under specific licensing terms.
