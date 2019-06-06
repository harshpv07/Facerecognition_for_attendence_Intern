def register_face():
    import cv2,os
    print(""" 
    -------------REGISTER YOUR FACE----------------

    Instructions :

    1. Enter your Full Name
    2. Look at the camera with your face in the frame and simulaneously press the spacebar

    """)
    name = str(input("Enter Your Name: "))
    cam = cv2.VideoCapture(0)

    cv2.namedWindow("test")

    img_counter = 0

    while True:
        ret, frame = cam.read()
        cv2.imshow("test", frame)
        if not ret:
            break
        k = cv2.waitKey(1)

        if k%256 == 32:
            # SPACE pressed
            print("\n\n\n")
            print("Confirm if your name and photo is correct Y/N ")
            print(name)
            y = input()
            if(y == "Y"):
                img_name = name+".jpg".format(img_counter)
                path = "Images/"
                cv2.imwrite(os.path.join(path,img_name), frame)
                print("{} written!".format(img_name))
                print("Face Sucessfully Registered")
                img_counter += 1
                break
            elif (y == "N"):
                newname = str(input("Enter the correct name :"))
                img_name = newname+".jpg".format(img_counter)
                path = "Images/"
                cv2.imwrite(os.path.join(path,img_name), frame)
                print("{} written!".format(img_name))
                print("Face Sucessfully Registered")
                img_counter += 1
                break

    cam.release()

    cv2.destroyAllWindows()


if __name__ == '__main__':
    register_face()
    