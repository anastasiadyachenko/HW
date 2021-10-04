import sqlite3


def table_check():
    connection = sqlite3.connect('test.db')
    cursor = connection.cursor()
    ss = '''create table if not exists Phone
                        (ID integer primary key autoincrement,
                        FirstName varchar(100),
                        SecondName varchar(100),
                        PhoneNumber varchar(20))
                        '''
    cursor.execute(ss)
    connection.commit()
    connection.close()
    return


def insert_new_phone(firstname, secondname, phone):
    table_check()
    connection = sqlite3.connect('test.db')
    cursor = connection.cursor()
    ss = "insert into Phone(FirstName, SecondName, PhoneNumber) values('{0}', '{1}', '{2}')"
    sse = ss.format(firstname, secondname, phone)
    cursor.execute(sse)
    connection.commit()
    connection.close()
    return


def update_phone(id, phone):
    table_check()
    connection = sqlite3.connect('test.db')
    cursor = connection.cursor()
    ss = "update Phone set PhoneNumber = '{1}' where ID = {0}"
    sse = ss.format(id, phone)
    cursor.execute(sse)
    connection.commit()
    connection.close()
    return


def delete_phone(id):
    table_check()
    connection = sqlite3.connect('test.db')
    cursor = connection.cursor()
    ss = "delete from Phone where ID = {0}"
    sse = ss.format(id)
    cursor.execute(sse)
    connection.commit()
    connection.close()
    return


def print_phone(id):
    table_check()
    connection = sqlite3.connect('test.db')
    cursor = connection.cursor()
    ss = "select * from Phone where ID = '{0}'"
    sse = ss.format(id)
    cursor.execute(sse)
    for row in cursor.fetchall():
        print(row)
    connection.commit()
    connection.close()
    return


def print_all_phones():
    table_check()
    connection = sqlite3.connect('test.db')
    cursor = connection.cursor()
    ss = "select * from Phone"
    cursor.execute(ss)
    for row in cursor.fetchall():
        print(row)
    connection.commit()
    connection.close()
    return


