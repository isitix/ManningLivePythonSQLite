import sqlite3

if __name__ == '__main__':
    conn = sqlite3.connect("datafile.db")
    cursor = conn.cursor()
    cursor.execute("drop table test")
    cursor.execute("create table test(id integer primary key, comment text)")
    cursor.execute("drop table people")
    cursor.execute("create table people (id integer primary key, name text, count integer)")
    cursor.execute("insert into people (name, count) values ('Bob', 1)")
    cursor.execute("insert into people (name, count) values (?, ?)",("Jill", 15))
    conn.commit()
    cursor.execute("insert into people (name, count) values (:username, \
    :usercount)", {"username": "Joe", "usercount": 10})
    result = cursor.execute("select * from people")
    print(result.fetchall())
    result = cursor.execute("select * from people where name like :name",{"name": "bob"})
    print(result.fetchall())
    cursor.execute("update people set count=? where name=?", (20, "Jill"))
    result = cursor.execute("select * from people")
    print(result.fetchall())
    cursor.execute("update people set count=? where name=?", (20, "Jill"))
    conn.commit()
    conn.close()