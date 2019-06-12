import ddbb as ddbb
import faces as faces
import numpy as np
import pandas as pd

def getDataToTrain(b_query, nrows, ratio, batch, iter):
    folderPath = "/Users/Erik/Data/Programes/AILikeYou/Pictures/"
    rowNumber=1
    query = b_query + " LIMIT " + str(iter*batch) + ", " + str(batch)
    data = ddbb.select(query)
    for index, row in data.iterrows():
        age = row["Age"]
        picPath = folderPath + row["full_path"]
        check = faces.validFace(picPath)
        if check == False:
            continue
        # print(str(int(row["face_x1"])))
        # print(str(int(row["face_x2"])))
        # print(str(int(row["face_y1"])))
        # print(str(int(row["face_y2"])))
        # print(str(int(row["pictureId"])))
        img = faces.cropFace(picPath, int(row["face_x1"]), int(row["face_x2"]), int(row["face_y1"]), int(row["face_y2"]))
        img = img/255
        img = np.array(img)
        img = img.flatten()
        d = np.append(img, age)
        if rowNumber == 1:
            X = img
            Y = age
        else:
            X = np.vstack([X, img])
            Y = np.append(Y, age)
        rowNumber=rowNumber+1
    nrows = X.shape[0]
    index = round(nrows*ratio)
    
    X_train = X[1:index,:]
    Y_train = Y[1:index]
    X_test = X[index:, :]
    Y_test = Y[index:]
    return X_train, Y_train, X_test, Y_test

