import cv2
import os
from deepdreamer import load_image


def CreateVideo(fileDirectory, fps, nameDream1, nameDream2, dreamsDirectory, mindChangeDirectory):

    imageOne = load_image(filename="{}{}/img_{}.jpg".format(dreamsDirectory, nameDream1, 0))
    width = len(imageOne[0])
    height = len(imageOne)

    fourCC = cv2.VideoWriter_fourcc(*"XVID")
    output = cv2.VideoWriter("{}{}_TO_{}.avi".format(fileDirectory, nameDream1, nameDream2)
                             , fourCC, fps, (width, height))
    processedFrame = 0

    while os.path.isfile("{}{}/img_{}.jpg".format(dreamsDirectory, nameDream1, processedFrame)):
        print("{}{}/img_{}.jpg".format(dreamsDirectory, nameDream1, processedFrame))
        if "img_0.jpg" in "{}{}/img_{}.jpg".format(dreamsDirectory, nameDream1, processedFrame):
            for i in range(0, fps):
                output.write(cv2.imread("{}{}/img_{}.jpg".format(dreamsDirectory, nameDream1, processedFrame)))
        output.write(cv2.imread("{}{}/img_{}.jpg".format(dreamsDirectory, nameDream1, processedFrame)))
        processedFrame += 1

    mindChangeFrame = 1
    while os.path.isfile("{}{}/img_{}.jpg".format(mindChangeDirectory, "{}_TO_{}".format(nameDream1, nameDream2), mindChangeFrame + 1)):
        print("{}{}/img_{}.jpg".format(mindChangeDirectory, "{}_TO_{}".format(nameDream1, nameDream2), mindChangeFrame + 1))
        output.write(cv2.imread("{}{}/img_{}.jpg".format(mindChangeDirectory, "{}_TO_{}".format(nameDream1, nameDream2), mindChangeFrame)))
        mindChangeFrame += 1

    while os.path.isfile("{}{}/img_{}.jpg".format(dreamsDirectory, nameDream2, processedFrame - 1)):
        print("{}{}/img_{}.jpg".format(dreamsDirectory, nameDream2, processedFrame - 1))
        if "img_0.jpg" in "{}{}/img_{}.jpg".format(dreamsDirectory, nameDream2, processedFrame - 1):
            for i in range(0, fps):
                output.write(cv2.imread("{}{}/img_{}.jpg".format(dreamsDirectory, nameDream2, processedFrame - 1)))
        output.write(cv2.imread("{}{}/img_{}.jpg".format(dreamsDirectory, nameDream2, processedFrame - 1)))
        processedFrame -= 1

    output.release()
