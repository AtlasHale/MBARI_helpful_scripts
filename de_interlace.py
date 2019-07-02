import os
import cv2


frames = os.listdir('test/all_frames')
os.mkdir('/Users/chale/Desktop/test/reduced_frames/')
for frame in frames:
    img = cv2.imread('/Users/chale/Desktop/test/all_frames/'+frame)
    de_interlaced_img = img[::2, 1::2]
    cv2.imwrite('/Users/chale/Desktop/test/reduced_frames/'+frame, de_interlaced_img)