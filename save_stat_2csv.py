# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 21:01:21 2018

@author: jocia.liang
"""

import os
import json
import pandas as pd
import argparse

parser = argparse.ArgumentParser(description='extract game stats to csv files')
parser.add_argument('--save2dir', default='game_detail/', help='save parsing file to this director')
args = parser.parse_args()

dirs = args.save2dir
away_dict, home_dict = {}, {}
game_dict = {}
feature_list = ['fga', 'fgm', 'tpa', 'tpm', 'fta', 'ftm', 'oreb', \
                'dreb', 'reb', 'ast', 'stl', 'blk', 'pf', 'tov', \
                'fbpts', 'fbptsa', 'fbptsm', 'pip', 'pipa', 'pipm', \
                'ble', 'bpts', 'tf', 'scp']

for file in os.listdir(dirs):
#for file in os.listdir(dirs):
    with open(dirs+file, 'r') as f:
        data = json.load(f)
        date = data['g']['gdte']
        vls, hls = data['g']['vls'], data['g']['hls']
        vn, hn = vls['ta'], hls['ta']
        vs, hs = int(vls['s']), int(hls['s'])
        w = 1 if hs > vs else 0
        vsts, hsts = vls['tstsg'], hls['tstsg']
        
        v_dict, h_dict = {}, {}
#        temp_dict = {}
#        temp_dict['home'] = hn
        v_dict['date'], h_dict['date'] = date, date
        v_dict['name'], h_dict['name'] = vn, hn
        h_dict['win'] = w
#        temp_dict['date'] = date
#        temp_dict['away'] = vn
#        temp_dict['win'] = w
        
        for key in vsts.keys():
#        for key in feature_list:
            v_dict[key], h_dict[key] = vsts[key], hsts[key]
#            temp_dict[key] = hsts[key] - vsts[key]
        
        for K,V in v_dict.items():
            if K in away_dict.keys():
                away_dict[K] = away_dict[K] + [V]
            else:
                away_dict[K] = [V]
                
        for K,V in h_dict.items():
            if K in home_dict.keys():
                home_dict[K] = home_dict[K] + [V]
            else:
                home_dict[K] = [V]
        
#        for K,V in temp_dict.items():
#            if K in game_dict.keys():
#                game_dict[K] = game_dict[K] + [V]
#            else:
#                game_dict[K] = [V]

df_v = pd.DataFrame.from_dict(away_dict) 
df_h = pd.DataFrame.from_dict(home_dict) 
#df_v.to_csv("away_feature.csv", index=False)
#df_h.to_csv("home_feature.csv", index=False)
df_v.to_csv("away_feature_2016.csv", index=False)
df_h.to_csv("home_feature_2016.csv", index=False)
#df = pd.DataFrame.from_dict(game_dict)
#df.to_csv("game_feature.csv", index = False)
#df.to_csv("game_feature_2016.csv", index = False)
            
            