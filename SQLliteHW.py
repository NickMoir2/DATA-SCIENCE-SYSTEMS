import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

connection = sqlite3.connect('student_grades.db')
cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS grades')
cursor.execute('DROP TABLE IF EXISTS students')

cursor.execute('''
   CREATE TABLE IF NOT EXISTS students (
       student_id INTEGER PRIMARY KEY AUTOINCREMENT,
       first_name TEXT,
       last_name TEXT,
       UNIQUE(first_name, last_name)
   )
''')

cursor.execute('''
   CREATE TABLE IF NOT EXISTS grades (
       grade_id INTEGER PRIMARY KEY AUTOINCREMENT,
       student_id INTEGER,
       subject TEXT,
       grade INTEGER,
       UNIQUE(student_id, subject),
       FOREIGN KEY (student_id) REFERENCES students(student_id)
   )
''')

cursor.execute('''
   INSERT OR IGNORE INTO students(first_name, last_name)
   VALUES ("Alice", "Johnson")
''')
cursor.execute('''
   INSERT OR IGNORE INTO students(first_name, last_name)
   VALUES ("Bob", "Smith")
''')
cursor.execute('''
   INSERT OR IGNORE INTO students(first_name, last_name)
   VALUES ("Carol", "White")
''')
cursor.execute('''
   INSERT OR IGNORE INTO students(first_name, last_name)
   VALUES ("David", "Brown")
''')
cursor.execute('''
   INSERT OR IGNORE INTO students(first_name, last_name)
   VALUES ("Eve", "Davis")
''')

cursor.execute('''
   INSERT OR IGNORE INTO grades(student_id, subject, grade)
   VALUES (1, "Math", 95)
''')
cursor.execute('''
   INSERT OR IGNORE INTO grades(student_id, subject, grade)
   VALUES (1, "English", 88)
''')
cursor.execute('''
   INSERT OR IGNORE INTO grades(student_id, subject, grade)
   VALUES (1, "History", 90)
''')
cursor.execute('''
   INSERT OR IGNORE INTO grades(student_id, subject, grade)
   VALUES (2, "Math", 82)
''')
cursor.execute('''
   INSERT OR IGNORE INTO grades(student_id, subject, grade)
   VALUES (2, "English", 76)
''')
cursor.execute('''
   INSERT OR IGNORE INTO grades(student_id, subject, grade)
   VALUES (2, "History", 85)
''')
cursor.execute('''
   INSERT OR IGNORE INTO grades(student_id, subject, grade)
   VALUES (3, "Math", 89)
''')
cursor.execute('''
   INSERT OR IGNORE INTO grades(student_id, subject, grade)
   VALUES (3, "English", 92)
''')
cursor.execute('''
   INSERT OR IGNORE INTO grades(student_id, subject, grade)
   VALUES (3, "History", 94)
''')
cursor.execute('''
   INSERT OR IGNORE INTO grades(student_id, subject, grade)
   VALUES (4, "Math", 75)
''')
cursor.execute('''
   INSERT OR IGNORE INTO grades(student_id, subject, grade)
   VALUES (4, "English", 80)
''')
cursor.execute('''
   INSERT OR IGNORE INTO grades(student_id, subject, grade)
   VALUES (4, "History", 78)
''')
cursor.execute('''
   INSERT OR IGNORE INTO grades(student_id, subject, grade)
   VALUES (5, "Math", 93)
''')
cursor.execute('''
   INSERT OR IGNORE INTO grades(student_id, subject, grade)
   VALUES (5, "English", 87)
''')
cursor.execute('''
   INSERT OR IGNORE INTO grades(student_id, subject, grade)
   VALUES (5, "History", 91)
''')

cursor.execute('''
   SELECT students.first_name, students.last_name, grades.subject, grades.grade
   FROM students
   JOIN grades ON students.student_id = grades.student_id
''')

results = cursor.fetchall()
print("All Student Names and Grades:")
for row in results:
   print(row)

cursor.execute('''
   SELECT students.first_name, students.last_name, AVG(grades.grade) AS average_grade
   FROM students
   JOIN grades ON students.student_id = grades.student_id
   GROUP BY students.student_id
''')

results = cursor.fetchall()
print("Average Grade for Each Student: ")
for row in results:
   print(row)

cursor.execute('''
   SELECT students.first_name, students.last_name, AVG(grades.grade) AS average_grade
   FROM students
   JOIN grades ON students.student_id = grades.student_id
   GROUP BY students.student_id
   ORDER BY average_grade DESC
   LIMIT 1
''')

result = cursor.fetchone()
print("Student with Highest Average Grade: ")
print(result)

cursor.execute('''
   SELECT AVG(grade) AS average_math_grade
   FROM grades
   WHERE subject = "Math"
''')

result = cursor.fetchone()
print("Average Math Grade: ")
print(result)

cursor.execute('''
   SELECT DISTINCT students.first_name, students.last_name
   FROM students
   JOIN grades ON students.student_id = grades.student_id
   WHERE grades.grade > 90
''')

results = cursor.fetchall()
print("Students With at Least One 90%: ")
for row in results:
   print(row)

connection.commit()

students_df = pd.read_sql_query('SELECT * FROM students', connection)
grades_df = pd.read_sql_query('SELECT * FROM grades', connection)

print("Students DataFrame:\n", students_df)
print("\nGrades DataFrame:\n", grades_df)

combined_df = pd.read_sql_query('''
    SELECT students.first_name, students.last_name, grades.subject, grades.grade
    FROM students
    JOIN grades ON students.student_id = grades.student_id
''', connection)

print("\nCombined DataFrame:\n", combined_df)

average_grades_per_student = combined_df.groupby(['first_name', 'last_name'])['grade'].mean()

average_grades_per_student.plot(kind='bar', title='Average Grades Per Student', ylabel='Average Grade')
plt.tight_layout()
plt.show()

average_grades_per_subject = combined_df.groupby('subject')['grade'].mean()

average_grades_per_subject.plot(kind='bar', title='Average Grades Per Subject', ylabel='Average Grade', color='skyblue')
plt.tight_layout()
plt.show()

# EXTRA CREDIT SECTION BELOW

cursor.execute('''
    SELECT students.first_name, students.last_name, grades.subject, grades.grade
    FROM grades
    JOIN students ON grades.student_id = students.student_id
    WHERE (grades.subject, grades.grade) IN (
        SELECT subject, MAX(grade)
        FROM grades
        GROUP BY subject
    )
''')

results = cursor.fetchall()
print("Students with the highest grade in each subject:")
for row in results:
    print(row)

highest_grades_df = pd.DataFrame(results, columns=['first_name', 'last_name', 'subject', 'grade'])

print("\nDataFrame of Students with Highest Grade in Each Subject:")
print(highest_grades_df)

highest_grades_df['student'] = highest_grades_df['first_name'] + ' ' + highest_grades_df['last_name']
plt.figure(figsize=(10, 6))
sns.barplot(x='subject', y='grade', hue='student', data=highest_grades_df)
plt.title('Highest Grade by Student for Each Subject')
plt.ylabel('Grade')
plt.xlabel('Subject')
plt.legend(title='Student')
plt.tight_layout()
plt.show()

connection.close()
