import os

from flask import Flask, request, abort, jsonify
import tensorflow_hub as hub
from tensorflow import expand_dims
from tensorflow.keras.utils import load_img, img_to_array
from tensorflow.nn import softmax
from numpy import argmax, max
import yaml
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader

from utils import download_classes, download_file

config = yaml.load(open('config.yml', 'r'), Loader=Loader)
model_config = config['model']
model = hub.load(model_config['tensorflow']['module'])
classes = download_classes(model_config['tensorflow']['classes'])

app = Flask(__name__)


def load_image(img_link: str = ''):
    # download image
    img_path = download_file(url=img_link)

    # load img as PIL
    img = load_img(path=img_path, target_size=(299, 299))

    # transform PIL to tensor
    img_array = img_to_array(img)
    img_array = expand_dims(img_array, 0)

    os.remove(img_path)

    return img_array


@app.route('/')
def root():
    return '<p>Hello World</p>'


@app.errorhandler(400)
def bad_request(e):
    return jsonify(error=str(e)), 400


@app.errorhandler(500)
def internal_error(e):
    return jsonify(error=str(e)), 500


@app.route('/predict', methods=['GET'])
def predict():
    args = request.args
    img_link = args.get('image_link', default='')

    if not img_link:
        abort(400, description='Provide an `image_link`')

    image = load_image(img_link)

    pred = model(image, training=False)
    score = softmax(pred)

    class_prediction = classes[argmax(score)]
    model_score = round(max(score) * 100, 2)

    return {
        'model-prediction': class_prediction,
        'model-prediction-confidence-score': model_score
    }
