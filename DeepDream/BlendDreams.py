import PIL.Image
import os
from shutil import copy2
import math
from scipy.misc import imresize
from deepdreamer import load_image
import numpy


def BlendDreams(blendDirectory, fps, dreamLength, nameDream1, nameDream2, 
               dreamsDirectory, blendLength, trimPercent):

    # Create new folder for the blend images.
    blendName = "{}{}_TO_{}".format(blendDirectory, nameDream1, nameDream2)
    os.mkdir(blendName)

    # Copy last image of the two dreams.
    copy2("{}{}/img_{}.jpg".format(dreamsDirectory, nameDream1, fps * dreamLength)
          , "{}/img_0.jpg".format(blendName))
    copy2("{}{}/img_{}.jpg".format(dreamsDirectory, nameDream2, fps * dreamLength)
          , "{}/img_9999.jpg".format(blendName))

    # Open the two images.
    imageOld = PIL.Image.open("{}/img_0.jpg".format(blendName))
    imageNew = PIL.Image.open("{}/img_9999.jpg".format(blendName))

    # Calculate rescale factor.
    xSize, ySize = imageOld.size
    xTrim = xSize * trimPercent / 100
    yTrim = ySize * trimPercent / 100

    # Stepwise transition between the two images.
    for i in range(0, blendLength * fps):
        # Blend two images and save the result.
        imageIntermediate = PIL.Image.blend(imageOld, imageNew, i/(blendLength*fps))
        imageIntermediate.save("{}/img_{}.jpg".format(blendName, i + 1))

        # Reload the image and zoom in.
        xTrim = xTrim + (xSize * trimPercent / 100) * -((i - blendLength * fps / 2) / (blendLength * fps / 2))
        yTrim = yTrim + (ySize * trimPercent / 100) * -((i - blendLength * fps / 2) / (blendLength * fps / 2))
        xTrimRounded = round(xTrim)
        yTrimRounded = round(yTrim)
        imageIntermediate = load_image("{}/img_{}.jpg".format(blendName, i + 1))
        imageIntermediate = imageIntermediate[yTrimRounded:ySize - yTrimRounded, xTrimRounded:xSize - xTrimRounded]
        imageIntermediate = imresize(imageIntermediate, (ySize, xSize), "nearest")

        # Save the final image.
        imageIntermediate = numpy.clip(imageIntermediate, 0.0, 255.0)
        imageIntermediate = imageIntermediate.astype(numpy.uint8)
        result = PIL.Image.fromarray(imageIntermediate, mode="RGB")
        result.save("{}/img_{}.jpg".format(blendName, i + 1))
