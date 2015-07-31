# heightdetector
		                        Height Detector: A Component of Energy Efficient Homes 
				               Research Location: University of Virginia
                                         Resources:  Python 2.7, OpenCV, Numpy, Matplotlib
                                            Erin Griffiths, Kyle Long, Kamin WHitehouse
                                       
Project Overview:  This project entails of determining the height of a person in .h264 video files recorded with raspberry pi’s. The purpose of determining the height of a person is linked to understanding who in a home used a certain amount of energy. In order to know how much energy one has used you need to identify who used what energy source. Determining a person height will allow for you to associate a person’s energy usage to their height. For example, the mom in a home is 5’6 and with deployed sensors data shows that a 5’6 person used 27% of the family’s water that month, you may conclude that mom was responsible for that energy usage. 

Steps (Write a python program to): 
-	Play Video (Every video is 24 hours long). (opencv, numpy)
-	Save images from the video where a person is in the video. (opencv, numpy)
-	Take the image with the person in it and set that up as a matrix (numpy, matplotlib)
-	Produce a universal formula using the coordinates from the image to determine the person’s height. 

Findings: A good way to determine the person’s height is to know the height of the top camera lense. Using the variable of the camera’s height to subtract that from the distance of top camera lense from the top of the person’s head will give one the person’s height. Say the top lense is 7 feet tall and the distance between the top lense to the person’s head in the optimal image is 2 feet, the person is 5 feet tall. 
Advice: 
-	Make sure all libraries and packages are installed correctly and are updated. You may want to use ffmpeg and gstreamer for OpenCV to properly. That is what I used. You may need to copy specific opencv files to your Python 27 folder. 
-	Use numpy to  represent the image. 

*These are all suggestions, use better, more efficient methods once discovered. 


