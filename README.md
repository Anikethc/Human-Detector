# Human-Detector

This Python program detects humans in a video file and saves the data to a CSV file.

## Introduction

What this program basically does is that it reads a video file for humans, makes a box around them, and saves the data to a CSV file.

This program was actually an assignment I had to do when I applied for a "Software Developer" job. So, I had to `create a model that detects whether a human is present or not and compute the results in a CSV file`.

So, the CSV file saves the timestamp and the human flag (whenever the program detects a human). A sample CSV row would be: `2021-08-23 18:28:28 FLAG`. This just says that, at that given time, the program detected a human.

## How to Use It?

### 1) Installation

You can go ahead and download the code and store the contents in one Directory itself. The directory can be anywhere on your system, it doesn't matter.

### 2) Downloading the Python Modules

You should download OpenCV, NumPy, and imutils. You can use the below commands:

`pip install opencv-python` <br/>
`pip install numpy` <br/>
`pip install imutils`
 
OpenCV is used to recognize the humans using it's built-in model. NumPy is used for the algorithms and imutils is used for image/frame processing.
 
### 3) Explanation of Code

The first thing it does is that it initializes cv2 and the detector.

The next 3 functions that follow it are for the **CSV** files. The first one checks if the CSV file is present. The second one creates a CSV file and the third one adds a flag. These functions are called in the `detect()` function.

In the `detect()` function, it processes the video and puts a box around each human and displays the 'human count' on the top-left. In this code, it also adds a FLAG in the CSV file for each human it detects.

In the `detectByVideo()` function, it reads the video and sends the data to the `detect()` for processing of the video.

Last, but not the least, it asks the user which video to play as there are 5 videos. You can just select either 1, 2, 3, 4, or 5 and it uses the respective video for processing.

### 4) Running the Program

To run the program, open command promt and go to the directory where the Python code is using the `cd` command. Then, use the following command to run the program `python Detector.py` or you can just run the code in whatever IDE you are using.

<img src="https://user-images.githubusercontent.com/50455489/169464167-9a018c93-f589-4f86-86f9-08fa085c09e7.png" width="650" height="300"/>
<img src="https://user-images.githubusercontent.com/50455489/169464226-f034f229-3659-4767-b46a-dc9f072d0703.PNG" width="650" height="300"/>

In the first image, you can see how the program works and counts the number of humans and in the second image, it gives you the timestamp as well as the human FLAG in the CSV file.

## Issues & Bugs

If you encounter any issues or bugs, you can visit the 'Issues' tab in my repository and create an issue. I will immediately look into it and resolve it as soon as possible.

## Any Doubts or Questions

If you have any doubts or questions, you are always free to ask me. I will be available on [Twitter](https://twitter.com/anikethchavare) and Discord (Aniketh#6387).

## Conclusion

I hope you liked my project. Thank you!
