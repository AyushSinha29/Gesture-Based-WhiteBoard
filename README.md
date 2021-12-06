# Gesture-Based-WhiteBoard

Link for [documentation](https://docs.google.com/document/d/1yWTFom6TQ0uTOndA1qIfjxuR_kluJBtdvQqelkGoJr8/edit?usp=sharing)

# Overview

Gesture based White Board is a Python scripted program that allows the user to draw on a Whiteboard using 4 available colors - Red , Green, Blue and Yellow, which can be interchangeably used by different hand gestures.

Here, color recognition and tracking is used to reach the goal. The color markings are recognized and the mask is created. This includes further steps in morphological manipulation of the generated mask. This is erosion and dilation. Erosion reduces the impurities present in the mask, and dilation further restores the eroded main mask. 

In this project, we created a whiteboard using OpenCV and Python. We use color recognition and segmentation techniques to draw shapes on the whiteboard. We have used MediaPipeHands to identify the various pre - defined hand gestures that will be used to change the color of the pointer or the brush of the whiteboard.

OpenCV (Open Source Computer Vision Library) is an open source computer vision and machine learning software library. OpenCV was built to provide a common infrastructure for computer vision applications and to accelerate the use of machine perception in the commercial products. Being a BSD-licensed product, OpenCV makes it easy for businesses to utilize and modify the code.
 
MediaPipeHands is a fidelity hand and finger tracking solution. Using Machine Learning (ML) to derive 21 3D landmarks of the hand from a single image. MediaPipe Hands uses an ML pipeline consisting of multiple models that work together. A palm detection model that works across images and returns a oriented hand bounding box. A landmark model of the hand that works in the cropped image area defined by the palm detector and returns the key points of a high fidelity 3D hand. 


# Project Prerequisites:

1. Python –  3.8.8 
2. OpenCV – 4.4
3. Numpy –  1.20.1
4. MediaPipe - 0.8.8.1



# Steps to develop virtual white board project using OpenCV and MediaPipe:

<br/>Import necessary packages.
<br/>Read frames from a webcam
<br/>Create the white board window
<br/>Detect the blue color
<br/>Draw on the white board
<br/>Change colors using hand gestures
<br/>Clear all the contents using virtual clear button
<br/>Press ‘x’ to quit the program


# References

https://opencv.org/

https://google.github.io/mediapipe/solutions/hands.html



# About the uploaded codes

1. int01.py - This script will open two separate windows, one for tracking the hand gestures and one for the white board.
2. int02.py - This script will open one window,  for tracking the hand gestures and same for the white board.
