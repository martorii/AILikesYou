import faces as faces
import ddbb as ddbb
import numpy as np
import matplotlib.pyplot as plt
import functions as f
import NN as nn
import tensorflow as tf
from tensorflow import keras
import os
from keras.models import model_from_json

rowCount_query = "SELECT COUNT(1) as nrows FROM Pictures"
nrows = ddbb.select(rowCount_query)["nrows"].iloc[0]
rowNumber=1
batch= 1000
epoch_number = 5
batch_number = int(np.round(nrows/batch, 0) + 1)
query = "SELECT pictureId, full_path, Age, face_x1, face_x2, face_y1, face_y2 FROM Pictures WHERE valid=1"
best_acc = 50
model = nn.createModel()

for epoch in range(1, epoch_number):
    for iter in range(1, batch_number):
        X_train, Y_train, X_test, Y_test = f.getDataToTrain(query, nrows, 0.8, batch, iter)
        model.fit(X_train, Y_train, epochs=10)
        test_loss, test_acc = model.evaluate(X_test, Y_test)
        print('Test accuracy:', test_acc)
        if test_acc > best_acc:
            best_acc = test_acc
            model_json = model.to_json()
            with open(str(best_acc) + "_age.json", "w") as json_file:
                json_file.write(model_json)
            # serialize weights to HDF5
            model.save_weights(str(best_acc) + "_age.h5")
    


