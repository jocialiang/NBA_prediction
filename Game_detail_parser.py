# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 19:25:36 2017

@author: jocia.liang
"""

import requests
import json
import os
import argparse

parser = argparse.ArgumentParser(description='NBA game stats parsing')
parser.add_argument('--save2dir', default='game_detail/', help='save parsing file to this director')
parser.add_argument('--yearStart', default=2017, help='starting season')
parser.add_argument('--yearEnd', default=2018, help='endding season')
parser.add_argument('--idxStart', default=1, help='start at a one game of a season')
parser.add_argument('--idxEnd', default=1231, help='end at one game of a season')
args = parser.parse_args()

def game_parser(dirs, yearStart, yearEnd, idxStart, idxEnd):
    dirs = dirs
    for year in range(yearStart, yearEnd):
        for game_idx in range(idxStart, idxEnd):
            game_idx = "%05d"%(game_idx)
            filename = str(year)+game_idx
            try:
                if not os.path.exists(dirs+filename):
                    url = "https://data.nba.com/data/10s/v2015/json/mobile_teams/nba/"\
                          + str(year) + "/scores/gamedetail/002" + str(year%2000)\
                          + game_idx + "_gamedetail.json"
                          
                    res = requests.get(url)             
                    data = json.loads(res.text)
                    
                    if data['g']['stt'] == 'Final':
                        with open(dirs+filename, "w") as f:
                            json.dump(data, f)
                        print("save "+filename)
                    else:
                        print("%d %s game is not finished"%(year, game_idx))
                        return
                else:
                    print(filename+" exists")
            except:
                print("%d %s %d error"%(year, game_idx, res.status_code))
                return
                
if __name__ == '__main__':
    game_parser(args.dirs, args.yearStart, args.yearEnd, args.idxStart, args.idxEnd)