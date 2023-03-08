import tensorflow as tf
import tensorflow  imort keras
import tenseorflow.keras.layers import Dense, Embedding, Bidrectional, LSTM
from tensorflow.keras.datasets import imdb

num_words = 10000
maxlen = 100

(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=num_words)
