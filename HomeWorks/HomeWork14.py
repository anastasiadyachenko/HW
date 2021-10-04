import sqlite3
connection = sqlite3.connect('test.db')
cursor = connection.cursor()

sql = '''create table if not exists Person
                    (ID integer primary key autoincrement,
                    FirstName varchar(100),
                    SecondName varchar(100),
                    Age integer)
                    '''
cursor.execute(sql)

#sql = "insert into Person(FirstName, SecondName, Age) values('Smith', 'John', 25)"
#cursor.execute(sql)
connection.commit()

sql = 'select * from Person'
cursor.execute(sql)

rows = cursor.fetchall()
for row in rows:
    print(row)
connection.close()
