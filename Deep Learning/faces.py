import cv2
import sys
import ddbb as ddbb
import numpy as np
 
def findFace(imagePath):
    cascPath = "/Users/Erik/Data/Programes/AILikeYou/ImageRecognition/FaceDetect-master/haarcascade_frontalface_default.xml"
    # Create the haar cascade
    faceCascade = cv2.CascadeClassifier(cascPath)
    
    # Read the image
    image = cv2.imread(imagePath)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags = cv2.CASCADE_SCALE_IMAGE
    )
    
    print("Found {0} faces!".format(len(faces)))
    
    padd = 10
    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x-padd, y-padd), (x+w+padd, y+h+padd), (0, 255, 0), 2)
    
    cv2.imshow("Faces found", image)
    cv2.waitKey(0)
    return
    

def countFaces(imagePath):
    cascPath = "/Users/Erik/Data/Programes/AILikeYou/ImageRecognition/FaceDetect-master/haarcascade_frontalface_default.xml"
    # Create the haar cascade
    faceCascade = cv2.CascadeClassifier(cascPath)
    
    # Read the image
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags = cv2.CASCADE_SCALE_IMAGE
    )

    return format(len(faces))

def detectFace(image):
    cascPath = "/Users/Erik/Data/Programes/AILikeYou/ImageRecognition/FaceDetect-master/haarcascade_frontalface_default.xml"
    # Create the haar cascade
    faceCascade = cv2.CascadeClassifier(cascPath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags = cv2.CASCADE_SCALE_IMAGE
    )
    return format(len(faces))

def cropFace(imagePath, x1, x2, y1, y2):
    img = cv2.imread(imagePath, 0)
    # cv2.imshow("normal", img)
    # cv2.waitKey(0)
    crop_img = img[y1:y2, x1:x2]
    crop_img = cv2.resize(crop_img,(250,250))
    # cv2.imshow("cropped", crop_img)
    # cv2.waitKey(0)
    return crop_img

def getData(nrows, field):
    query = "SELECT full_path, " + str(field) + " FROM Pictures LIMIT " + str(nrows)

def validFace(imagePath):
    try:
        image = cv2.imread(imagePath, 0)
        if image is None:
            return False
        height = np.size(image, 0)
        width = np.size(image, 1)
        if height > 1:
            return True
        if width > 1:
            return True
        return False
    except:
        return False