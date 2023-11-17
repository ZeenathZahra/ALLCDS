import os
import tensorflow
from tensorflow import keras

class Prata():
  def __init__(self,batch_size,img_height,img_width):
    self.batch_size=batch_size
    self.img_height=img_height
    self.img_width=img_width

  def load_data(self,path):
    train_ds= tensorflow.keras.utils.image_dataset_from_directory(
        path,
        seed=123,
        image_size=(self.img_height, self.img_width),
        batch_size=self.batch_size)
    AUTOTUNE = tensorflow.data.AUTOTUNE
    return train_ds.cache().prefetch(buffer_size=AUTOTUNE)


class Uzta():
  def __init__(self,path):
    self.path=path

  def unzip(self):
    zipfile.ZipFile(self.path,'r').extractall()

class Prometheus():
  def __init__(self,model_dir):
    self.model_dir=model_dir

  def infer(self,dataset):
    model = tensorflow.keras.models.load_model(self.model_dir)
    return "HEM" if model.predict(dataset)[0][0]>0.5 else "ALL"



