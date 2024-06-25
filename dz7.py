import sqlite3

with sqlite3.connect('student.db') as con:
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    birth_year INTEGER,
    hobby TEXT,
    homework_score INTEGER
    )''')


    cur.execute('''INSERT INTO students(first_name, last_name, birth_year, hobby, homework_score) VALUES
    ('Mirbek', 'Atabekov', 1998, 'Reading', 8),
    ('Alice', 'Smith', 1999, 'Gaming', 12),
    ('Michael', 'Jordan', 1997, 'Swimming', 9),
    ('Leo', 'Messi', 2000, 'Painting', 15),
    ('James', 'Lebron', 1996, 'Cooking', 6),
    ('Sophia', 'Davis', 1998, 'Dancing', 11),
    ('Daniel', 'Alves', 1999, 'Programming', 7),
    ('Aigul', 'Bolotova', 2001, 'Writing', 10),
    ('Kairat', 'Nurtas', 1995, 'Photography', 13),
    ('Aijan', 'Aibekova', 1997, 'Music', 5)''')

    cur.execute('''select * from students''')
    for i in cur.fetchall():
        print(i)

#     cur.execute('''SELECT * FROM students WHERE LENGTH(last_name) > 10;
# ''')

#     cur.execute('''UPDATE students SET first_name = 'genius' WHERE homework_score > 10;
# ''')

#     cur.execute('''SELECT * FROM students WHERE first_name = 'genius';
# ''')

#     cur.execute('''DELETE FROM students WHERE id % 2 = 0;
# ''')



