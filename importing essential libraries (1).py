import os
import zipfile
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tqdm import tqdm_notebook
from tensorflow.keras.preprocessing.image import ImageDataGenerator,load_img,img_to_array,array_to_img
%matplotlib inline
from scipy.stats import norm
import tensorflow.keras.backend as K
from tensorflow.keras.layers import Dense,Layer,Lambda,Add,Multiply,Input,Conv2D,MaxPool2D,Flatten,Conv2DTranspose,Reshape,Dropout,GlobalAveragePooling2D,GaussianNoise
from tensorflow.keras.models import Sequential,Model
from tensorflow.keras.utils import plot_model
from PIL import Image
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.losses import mse
import pandas as pd
import shutil
from skimage.filters import threshold_local
from scipy.fftpack import fft2, ifft2, fftshift
from matplotlib.animation import FuncAnimation
from IPython.display import HTML
import torch
import torch.nn as nn
from torch.utils.data import DataLoader