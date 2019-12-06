# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 15:55:12 2018

@author: jocia.liang
"""

import pandas as pd
from keras.models import Sequential, load_model 
#from keras.layers.core import Dense 
import numpy as np
import math
import matplotlib.pyplot as plt

game_4_11 = [('BKN','BOS',0), ('NYK','CLE',0), ('TOR','MIA',0), ('WAS','ORL',0),\
             ('MIL','PHI',0), ('DET','CHI',0), ('DEN','MIN',0), ('SAS','NOP',0),\
             ('MEM','OKC',0), ('LAL','LAC',0), ('UTA','POR',0), ('HOU','SAC',0)]
game_4_12 = [('IND','CLE',0), ('NOP','POR',0)]
game = []
game = game_4_12

#df_v = pd.read_csv('away_feature_2016.csv')
#df_h = pd.read_csv('home_feature_2016.csv')
#df_h = df_h.drop(["win"], axis=1)
df = pd.read_csv('game_feature_2016.csv')
df = df.drop(['win'], axis=1)
model = load_model('nba_model_2016.h5')
#c_p = []
#vote_sum = [0]*len(game)


#for comp in range(3,16):
#    c_p_sum = []
#    vote = []
#    for away, home, label in game:
##        data_away = df_v[(df_v['name']==away)].sort_values(by='date', \
##                       ascending=False)[:comp].mean()
##        data_home = df_h[(df_h['name']==home)].sort_values(by='date', \
##                       ascending=False)[:comp].mean()
#        data_away = df[(df['away']==away)].sort_values(by='date', \
#                       ascending=False)[:comp].mean()
#        data_home = df[(df['home']==home)].sort_values(by='date', \
#                       ascending=False)[:comp].mean()
##        x = np.array(data_home - data_away)
#        x = np.array(data_home + data_away)
#        result = model.predict_classes(x[np.newaxis,:], verbose=0)[0][0]
#        prob = model.predict(x[np.newaxis,:], verbose=0)[0][0]
#        print(away, home, result, prob)
#        
#        vote.append(result)
#        
#        c_p_i = -label*math.log(prob+1.0e-100)-(1-label)*math.log(1.0-prob+1.0e-100)
#        c_p_sum.append(c_p_i)
#    print(vote)
#    c_p_avg = sum(c_p_sum)/len(c_p_sum)
#    c_p.append(c_p_avg)
#    print(comp, c_p_avg)
#    
#    vote_sum = [sum(x) for x in zip(vote, vote_sum)]
#print(vote_sum)
#plt.plot(c_p)
    
h = {"fga":88,"fgm":43,"tpa":36,"tpm":11,"fta":34,"ftm":23,"oreb":7,"dreb":36,"reb":43,"ast":25,"stl":5,"blk":2,"pf":29,"tov":11,"fbpts":14,"fbptsa":14,"fbptsm":6,"pip":62,"pipa":44,"pipm":31,"ble":7,"bpts":35,"tf":1,"scp":10,"tmreb":13,"tmtov":0,"potov":9}
v = {"fga":83,"fgm":37,"tpa":34,"tpm":17,"fta":38,"ftm":32,"oreb":8,"dreb":36,"reb":44,"ast":24,"stl":6,"blk":5,"pf":27,"tov":7,"fbpts":23,"fbptsa":13,"fbptsm":8,"pip":34,"pipa":33,"pipm":17,"ble":13,"bpts":36,"tf":1,"scp":10,"tmreb":8,"tmtov":1,"potov":17}
x = [h[_] - v[_] for _ in sorted(h.keys())]
x= np.array(x)
result = model.predict_classes(x[np.newaxis,:], verbose=0)[0][0]
prob = model.predict(x[np.newaxis,:], verbose=0)[0][0]
print(result, prob)