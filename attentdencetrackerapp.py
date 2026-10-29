import streamlit as st
import pymysql
from datetime import date

# ---------- Database Connection ----------
def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",       
        password="root",
        database="attendance_db6"
    )

# ---------- Add Student ----------
def add_student(name, roll_no):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO students (name, roll_no) VALUES (%s, %s)",
        (name, roll_no)
    )
    conn.commit()
    conn.close()

# ---------- Get Students ----------
def get_students():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM students")
    data = cursor.fetchall()
    conn.close()
    return data

# ---------- Mark Attendance ----------
def mark_attendance(student_id, status):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO attendance (student_id, date, status)
        VALUES (%s, %s, %s)
        ON DUPLICATE KEY UPDATE status=%s
        """,
        (student_id, date.today(), status, status)
    )
    conn.commit()
    conn.close()

# ---------- Fetch Attendance ----------
def get_attendance():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT s.name, a.date, a.status
        FROM attendance a
        JOIN students s ON a.student_id = s.id
        ORDER BY a.date DESC
    """)
    data = cursor.fetchall()
    conn.close()
    return data

# ---------- Streamlit UI ----------
st.title("📋 Simple Attendance Tracker")

menu = st.sidebar.selectbox(
    "Menu",
    ["Add Student", "Mark Attendance", "View Attendance"]
)

# ---------- Add Student UI ----------
if menu == "Add Student":
    st.subheader("➕ Add Student")
    name = st.text_input("Student Name")
    roll_no = st.text_input("Roll Number")

    if st.button("Add"):
        add_student(name, roll_no)
        st.success("Student added successfully!")

# ---------- Mark Attendance UI ----------
elif menu == "Mark Attendance":
    st.subheader("✅ Mark Attendance")

    students = get_students()
    student_dict = {name: sid for sid, name in students}

    selected_student = st.selectbox("Select Student", student_dict.keys())
    status = st.radio("Status", ["Present", "Absent"])

    if st.button("Submit"):
        mark_attendance(student_dict[selected_student], status)
        st.success("Attendance marked!")

# ---------- View Attendance UI ----------
elif menu == "View Attendance":
    st.subheader("📊 Attendance Records")
    records = get_attendance()

    for name, date_val, status in records:
        st.write(f"**{name}** | {date_val} | {status}")
