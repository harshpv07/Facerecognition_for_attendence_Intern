def motion():
        import numpy as np
        import cv2
        from facedetect import findface
        import sys
        import threading

        sdThresh = 10
        font = cv2.FONT_HERSHEY_SIMPLEX
        def distMap(frame1, frame2):
                frame1_32 = np.float32(frame1)
                frame2_32 = np.float32(frame2)
                diff32 = frame1_32 - frame2_32
                norm32 = np.sqrt(diff32[:,:,0]**2 + diff32[:,:,1]**2 + diff32[:,:,2]**2)/np.sqrt(255**2 + 255**2 + 255**2)
                dist = np.uint8(norm32*255)
                return dist
        cap = cv2.VideoCapture(0)

        _, frame1 = cap.read()
        _, frame2 = cap.read()

        facecount = 0
        while(True):
                _, frame3 = cap.read()
                rows, cols, _ = np.shape(frame3)
                #cv2.imshow('dist', frame3)
                dist = distMap(frame1, frame3)

                frame1 = frame2
                frame2 = frame3

                # apply Gaussian smoothing
                mod = cv2.GaussianBlur(dist, (9,9), 0)

                # apply thresholding
                _, thresh = cv2.threshold(mod, 100, 255, 0)

                # calculate st dev test
                _, stDev = cv2.meanStdDev(mod)

                #cv2.imshow('dist', mod)
                cv2.putText(frame2, "Standard Deviation - {}".format(round(stDev[0][0],0)), (70, 70), font, 1, (255, 0, 255), 1, cv2.LINE_AA)
                if stDev > sdThresh:
                        print("motion")
                        exit()
                else:
                        print("No Motion")

                #cv2.imshow('frame', frame2)
                if cv2.waitKey(1) & 0xFF == 27:
                        exit()
                        break

        cap.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':      
    motion()