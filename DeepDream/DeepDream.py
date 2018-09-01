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
import BlendDreams
import CreateVideo

# general settings
dreamDirectory = "Application/Dreams/"
layers = [6, 10, 3]
iterations = 1
stepSize = 1
rescaleFactor = 0.6
repeats = 5
blend = 0.2

### Create a dream image.
# Settings
pictureName = "IMG-20170212-WA0010.jpg"
pictureInputDirectory = "Application/PicturesInput/"
pictureOutputDirectory = "Application/PicturesOutput/"

#DreamImage.DreamImage(pictureInputDirectory, layers, iterations, stepSize, rescaleFactor, 
#                      repeats, blend, pictureName, pictureOutputDirectory)


### Create a dream video.
# Settings
fps = 20
dreamImage1 = "Baumstaemme1920x1080"
dreamImage2 = "GreenTree1920x1080"
changeLayerAfterSec = 1
dreamLength = len(layers) * changeLayerAfterSec
trimPercent = 0.3
blendDirectory = "Application/Blend/"
blendLength = 2
videoOutputDirectory = "Application/Videos/"
picturesFolder = ""

#DreamFrames.DreamFrames(dreamDirectory, layers, iterations, stepSize, rescaleFactor, repeats, 
#                        blend, fps, dreamImage1, dreamLength, changeLayerAfterSec, trimPercent)
#DreamFrames.DreamFrames(dreamDirectory, layers, iterations, stepSize, rescaleFactor, repeats, 
#                        blend, fps, dreamImage2, dreamLength, changeLayerAfterSec, trimPercent)
BlendDreams.BlendDreams(blendDirectory, fps, dreamLength, dreamImage1, dreamImage2, 
                      dreamDirectory, blendLength, trimPercent)
#CreateVideo.CreateVideo(videoOutputDirectory, fps, dreamImage1, dreamImage2, 
#                        dreamDirectory, blendDirectory)

print("=)")
