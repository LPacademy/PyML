from keras.applications.vgg16 import VGG16, preprocess_input, decode_predictions
from keras.preprocessing import image
import numpy as np
import sys
import json
from json_encoders import MyEncoder


"""
ImageNetで学習済みのVGG16モデルを使って入力画像のクラスを予測する]
Original code: https://github.com/aidiary/keras-examples/blob/master/vgg16/test_vgg16/test_vgg16.py
"""
def predict(filename):
    model = VGG16(weights='imagenet')
    img = image.load_img(filename, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    preds = model.predict(preprocess_input(x))
    results = decode_predictions(preds, top=5)[0]
    return results
