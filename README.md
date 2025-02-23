# Real_Object_Detection
--A real-time object tracker that can follow a specific object in a live webcam feed.

--This code is a real-time object tracking application using OpenCV. It allows the user to select an object in the first frame of a webcam feed and then tracks that object as it moves. Below is a step-by-step explanation of the code:

-Step 1: Initialize the Webcam
The program starts by initializing the webcam using OpenCV's cv2.VideoCapture(0). If the webcam cannot be opened, an error message is displayed, and the program exits.

-Step 2: Select the Object to Track
The first frame is captured from the webcam, and the user is prompted to select an object by drawing a bounding box. If no object is selected, the program exits with an error message.

-Step 3: Initialize the Tracker
The CSRT tracker is initialized using cv2.TrackerCSRT_create(). The tracker is then initialized with the first frame and the selected bounding box.

-Step 4: Tracking Loop
The program enters a loop to continuously read frames from the webcam. If a frame cannot be read, the webcam is reinitialized, and the program waits for 1 second before retrying.

-Step 5: Update the Tracker
The tracker updates its position based on the current frame. If tracking is successful, the bounding box is drawn on the frame, and the status is set to "Tracking...". If tracking fails for more than 5 consecutive frames, the status is set to "Lost tracking!", and the tracker is reinitialized with the last valid bounding box.

-Step 6: Display Status and Frame
The tracking status ("Tracking..." or "Lost tracking!") is displayed on the frame. The frame is then displayed in a window titled "Live Object Tracking".

Step 7: Exit on 'q' Key Press
The loop continues until the user presses the 'q' key, at which point the program exits.

Step 8: Release Resources
The webcam is released, and all OpenCV windows are closed.
