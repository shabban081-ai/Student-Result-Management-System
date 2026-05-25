from tkinter import *
from tkinter import messagebox
import sqlite3

# DATABASE
conn = sqlite3.connect('student_result.db')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS students(
    roll INTEGER PRIMARY KEY,
    name TEXT,
    maths INTEGER,
    python INTEGER,
    coa INTEGER,
    total INTEGER,
    percentage REAL,
    grade TEXT
)
''')

conn.commit()


# FUNCTIONS

def calculate_grade(percentage):
    if percentage >= 90:
        return 'A+'
    elif percentage >= 75:
        return 'A'
    elif percentage >= 60:
        return 'B'
    elif percentage >= 40:
        return 'C'
    else:
        return 'Fail'



def add_result():
    try:
        roll = int(roll_entry.get())
        name = name_entry.get()

        maths = int(maths_entry.get())
        python_marks = int(python_entry.get())
        coa = int(coa_entry.get())

        total = maths + python_marks + coa
        percentage = (total / 300) * 100

        grade = calculate_grade(percentage)

        cur.execute('''
        INSERT INTO students
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (roll, name, maths, python_marks, coa,
              total, percentage, grade))

        conn.commit()

        result_text.set(
            f'Total: {total}\n'
            f'Percentage: {percentage:.2f}%\n'
            f'Grade: {grade}'
        )

        messagebox.showinfo('Success', 'Result Added Successfully')

    except Exception as e:
        messagebox.showerror('Error', str(e))



def search_result():
    try:
        roll = int(search_entry.get())

        cur.execute('SELECT * FROM students WHERE roll=?', (roll,))

        data = cur.fetchone()

        if data:
            output = f'''
Roll No: {data[0]}
Name: {data[1]}
Maths: {data[2]}
Python: {data[3]}
COA: {data[4]}
Total: {data[5]}
Percentage: {data[6]:.2f}%
Grade: {data[7]}
'''
            search_result_text.set(output)

        else:
            messagebox.showinfo('Not Found', 'Student Record Not Found')

    except Exception as e:
        messagebox.showerror('Error', str(e))


# GUI WINDOW
root = Tk()
root.title('Student Result Management System')
root.geometry('600x700')
root.config(bg='lightblue')

heading = Label(root,
                text='Student Result Management System',
                font=('Arial', 20, 'bold'),
                bg='lightblue')
heading.pack(pady=10)


# INPUT FRAME
frame = Frame(root, bg='lightblue')
frame.pack(pady=10)


Label(frame, text='Roll Number', bg='lightblue', font=('Arial', 12)).grid(row=0, column=0, pady=5)
roll_entry = Entry(frame, font=('Arial', 12))
roll_entry.grid(row=0, column=1)


Label(frame, text='Student Name', bg='lightblue', font=('Arial', 12)).grid(row=1, column=0, pady=5)
name_entry = Entry(frame, font=('Arial', 12))
name_entry.grid(row=1, column=1)


Label(frame, text='Maths Marks', bg='lightblue', font=('Arial', 12)).grid(row=2, column=0, pady=5)
maths_entry = Entry(frame, font=('Arial', 12))
maths_entry.grid(row=2, column=1)


Label(frame, text='Python Marks', bg='lightblue', font=('Arial', 12)).grid(row=3, column=0, pady=5)
python_entry = Entry(frame, font=('Arial', 12))
python_entry.grid(row=3, column=1)


Label(frame, text='COA Marks', bg='lightblue', font=('Arial', 12)).grid(row=4, column=0, pady=5)
coa_entry = Entry(frame, font=('Arial', 12))
coa_entry.grid(row=4, column=1)


Button(root,
       text='Add Result',
       command=add_result,
       font=('Arial', 12, 'bold'),
       bg='green',
       fg='white').pack(pady=10)


# RESULT DISPLAY
result_text = StringVar()

result_label = Label(root,
                     textvariable=result_text,
                     font=('Arial', 14),
                     bg='lightblue')
result_label.pack(pady=10)


# SEARCH SECTION
search_heading = Label(root,
                       text='Search Student Result',
                       font=('Arial', 16, 'bold'),
                       bg='lightblue')
search_heading.pack(pady=10)


search_frame = Frame(root, bg='lightblue')
search_frame.pack()


Label(search_frame,
      text='Enter Roll Number',
      bg='lightblue',
      font=('Arial', 12)).grid(row=0, column=0)

search_entry = Entry(search_frame, font=('Arial', 12))
search_entry.grid(row=0, column=1)


Button(root,
       text='Search Result',
       command=search_result,
       font=('Arial', 12, 'bold'),
       bg='blue',
       fg='white').pack(pady=10)


search_result_text = StringVar()

search_result_label = Label(root,
                            textvariable=search_result_text,
                            font=('Arial', 13),
                            bg='lightblue',
                            justify=LEFT)
search_result_label.pack(pady=10)


root.mainloop()