def findface():
    import face_recognition
    import cv2
    import numpy as np
    from logfile import timee
    import sqlite3
    conn = sqlite3.connect('logfile.db')
    print ("Opened database successfully")
    video_capture = cv2.VideoCapture(0)
    employee_face = []
    known_face_names = []
    encoding_names = {}
    counter = 0
    cursor = conn.execute("SELECT IMAGE,NAME from names")
    for row in cursor:
        # print ("IMAGE = ", row[0])
        # print ("NAME = ", row[1])
        employee_face.append(row[0])
        known_face_names.append(row[1])
        encoding_names[str(row[1]) + "_face_encoding"] = [face_recognition.face_encodings(face_recognition.load_image_file("Images/" + employee_face[counter]))[0]]
        counter = counter + 1
    known_face_encodings = []
    for keys,values in encoding_names.items():
        known_face_encodings.append(values)
    #print(known_face_encodings)
    #print(known_face_names)
    conn.close()

    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True

    while True:
        ret, frame = video_capture.read()
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]
        if process_this_frame:
            # Find all the faces and face encodings in the current frame of video
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"

                # # If a match was found in known_face_encodings, just use the first one.
                # if True in matches:
                #     first_match_index = matches.index(True)
                #     name = known_face_names[first_match_index]

                # Or instead, use the known face with the smallest distance to the new face
                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)

                if matches[best_match_index]:
                    name = known_face_names[best_match_index]

                face_names.append(name)

        process_this_frame = not process_this_frame


        # Display the results
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    time(name)
    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    findface()
    