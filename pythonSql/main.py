import sqlite3
import os


def create_database():
    if os.path.exists("Students.db"):
        os.remove("Students.db")

    conn = sqlite3.connect("Students.db")
    cursor = conn.cursor()
    return conn, cursor


def create_tables(cursor):
    cursor.execute('''
    CREATE TABLE Students  (
        id INTEGER PRIMARY KEY,
        name VARCHAR NOT NULL,
        age INTEGER,
        email VARCHAR UNIQUE,
        city VARCHAR 
        )
    ''')

    cursor.execute('''
        CREATE TABLE Courses  (
            id INTEGER PRIMARY KEY,
            course_name VARCHAR NOT NULL,
            instructor TEXT,
            credits INTEGER 
            )
    ''')



def insert_sample_data(cursor):

    students = [
        (1, 'Alice Johnson', 20, 'alice@gmail.com', 'New York'),
        (2, 'Bob Smith', 19, 'bob@gmail.com', 'Chicago'),
        (3, 'Carol White', 21, 'carol@gmail.com', 'Boston'),
        (4, 'David Brown', 20, 'david@gmail.com', 'New York'),
        (5, 'Emma Davis', 22, 'emma@gmail.com', 'Seattle')
    ]

    cursor.executemany("INSERT INTO Students VALUES (?,?,?,?,?)", students)

    courses = [
        (1, 'Python Programming', 'Dr. Anderson', 3),
        (2, 'Web Development', 'Prof. Wilson', 4),
        (3, 'Data Science', 'Dr. Taylor', 3),
        (4, 'Mobile Apps', 'Prof. Garcia', 2)
    ]

    cursor.executemany("INSERT INTO Courses VALUES (?,?,?,?)", courses)

    print("Sample data inserted successfully")

def basic_sql_operations(cursor):
    #SELECT ALL
    print("--------------Select All ------------------")
    cursor.execute("SELECT * FROM Students")
    records = cursor.fetchall()
    for row in records:
        print(row)

    #SELECT Columns
    print("--------------Select Columns ------------------")
    cursor.execute("SELECT name , age FROM Students")
    records = cursor.fetchall()
    print(records)

    # WHERE clause
    print("--------------WHERE age = 20 ------------------")
    cursor.execute("SELECT * FROM Students WHERE age = 20")
    records = cursor.fetchall()
    print(records)

    #WHERE with string
    print("--------------WHERE city = 'New York' ------------------")
    cursor.execute("SELECT * FROM Students WHERE city = 'New York' ")
    records = cursor.fetchall()
    print(records)

    # ORDER BY
    print("--------------ORDER BY age ------------------")
    cursor.execute("SELECT * FROM Students ORDER BY age")
    records = cursor.fetchall()
    print(records)

    # LIMIT
    print("--------------LIMIT BY 3 ------------------")
    cursor.execute("SELECT * FROM Students LIMIT 3")
    records = cursor.fetchall()
    print(records)


def sql_update_delete_insert_operations(cursor, conn):

    #INSERT
    cursor.execute("INSERT INTO Students VALUES(6, 'Frank Miller', 23 , 'frank@gmail.com' , 'Miami' )")
    conn.commit()

    #UPDATE
    cursor.execute("UPDATE Students SET age = 24 WHERE id = 6 ")
    conn.commit()

    #DELETE
    cursor.execute("DELETE FROM Students WHERE id = 6 ")
    conn.commit()

def aggregate_functions(cursor):

    #COUNT
    print("-----------aggregate_functions_count------------------")
    cursor.execute("SELECT COUNT(*) FROM STUDENTS ")
    result = cursor.fetchone()
    print(result[0])

    #AVERAGE
    print("-----------aggregate_functions_average------------------")
    cursor.execute("SELECT AVG(age) FROM STUDENTS ")
    result = cursor.fetchone()
    print(result[0])

    # MAX - MİN
    print("-----------aggregate_functions_Max_Min------------------")
    cursor.execute("SELECT MAX(age) , MIN(age) FROM STUDENTS ")
    result = cursor.fetchall()
    print(result)

    # GROUP BY
    print("-----------aggregate_functions_Group_by------------------")
    cursor.execute("SELECT city, COUNT(*) FROM STUDENTS GROUP BY city")
    result = cursor.fetchall()
    print(result)



def questions():
    '''
    Basit
    1) Bütün kursların bilgilerini getirin
    2) Sadece eğitmenlerin ismini ve ders ismi bilgilerini getirin
    3) Sadece 21 yaşındaki öğrencileri getirin
    4) Sadece Chicago'da yaşayan öğrencileri getirin
    5) Sadece 'Dr. Anderson' tarafından verilen dersleri getirin
    6) Sadece ismi 'A' ile başlayan öğrencileri getirin
    7) Sadece 3 ve üzeri kredi olan dersleri getirin

    Detaylı
    1) Öğrencileri alphabetic şekilde dizerek getirin
    2) 20 yaşından büyük öğrencileri, ismine göre sıralayarak getirin
    3) Sadece 'New York' veya 'Chicago' da yaşayan öğrencileri getirin
    4) Sadece 'New York' ta yaşamayan öğrencileri getirin
    '''

print("------------------------------------------")
print("------------------------------------------")
print("------------------COURSES------------------")
print("------------------------------------------")
print("------------------------------------------")


def all_course(cursor):

    print("------------------------------------------")
    print("------------------------------------------")
    print("------------------HOMEWORK------------------")
    print("------------------------------------------")
    print("------------------------------------------")

    print("")

    print("-----------Select all Courses-----------")
    cursor.execute("SELECT * FROM courses")
    records = cursor.fetchall()
    for row in records:
        print(row)

def name_auth_instructor(cursor):

    print("------------SELECT NAME AND INSTRUCTOR----------------- ")
    cursor.execute("SELECT course_name , instructor FROM courses ")
    records = cursor.fetchall()
    print(records)

def age_21(cursor):
    print("---------- age = 21 --------------")
    cursor.execute("SELECT * FROM STUDENTS WHERE age = 21 ")
    records = cursor.fetchall()
    print(records)

def live_chicago(cursor):
    print("-----------LİVE İN CHİCAGO-------------------")
    cursor.execute("SELECT * FROM STUDENTS WHERE city = 'Chicago'")
    records = cursor.fetchall()
    print(records)

def dr_anderson(cursor):
    print("-------------ONLY DR ANDERSON----------------")
    cursor.execute("SELECT * FROM COURSES WHERE instructor = 'Dr. Anderson' ")
    records = cursor.fetchall()
    print(records)

def name_A(cursor):
    print("------------- NAME -A ----------------------")
    cursor.execute("SELECT * FROM STUDENTS WHERE name LIKE 'A%' ")
    records = cursor.fetchall()
    print(records)

def main():
    conn, cursor = create_database()

    try:
        create_tables(cursor)
        insert_sample_data(cursor)
        basic_sql_operations(cursor)
        sql_update_delete_insert_operations(cursor, conn)
        aggregate_functions(cursor)
        all_course(cursor)
        name_auth_instructor(cursor)
        age_21(cursor)
        live_chicago(cursor)
        dr_anderson(cursor)
        name_A(cursor)
        conn.commit()

    except sqlite3.Error as e:
        print(e)

    finally:
        conn.close()


if __name__ == "__main__":
    main()