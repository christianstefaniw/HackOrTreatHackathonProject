from keras.models import load_model
from keras.preprocessing import image
import matplotlib.pyplot as plt
import numpy as np


def load_image(img_path, show=False):

    img = image.load_img(img_path, target_size=(400, 280))
    img_tensor = image.img_to_array(img)
    img_tensor = np.expand_dims(img_tensor, axis=0)
    img_tensor /= 255.

    if show:
        plt.imshow(img_tensor[0])
        plt.axis('off')
        plt.show()

    return img_tensor


def run_test(file):
    model = load_model("model.h5")

    new_image = load_image(file)

    pred = model.predict(new_image)
    val = float(pred[0])
    return "Your costume is {}/10 scary".format(int(round((val*10), 0)))
