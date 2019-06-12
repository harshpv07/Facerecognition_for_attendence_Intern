def csv(username):
    import csv
    import sqlite3
    conn = sqlite3.connect("logfile.db")
    print("Sucessfully opened DB")
    count = 0
    cursor = conn.execute("SELECT ID,NAME,DATE,INTIME,OUTTIME from logfile  WHERE NAME = (?)",(username))
    for row in cursor:
        csvData = [[]]
        csvData[0].append([row[0],row[1],row[2],row[3],row[4]])
        count = count + 1
    with open('attendence.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(csvData)

    csvFile.close()
if __name__ == '__main__':
    csv("harsh")
    