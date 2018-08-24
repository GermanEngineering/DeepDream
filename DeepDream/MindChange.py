import PIL.Image
import os
from shutil import copy2
import math
from scipy.misc import imresize
from deepdreamer import load_image
import numpy


def MindChange(fileDirectory, fps, dreamLength, nameDream1, nameDream2, dreamsDirectory, mindChangeLength, trimPercent):
    mindChangeName = "{}{}_TO_{}".format(fileDirectory, nameDream1, nameDream2)
    os.mkdir(mindChangeName)
    copy2("{}{}/img_{}.jpg".format(dreamsDirectory, nameDream1, fps * dreamLength)
          , "{}/img_0.jpg".format(mindChangeName))
    copy2("{}{}/img_{}.jpg".format(dreamsDirectory, nameDream2, fps * dreamLength)
          , "{}/img_9999.jpg".format(mindChangeName))

    imageOld = PIL.Image.open("{}/img_0.jpg".format(mindChangeName))
    imageNew = PIL.Image.open("{}/img_9999.jpg".format(mindChangeName))

    xSize, ySize = imageOld.size
    xTrim = xSize * trimPercent / 100
    yTrim = ySize * trimPercent / 100

    for i in range(0, mindChangeLength * fps):
        imageIntermediate = PIL.Image.blend(imageOld, imageNew, i/(mindChangeLength*fps))
        imageIntermediate.save("{}/img_{}.jpg".format(mindChangeName, i + 1))

        xTrim = xTrim + (xSize * trimPercent / 100) * -((i - mindChangeLength * fps / 2) / (mindChangeLength * fps / 2))
        yTrim = yTrim + (ySize * trimPercent / 100) * -((i - mindChangeLength * fps / 2) / (mindChangeLength * fps / 2))
        xTrimRounded = round(xTrim)
        yTrimRounded = round(yTrim)
        imageIntermediate = load_image("{}/img_{}.jpg".format(mindChangeName, i + 1))
        imageIntermediate = imageIntermediate[yTrimRounded:ySize - yTrimRounded, xTrimRounded:xSize - xTrimRounded]
        imageIntermediate = imresize(imageIntermediate, (ySize, xSize), "nearest")

        imageIntermediate = numpy.clip(imageIntermediate, 0.0, 255.0)
        imageIntermediate = imageIntermediate.astype(numpy.uint8)

        result = PIL.Image.fromarray(imageIntermediate, mode="RGB")
        result.save("{}/img_{}.jpg".format(mindChangeName, i + 1))
