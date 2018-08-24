from deepdreamer import model, load_image, recursive_optimize
import numpy as np
import PIL.Image


def DreamImage(fileDirectory, layers, iterations, stepSize, rescaleFactor, repeats, blend, pictureName, outputDirectory):
    filePath = fileDirectory + pictureName
    baseImage = load_image(filename='{}'.format(filePath))

    for layer in layers:
        try:
            img_result = recursive_optimize(layer_tensor=model.layer_tensors[layer]
                                            , image=baseImage
                                            , num_iterations=iterations
                                            , step_size=stepSize
                                            , rescale_factor=rescaleFactor
                                            , num_repeats=repeats
                                            , blend=blend)

            img_result = np.clip(img_result, 0.0, 255.0)
            img_result = img_result.astype(np.uint8)
            result = PIL.Image.fromarray(img_result, mode='RGB')
            result.save("{}Layer{}_Iter{}_Step{}_Rescale{}_Repeats{}_Blend{}.jpg".format(outputDirectory, layer, iterations, stepSize, rescaleFactor, repeats, blend))
        except Exception as ex:
            print(ex)
