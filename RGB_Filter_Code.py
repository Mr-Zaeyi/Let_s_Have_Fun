import cv2
import numpy as np

# Create a VideoCapture object and read from input file
cap = cv2.VideoCapture('conveyorKapla1.mp4')

# Check if camera opened successfully
if (cap.isOpened() == False): 
    print("Error opening video stream or file")

# Read until video is completed
while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret == True:
        # Crop the frame
        croppedImg = frame[181:328, 185:622]
        
        # Apply red filter (keep red channel, zero out green and blue)
        filtered_img = croppedImg.copy()
        filtered_img[:, :, 0] = 0  # Set blue channel to 0
        filtered_img[:, :, 1] = 0  # Set green channel to 0
        # Red channel (index 2) remains unchanged
        
        # Display the resulting frame
        cv2.imshow('Original', croppedImg)
        cv2.imshow('Red Filter', filtered_img)
 
        # Press Q on keyboard to exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
 
    else: 
        break

# When everything done, release the video capture object
cap.release()
cv2.destroyAllWindows()