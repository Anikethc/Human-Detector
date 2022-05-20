# Detect Humans in Video and Save to CSV

# Imports
import cv2
import numpy
import imutils
import csv
import os
from os.path import exists
import datetime

# Initialize the Detector
detector = cv2.HOGDescriptor()
detector.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# Check if File is Present
def checkCSV():
    isCSVPresent = exists('flags.csv')

    return isCSVPresent

# Add CSV File
def addCSV():
    with open('flags.csv', 'w') as csv_file:
        fieldNames = ['Timestamp', ' Flag']

        writer = csv.DictWriter(csv_file, fieldnames=fieldNames)

        writer.writeheader()

# Add Flag in CSV
def addFlag():
    flagList = [datetime.datetime.now(), ' FLAG']
    emptyList = ['']
    with open('flags.csv', 'a') as csv_file:
        writer_object = csv.writer(csv_file)
        writer_object.writerow(emptyList)

        writer_object.writerow(flagList)
        csv_file.close()

# Detect the Humans
def detect(frame):
    # Set the Box Coordinates & Styles
    bounding_box_cordinates, weights =  detector.detectMultiScale(frame, winStride = (4, 4), padding = (8, 8), scale = 1.03)
    
    # Detect How Many People Are There
    person = 1
    for x,y,w,h in bounding_box_cordinates:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
        cv2.putText(frame, f'Person {person}', (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 1)

        if (checkCSV() == False):
            addCSV()
        else:
            addFlag()

        person += 1

    # Text on the Output
    cv2.putText(frame, 'Status: Detecting ', (40,40), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255,0,0), 2)
    cv2.putText(frame, f'Total People: {person-1}', (40,70), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255,0,0), 2)

    # Show the Output
    cv2.imshow('output', frame)
    return frame

# Detect by Giving Video Path
def detectByVideo(path):
    # Initialize the Video
    video = cv2.VideoCapture(path)
    check, frame = video.read()

    # Check if Video is Null
    if check == False:
        print('Video Not Found. Please Enter a Valid Path.')
        return

    # Detect the Video And Send Data to detect() Function.
    while video.isOpened():
        check, frame =  video.read()
        if check:
            frame = imutils.resize(frame , width=min(800,frame.shape[1]))
            frame = detect(frame)
            
            key = cv2.waitKey(1)
            if key== ord('q'):
                break
        else:
            break
    
    # Destroy the Video
    video.release()
    cv2.destroyAllWindows()

# Ask User Which Video
print("Which video do you want to use? (1, 2, 3, 4, 5)?")
userChoice = input("Enter your number: ")

# Run the Detection
detectByVideo("Videos/" + str(userChoice) + ".mp4")