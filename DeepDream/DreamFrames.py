from deepdreamer import model, load_image, recursive_optimize
import numpy as np
import PIL.Image
from scipy.misc import imresize
import os
import numpy
import random
import math


def DreamFrames(fileDirectory, layers, iterations, stepSize, rescaleFactor, repeats, blend
                , fps, dreamName, dreamLength, changeLayerAfterSec, trimPercent):
    redCorrection = int(random.choice("23"))
    greenCorrection = int(random.choice("23"))
    blueCorrection = int(random.choice("23"))

    for i in range(0, dreamLength * fps):
        if not os.path.isfile("{}{}/img_{}.jpg".format(fileDirectory, dreamName, i + 1)):
            # load image
            img_result = load_image(filename="{}{}/img_{}.jpg".format(fileDirectory, dreamName, i))

            # get image size
            xSize = len(img_result[0])
            ySize = len(img_result)

            # zoom
            xTrim = math.ceil(xSize * trimPercent / 100)
            yTrim = math.ceil(ySize * trimPercent / 100)
            img_result = img_result[yTrim:ySize - yTrim - 9, xTrim:xSize - xTrim - 9]
            img_result = imresize(img_result, (ySize, xSize), "nearest")

            # adjust brightness
            upperBrightnessLevel = xSize*ySize*255*0.8
            lowerBrightnessLevel = xSize*ySize*255*0.2
            redSum = numpy.sum(img_result[:, :, 0])
            if redSum < lowerBrightnessLevel:
                redCorrection = int(random.choice("34"))
            elif redSum > upperBrightnessLevel:
                redCorrection = int(random.choice("12"))
            img_result[:, :, 0] += redCorrection
            greenSum = numpy.sum(img_result[:, :, 0])
            if greenSum < lowerBrightnessLevel:
                greenCorrection = int(random.choice("34"))
            elif greenSum > upperBrightnessLevel:
                greenCorrection = int(random.choice("12"))
            img_result[:, :, 1] += greenCorrection
            blueSum = numpy.sum(img_result[:, :, 0])
            if blueSum < lowerBrightnessLevel:
                blueCorrection = int(random.choice("34"))
            elif blueSum > upperBrightnessLevel:
                blueCorrection = int(random.choice("12"))
            img_result[:, :, 2] += blueCorrection
            img_result = np.clip(img_result, 0.0, 255.0)
            img_result = img_result.astype(np.uint8)

            # select layer
            framesPerLayer = fps * changeLayerAfterSec
            # automatically loop through layers 10..2
            # layer = int(11 - (math.ceil((i - math.floor(i/(9*framesPerLayer))*(9*framesPerLayer)) / framesPerLayer)))
            # cycle through layers list
            layer = layers[int(math.ceil(i - (math.floor(i/(framesPerLayer*len(layers)))) * (framesPerLayer*len(layers)))/framesPerLayer)]

            # select iterations
            iterations = int(min(21.0, layer * math.pi) + 2)

            img_result = recursive_optimize(layer_tensor=model.layer_tensors[layer],
                                            image=img_result,
                                            num_iterations=iterations,
                                            step_size=stepSize,
                                            rescale_factor=rescaleFactor,
                                            num_repeats=1,
                                            blend=blend)

            img_result = np.clip(img_result, 0.0, 255.0)
            img_result = img_result.astype(np.uint8)

            result = PIL.Image.fromarray(img_result, mode="RGB")
            print("{}{}/img_{}.jpg".format(fileDirectory, dreamName, i + 1))
            result.save("{}{}/img_{}.jpg".format(fileDirectory, dreamName, i + 1))
        else:
            print(i)
