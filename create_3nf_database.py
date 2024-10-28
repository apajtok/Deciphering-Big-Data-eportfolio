import sqlite3

def create_database():
    """Creates a SQLite database with tables in 3NF."""

    conn = sqlite3.connect('sample_data/student_exams_3nf.db')
    cursor = conn.cursor()

    # Create Students table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Students (
            StudentNumber INTEGER PRIMARY KEY,
            StudentName TEXT,
            DateOfBirth DATE
        )
    ''')

    # Create Courses table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Courses (
            CourseName TEXT PRIMARY KEY
        )
    ''')

    # Create Exams table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Exams (
            ExamID INTEGER PRIMARY KEY,
            StudentNumber INTEGER,
            CourseName TEXT,
            FOREIGN KEY (StudentNumber) REFERENCES Students(StudentNumber),
            FOREIGN KEY (CourseName) REFERENCES Courses(CourseName)
        )
    ''')

    # Create ExamBoards table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ExamBoards (
            BoardID INTEGER PRIMARY KEY,
            ExamBoardName TEXT
        )
    ''')

    # Create Teachers table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Teachers (
            TeacherID INTEGER PRIMARY KEY,
            TeacherName TEXT
        )
    ''')

    # Create CourseExams table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS CourseExams (
            CourseExamID INTEGER PRIMARY KEY,
            CourseName TEXT,
            ExamID INTEGER,
            BoardID INTEGER,
            FOREIGN KEY (CourseName) REFERENCES Courses(CourseName),
            FOREIGN KEY (ExamID) REFERENCES Exams(ExamID),
            FOREIGN KEY (BoardID) REFERENCES ExamBoards(BoardID)
        )
    ''')

    # Create CourseTeachers table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS CourseTeachers (
            CourseTeacherID INTEGER
