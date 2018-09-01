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
dreamDirectory = "Application/Dreams/"  # string - Relative path to the input file folder.
layers = [6, 10, 3]                     # List<int> - List of layers the dream should loop through.
iterations = 1                          # int - Number of optimization iterations.
stepSize = 0.5                          # double (/float!?) - Scale for each step of gradient descent.
rescaleFactor = 0.6                     # double - Downscaling factor for the image.
repeats = 5                             # int - Number of image downscales.
blend = 0.2                             # double - Factor for blending the original and processed images.

"""
### Create a dream image. ###
# Settings
pictureName = "IMG-20170212-WA0010.jpg"                 # string - File name of the input image.
pictureInputDirectory = "Application/PicturesInput/"    # string - Relative path to the input folder.
pictureOutputDirectory = "Application/PicturesOutput/"  # string - Relative path to the output folder.

DreamImage.DreamImage(pictureInputDirectory, layers, iterations, stepSize, rescaleFactor, 
                      repeats, blend, pictureName, pictureOutputDirectory)
"""

### Create a dream video. ###
# Settings
fps = 20                                        # int - Frames per second of the video [images/s].
dreamImage1 = "Squirel1920x1080"                # string - Folder name for the dream images.
dreamImage2 = "LightTree1920x1080"              # string - Folder name for the dream images.
changeLayerAfterSec = 5                         # int - Time befor switching to the next layer [s].
dreamLength = len(layers) * changeLayerAfterSec # int - Duration of the dream [s].
trimPercent = 0.25                              # double - Factor to trim the image [%].
blendDirectory = "Application/Blend/"           # string - Relative path to the blend folder. 
blendLength = 3                                 # int - Duration of the blend effect inbetween two dreams [s].
videoOutputDirectory = "Application/Videos/"    # string - Relative path to the video folder.

DreamFrames.DreamFrames(dreamDirectory, layers, iterations, stepSize, rescaleFactor, repeats, 
                        blend, fps, dreamImage1, dreamLength, changeLayerAfterSec, trimPercent)
DreamFrames.DreamFrames(dreamDirectory, layers, iterations, stepSize, rescaleFactor, repeats, 
                        blend, fps, dreamImage2, dreamLength, changeLayerAfterSec, trimPercent)
BlendDreams.BlendDreams(blendDirectory, fps, dreamLength, dreamImage1, dreamImage2, 
                      dreamDirectory, blendLength, trimPercent)
CreateVideo.CreateVideo(videoOutputDirectory, fps, dreamImage1, dreamImage2, 
                        dreamDirectory, blendDirectory)

print("Finished successfully =)")
