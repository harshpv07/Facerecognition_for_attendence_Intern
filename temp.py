import threading
import sqlite3
conn = sqlite3.connect('logfile.db')
import face_recognition
print ("Opened database successfully")
employee_face = []
known_face_name = []
encoding_names = {}
counter = 0
cursor = conn.execute("SELECT IMAGE,NAME from names")
for row in cursor:
   # print ("IMAGE = ", row[0])
   # print ("NAME = ", row[1])
   employee_face.append(row[0])
   known_face_name.append(row[1])
   encoding_names[str(row[1]) + "_face_encoding"] = [face_recognition.face_encodings(face_recognition.load_image_file("Images/" + employee_face[counter]))[0]]
   counter = counter + 1

known_face_encodings = []
for keys,values in encoding_names.items():
       known_face_encodings.append(keys)
print ("Operation done successfully")
print(known_face_encodings)
# print(employee_face)
# print(known_face_name)
conn.close()

#str(row[1]) + "_face_encoding" = face_recognition.face_encodings(face_recognition.load_image_file(employee_face[0]))[0]
# encoding_names[str(row[1]) + "_face_encoding"] = [face_recognition.face_encodings(face_recognition.load_image_file(employee_face[0]))[0]]
# print(encoding_names)

 #obama