import numpy as np
import tensorflow as tf
import pyreadr
import pandas as pd
import keras
from keras.layers import Dense,Dropout,BatchNormalization
from keras.models import Sequential,Model
from keras.callbacks import ModelCheckpoint,EarlyStopping,ReduceLROnPlateau
from keras.optimizers import Adam
from keras.regularizers import l1
from sklearn.preprocessing import StandardScaler