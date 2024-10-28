import sqlite3

def create_database():
    """Creates a SQLite database with tables in 3NF."""

    conn = sqlite3.connect('sample_data/student_exams_3nf_v2.db')  # New database file name
    cursor = conn.cursor()

    # Create Students table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Students (
            StudentNumber INTEGER PRIMARY KEY,
            StudentName TEXT,
            DateOfBirth DATE
        )
    ''')

    # ... (Rest of the CREATE TABLE statements for other tables: Courses, Exams, ExamBoards, Teachers, CourseExams, CourseTeachers, StudentCourses) ...

    conn.commit()
    conn.close()

    print("3NF Database (v2) and tables created successfully!")

if __name__ == "__main__":
    create_database()
