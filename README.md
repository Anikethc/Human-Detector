# Human-Detector

This Python program detects humans in a video file and saves the data to a CSV file.

## Introduction

What this program basically does is that it reads a video file for humans, makes a box around them, and saves the data to a CSV file.

This program was actually an assignment I had to do when I applied for a "Software Developer" job. So, I had to `create a model that detects whether a human is present or not and compute the results in a CSV file`.

So, the CSV file saves the timestamp and the human flag (whenever the program detects a human). A sample CSV row would be: `2021-08-23 18:28:28 FLAG`. This just says that, at that given time, the program detected a human.

## How to Use It?

### Installation

You can go ahead and download the code and store the contents in one Directory itself. The directory can be anywhere on your system, it doesn't matter.

### Downloading the Python Modules

You should download OpenCV, NumPy, and imutils. You can use the below commands:

`pip install opencv-python` <br/>
`pip install numpy` <br/>
`pip install imutils`
 
OpenCV is used to recognize the humans using it's built-in model. NumPy is used for the algorithms and imutils is used for image/frame processing.
 
### Explanation of Code

The first thing it does is that it initializes cv2 and the detector.

The next 3 functions that follow it are for the **CSV** files. The first one checks if the CSV file is present. The second one creates a CSV file and the third one adds a flag. These functions are called in the `detect()` function.

In the `detect()` function, it processes the video and puts a box around each human and displays the 'human count' on the top-left. In this code, it also adds a FLAG in the CSV file for each human it detects.

In the `detectByVideo()` function, it reads the video and sends the data to the `detect()` for processing of the video.

Last, but not the least, it asks the user which video to play as there are 5 videos. You can just select either 1, 2, 3, 4, or 5 and it uses the respective video for processing.

## Issues & Bugs

If you encounter any issues or bugs, you can visit the 'Issues' tab in my repository and create an issue. I will immediately look into it and resolve it as soon as possible.

## Any Doubts or Questions

If you have any doubts or questions, you are always free to ask me. I will be available on [Twitter](https://twitter.com/anikethchavare) and Discord (Aniketh#6387).

## Conclusion

I hope you liked my project. Thank you!
