def check(name,date):
    import sqlite3
    conn = sqlite3.connect('logfile.db')
    cursor = conn.execute("SELECT DATE,NAME from logfile")
    for row in cursor:
        if(row[0] == date and row[1] == name):
            return True

# if __name__ == '__main__':
#     check("harsh","2019-06-12")
    