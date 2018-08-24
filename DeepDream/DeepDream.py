"""
layer_tensors[1]:   wavy _____
layer_tensors[2]:   lines ++___
layer_tensors[3]:   boxes, circles +++++
layer_tensors[4]:   eyes, circles _____
layer_tensors[5]:   furry eyes +____
layer_tensors[6]:   dogs, animal legs, faces +++__
layer_tensors[7]:   legs, faces, reptilian eyes _____
layer_tensors[8]:   snake heads, creepy faces, reptilians +____
layer_tensors[9]:   snake heads, faces, fish +____
layer_tensors[10]:  birds, lizards +++__

Layer 3: 20 iterations, 0.5 rescale, and 8 repeats is decent start
Layer 10: 40 iterations and 25 repeats is good.
"""

import DreamImage
import DreamFrames
import MindChange
import CreateVideo

# general
fileDirectory = "Application/Dreams/"
layers = [6, 10, 3]
iterations = 1  # how clear is the dream vs original image
stepSize = 1
rescaleFactor = 0.6
repeats = 5 # How many "passes" over the data. More passes, the more granular the gradients will be.
blend = 0.2
# images
pictureName = "IMG-20170212-WA0010.jpg"
outputDirectory = "Application/PicturesOutput/"
# video
fps = 20
# frames
dreamName = "Snowman1280x720"
changeLayerAfterSec = 1
dreamLength = len(layers) * changeLayerAfterSec
trimPercent = 0.3
# mind change
mindChangeName = "MindChangeTest"
mindChangeLength = 2
# create video
picturesFolder = ""

"""
DreamFrames.DreamFrames("Application/Dreams/", layers, iterations, stepSize, rescaleFactor, repeats, blend
                        , fps, "Baumstaemme1920x1080", dreamLength, changeLayerAfterSec, trimPercent)

DreamFrames.DreamFrames("Application/Dreams/", layers, iterations, stepSize, rescaleFactor, repeats, blend
                        , fps, "GreenTree1920x1080", dreamLength, changeLayerAfterSec, trimPercent)

MindChange.MindChange("Application/MindChange/", fps, dreamLength, "Baumstaemme1920x1080", "GreenTree1920x1080"
                      , "Application/Dreams/", mindChangeLength, trimPercent)
"""
CreateVideo.CreateVideo("Application/Videos/", fps, "Snowman1280x720", "IR1280x720"
                        , "Application/Dreams/", "Application/MindChange/")

print("=)")
