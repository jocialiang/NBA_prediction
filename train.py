# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 15:07:12 2018

@author: jocia.liang
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from keras.models import Sequential 
from keras.layers.core import Dense 

df_v = pd.read_csv('away_feature_2016.csv')
df_h = pd.read_csv('home_feature_2016.csv')
df_v_x =  df_v.drop(["date", "name"], axis=1)
df_h_x = df_h.drop(["win", "date", "name"], axis=1)
data_x = np.array(df_h_x - df_v_x)
data_y = np.array(df_h['win'])
print(data_x.shape, data_y.shape)

train_x, test_x, train_y, test_y = \
    train_test_split(data_x, data_y, test_size=0.0, random_state=42)

model = Sequential() 
model.add(Dense(5, input_dim=train_x.shape[1], activation='relu'))
#model.add(Dense(3, activation='relu')) 
#model.add(Dense(2, activation='relu'))
model.add(Dense(1, activation='sigmoid')) 
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.summary()

model.fit(train_x, train_y, batch_size=16, epochs=100, validation_split=0.2)
#score = model.evaluate(test_x, test_y)
#print(score[1])
#model.save('nba_model_2016.h5')

