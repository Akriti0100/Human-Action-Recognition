import os
import numpy as np
from .utils import Videos
from keras.models import model_from_json


def prediction(path):

    """ Function to recognize the action executed using the CNN-Model """
    print("hiii")
    class_labels = ['boxing', 'handclapping', 'handwaving', 'jogging', 'running', 'walking']
    reader = Videos(target_size=(128, 128), 
                    to_gray=True, 
                    max_frames=50, 
                    extract_frames='first', 
                    normalize_pixels=(-1, 1))
    json_file = open(os.getcwd() + '\\actions\\' + 'model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    loaded_model.load_weights(os.getcwd() + '\\actions\\' + 'Model.weights.best.hdf5')
    x_pred = reader.read_videos([path])
    y_proba = loaded_model.predict(x_pred)
    y_label = class_labels[np.argmax(y_proba)]

    print(y_proba)

    return y_label
