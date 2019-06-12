def findface():
    import face_recognition
    import cv2
    import time
    import numpy as np
    from logfile import timee
    from Check import check
    from outtime import timeout
    import datetime
    x = str(datetime.datetime.now())
    date = (x.split(" ",)[0])
    video_capture = cv2.VideoCapture(0)
    employee_face = ["obama.jpg","harsh.jpg"]
    obama_image = face_recognition.load_image_file(employee_face[0])
    obama_face_encoding = face_recognition.face_encodings(obama_image)[0]
    harsh_image = face_recognition.load_image_file(employee_face[1])
    harsh_face_encoding = face_recognition.face_encodings(harsh_image)[0]
    known_face_encodings = [
        obama_face_encoding,
        harsh_face_encoding
    ]
    known_face_names = [
        "Barack Obama",
        "harsh"
    ]
    face = []
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
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
        # dict1 = {"harsh":"12421","raj":"84511","santosh":"45132"}
        # for key,values in dict1:
        #     if(key in name == [""])

        if(name != "Unknown"):
            timee(name)
            face.append(name)
            cv2.imshow('Video', frame)  
            cv2.waitKey(4000) 
            # if name in face:
            #     timeout(name)
            #     face.clear()
            # else:
                #check(name,date)
            
            # video_capture.release()
            # time.sleep(7)
            # video_capture = cv2.VideoCapture(0)

            # if(check(name,date) == True):
            #     timeout(name)
            
            exit()            
            break
            video_capture.release()
            cv2.destroyAllWindows()

    # start from here 
    # to recognise the face for timeout
    
    # import sqlite3
    # conn = sqlite3.connect('logfile.db')
    # cursor = conn.execute("SELECT DATE,NAME from names")
    # for row in cursor:
    #     if(row[0] == date and row[1] == name):
    #         timeout(name)

    
    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    findface()
    