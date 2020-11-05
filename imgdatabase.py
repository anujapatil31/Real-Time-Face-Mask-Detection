# Program To Read video 
# and Extract Frames 
import cv2 
  
# Function to extract frames 
def FrameCapture(): 
      
    # Path to video file 
    cap = cv2.VideoCapture(0)
  
    # Used as counter variable 
    count = 0
  
    # checks whether frames were extracted 
    success = 1
  
    while success: 
  
        # vidObj object calls read 
        # function extract frames 
        success, image = cap.read() 
  
        # Saves the frames with frame-count 
        cv2.imwrite("frame%d.jpg" % count, image)
        cv2.imshow('frame', image)
  
        count += 1
        if cv2.waitKey(1) & 0xFF == ord('q'):
          break
# Driver Code 
if __name__ == '__main__': 
  
    # Calling the function 
    FrameCapture()