import sqlite3

connection = sqlite3.connect('college.db')
cursor = connection.cursor()

#user table
user_table = '''CREATE TABLE IF NOT EXISTS
user(user_id INTEGER AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100), username VARCHAR(30), userpass VARCHAR(32), userrole VARCHAR(50), status ENUM("Active", "Inactive"))'''

cursor.execute(user_table)

#student table
student_table = '''CREATE TABLE IF NOT EXISTS
student(student_id INTEGER AUTO_INCREMENT PRIMARY KEY, firstname VARCHAR(50), middlename VARCHAR(50), lastname VARCHAR(50), date_of_birth VARCHAR(50), residence VARCHAR(50), user_id FOREIGN KEY, course_id FOREIN KEY)'''

cursor.execute(student_table)

#course table
course_table = '''CREATE TABLE IF NOT EXISTS
course(course_id INTEGER AUTO_INCREMENT PRIMARY KEY, coursename VARCHAR(50), description VARCAHR(50))'''

cursor.execute(course_table)
