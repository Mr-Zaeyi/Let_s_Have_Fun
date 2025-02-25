# import cv2
# import numpy as np
 
# # Create a VideoCapture object and read from input file
# cap = cv2.VideoCapture('conveyorKapla1.mp4')
 
# # Check if camera opened successfully
# if (cap.isOpened()== False): 
#     print("Error opening video stream or file")
 
# # Read until video is completed
# while(cap.isOpened()):
#     # Capture frame-by-frame
#     ret, frame = cap.read()
#     if ret == True:
#         croppedImg = frame[200:800, 0:700]
#         # Get frame dimensions
#         height, width, channels = croppedImg.shape
#         # Apply red filter by setting green and blue channels to 0
#         for i in range(height):
#             for j in range(width):
#                 croppedImg[i,j,0] = 0  # Set blue channel to 0
#                 croppedImg[i,j,1] = 0  # Set green channel to 0
 
#         # Display the resulting frame with red filter
#         cv2.imshow('Red Filter', croppedImg)
 
#         # Press Q on keyboard to exit
#         if cv2.waitKey(25) & 0xFF == ord('q'):
#             break
 
#     # Break the loop
#     else: 
#         break
 
# # When everything done, release the video capture object
# cap.release()
 
# # Closes all the frames
# cv2.destroyAllWindows()

import cv2
import numpy as np

# Create a VideoCapture object and read from input file
cap = cv2.VideoCapture(0)

# Check if camera opened successfully
if (cap.isOpened()== False): 
    print("Error opening video stream or file")

# Liste pour stocker les positions du centre de l'objet bleu
trajectory_points = []

# Créer une image noire pour tracer la trajectoire complète
ret, first_frame = cap.read()
if ret:
    height, width = first_frame.shape[:2]
    trajectory_image = np.zeros((height, width, 3), dtype=np.uint8)

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        # Conversion en HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Définition de la plage de bleu
        lower_blue = np.array([110,50,50])
        upper_blue = np.array([130,255,255])

        # Création du masque bleu
        mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)

        # Réduction du bruit
        kernel = np.ones((5,5), np.uint8)
        mask_blue = cv2.erode(mask_blue, kernel, iterations=1)
        mask_blue = cv2.dilate(mask_blue, kernel, iterations=1)

        # Trouver les contours de l'objet bleu
        contours, _ = cv2.findContours(mask_blue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        # Pour l'objet bleu, calculer le centre de gravité
        if len(contours) > 0:
            # Prendre le plus grand contour
            c = max(contours, key=cv2.contourArea)
            
            # Calculer les moments
            M = cv2.moments(c)
            if M["m00"] != 0:
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
                
                # Ajouter le point à la trajectoire
                trajectory_points.append((cX, cY))
                
                # Dessiner le centre sur l'image originale
                cv2.circle(frame, (cX, cY), 5, (0, 255, 255), -1)
                
                # Dessiner la trajectoire sur l'image de trajectoire
                if len(trajectory_points) > 1:
                    cv2.line(trajectory_image,
                            trajectory_points[-2],
                            trajectory_points[-1],
                            (255, 0, 0), 2)

        # Combiner l'image originale avec la trajectoire
        combined = cv2.addWeighted(frame, 1, trajectory_image, 1, 0)

        # Afficher les résultats
        cv2.imshow('Tracking', combined)
        cv2.imshow('Blue mask', mask_blue)
 
        # Press Q on keyboard to exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else: 
        break

cap.release()
cv2.destroyAllWindows()