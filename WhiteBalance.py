import numpy as np
import cv2
from skimage import img_as_float, img_as_ubyte

# Capture video from file
cap = cv2.VideoCapture(0)

while(True):

    ret, frame = cap.read()

    if ret == True:

        img = img_as_float(frame)

        r = img[:,:,0]
        g = img[:,:,1]
        b = img[:,:,2]

        avg_r = np.sum(r)/r.size
        avg_g = np.sum(g)/g.size
        avg_b = np.sum(b)/b.size

        avg = (avg_r + avg_g + avg_b) / 3

        rw = avg_r/avg
        gw = avg_g/avg
        bw = avg_b/avg

        r = r/rw
        g = g/gw
        b = b/bw

        img_combined = np.dstack((r, g, b))

        img = np.clip(img_combined, 0, 1.0)

        img = img_as_ubyte(img)

        cv2.imshow('original',frame)
        cv2.imshow('WhiteBalance',img)


        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    else:
        break

cap.release()
cv2.destroyAllWindows()
