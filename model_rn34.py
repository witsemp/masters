import tensorflow as tf
from tensorflow import keras
model = keras.applications.resnet50.ResNet50(weights='imagenet')
