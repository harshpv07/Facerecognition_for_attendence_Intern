def timeout(name):
    import datetime
    x = str(datetime.datetime.now())
    date = (x.split(" ",)[0])
    time = (x.split(" ",)[1])
    print(date)
    print(time)
    import sqlite3
    conn = sqlite3.connect('logfile.db')
    print ("Opened database successfully")
    conn.execute("UPDATE logfile SET OUTTIME = ? WHERE NAME = ? AND DATE = ?", (time,name,date))
    conn.commit()
    print("Updated Records Sucessfully")
    conn.close()
# if __name__ == '__main__':
#     timeout("harsh")
    
    