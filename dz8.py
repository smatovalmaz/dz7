import sqlite3

with sqlite3.connect('person.db') as con:
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS Employees (
    EmployeeID INTEGER PRIMARY KEY ,
    FirstName TEXT,
    LastName TEXT,
    DepartmentID INTEGER,
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
    )''')

    cur.execute('''CREATE TABLE IF NOT EXISTS Departments (
    DepartmentID INTEGER PRIMARY KEY AUTOINCREMENT,
    DepartmentName TEXT,
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
    )''')


    cur.execute('''INSERT INTO Employees (EmployeeID, FirstName, LastName, DepartmentID) VALUES
        (1, 'John', 'Alibekov', 101),
        (2, 'Ilgiz', 'Alimov', 101),
        (3, 'Maksat', 'Tursunov', 102),
        (4, 'Emily', 'Li', 102),
        (5, 'David', 'Villa', 103),
        (6, 'Tomas', 'Miller', 103);
        ''')


    cur.execute('''INSERT INTO Departments (DepartmentID, DepartmentName) VALUES
        (101, 'HR'),
        (102, 'IT'),
        (103, 'Sales')
        ''')



    cur.execute('''select * from Employees''')
    for i in cur.fetchall():
        print(i)



    print('')


    cur.execute('''select * from Departments where DepartmentID=102''')
    for i in cur.fetchall():
        print(i)