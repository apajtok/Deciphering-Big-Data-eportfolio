import sqlite3

def create_database():
    """Creates a SQLite database and tables for students, courses, and exams in 1NF."""

    conn = sqlite3.connect('sample_data/student_exams_1nf.db')
    cursor = conn.cursor()

    # Check if tables exist before creating them
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Students'")
    if not cursor.fetchone():
        cursor.execute('''
            CREATE TABLE Students (
                StudentNumber INTEGER PRIMARY KEY,
                StudentName TEXT,
                DateOfBirth DATE,
                Support TEXT
            )
        ''')

    # ... (Repeat the above check and creation for other tables: Courses, Exams, ExamBoards, Teachers, CourseTeacher) ...

