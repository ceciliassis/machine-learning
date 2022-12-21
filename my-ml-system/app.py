import pickle
import random

from flask import Flask
from sklearn import datasets


app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<p>Hello World</p>'


@app.route('/predict')
def predict():
    digits = datasets.load_digits()
    image = random.randrange(len(digits.images))
    image_data = digits.images[image].reshape(1, -1)
    image_target = digits.target[image]
    model = pickle.load(open('model/sklearn-model/clf.model', 'rb'))

    return f'Predição: {model.predict(image_data)[0]}, Classe: {image_target}'
