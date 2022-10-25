import pandas as pd
import psycopg2
from keras.backend import reshape
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense
import matplotlib.pyplot as plt
import numpy as np


def neiron_lan(temperature, speed, humidity, pressure):
    con = psycopg2.connect(
        database="stoloto",
        user="postgres",
        password="1",
        host="127.0.0.1",
        port="5432"
    )
    df = pd.read_sql('SELECT factors.temperature, factors.speed, factors.humidity, factors.pressure, con_data.concentration from con_data inner join factors on con_data.date = factors.date',
                      con)
    dataset = df.values.astype(float)
    X = dataset[:, 0:4]
    Y = dataset[:, 4]
    X_train, X_val_and_test, Y_train, Y_val_and_test = train_test_split(X, Y, test_size=0.3)
    X_val, X_test, Y_val, Y_test = train_test_split(X_val_and_test, Y_val_and_test, test_size=0.5)
    model = Sequential([
        Dense(32, activation='relu', input_shape=(4,)),
        Dense(32, activation='relu'),
        Dense(1),
    ])
    model.compile(optimizer='adam',
                  loss='mse',
                  metrics=['mae'])

    hist = model.fit(X_train, Y_train,
                     batch_size=32, epochs=100,
                     validation_data=(X_val, Y_val))

    concentration = abs(model.predict(np.array([[temperature, speed, humidity, pressure]])))[0]
    return concentration[0]


#neiron_lan(-1, 1, 50, 754)
