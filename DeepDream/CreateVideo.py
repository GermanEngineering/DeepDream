import cv2
import os
from deepdreamer import load_image


def CreateVideo(fileDirectory, fps, nameDream1, nameDream2, dreamsDirectory, blendDirectory):

    # Get first image.
    imageOne = load_image(filename="{}{}/img_{}.jpg".format(dreamsDirectory, nameDream1, 0))
    width = len(imageOne[0])
    height = len(imageOne)

    # Define output properties.
    fourCC = cv2.VideoWriter_fourcc(*"XVID")
    output = cv2.VideoWriter("{}{}_TO_{}.avi".format(fileDirectory, nameDream1, nameDream2)
                             , fourCC, fps, (width, height))

    processedFrame = 0

    # Add images of first dream to video.
    while os.path.isfile("{}{}/img_{}.jpg".format(dreamsDirectory, nameDream1, processedFrame)):
        print("{}{}/img_{}.jpg".format(dreamsDirectory, nameDream1, processedFrame))
        # Show initial image for 2 seconds.
        if "img_0.jpg" in "{}{}/img_{}.jpg".format(dreamsDirectory, nameDream1, processedFrame):
            for i in range(0, 2 * fps):
                output.write(cv2.imread("{}{}/img_{}.jpg".format(dreamsDirectory, nameDream1, processedFrame)))
        output.write(cv2.imread("{}{}/img_{}.jpg".format(dreamsDirectory, nameDream1, processedFrame)))
        processedFrame += 1

    # Add blend images to video.
    blendFrame = 1
    while os.path.isfile("{}{}/img_{}.jpg".format(blendDirectory, "{}_TO_{}".format(nameDream1, nameDream2), blendFrame + 1)):
        print("{}{}/img_{}.jpg".format(blendDirectory, "{}_TO_{}".format(nameDream1, nameDream2), blendFrame + 1))
        output.write(cv2.imread("{}{}/img_{}.jpg".format(blendDirectory, "{}_TO_{}".format(nameDream1, nameDream2), blendFrame)))
        blendFrame += 1

    # Add images of seconf dream to video.
    while os.path.isfile("{}{}/img_{}.jpg".format(dreamsDirectory, nameDream2, processedFrame - 1)):
        print("{}{}/img_{}.jpg".format(dreamsDirectory, nameDream2, processedFrame - 1))
        # Show last image for 2 seconds.
        if "img_0.jpg" in "{}{}/img_{}.jpg".format(dreamsDirectory, nameDream2, processedFrame - 1):
            for i in range(0, 2 * fps):
                output.write(cv2.imread("{}{}/img_{}.jpg".format(dreamsDirectory, nameDream2, processedFrame - 1)))
        output.write(cv2.imread("{}{}/img_{}.jpg".format(dreamsDirectory, nameDream2, processedFrame - 1)))
        processedFrame -= 1

    # Create video.
    output.release()
