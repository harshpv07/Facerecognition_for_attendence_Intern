def time(name):
    import datetime
    x = str(datetime.datetime.now())
    date = (x.split(" ",)[0])
    time = (x.split(" ",)[1])
    import sqlite3
    conn = sqlite3.connect('logfile.db')
    print ("Opened database successfully")
    conn.execute("INSERT INTO logfile (NAME,DATE,INTIME,OUTTIME) VALUES (?,?,?,?)",(name,date,time,""));
    conn.commit()
    print("Records inserted Sucessfully")
    conn.close()
# if __name__ == '__main__':
#     time("harsh")
    

    