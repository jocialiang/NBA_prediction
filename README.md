# NBA_prediction
parsing NBA stats, cleaning data and saving data as .csv files, creating tensorflow model and training, predicting new games.
## Usage
1. crawling NBA stats from website and saving files
python Game_detail_parser.py --save2dir 'game_detail/' --yearStart 2017 --yearEnd 2018 --idxStart 1 --idxEnd 1231
2. cleaning data
python save_stat_2csv.py --save2dir 'game_detail/'
3. creating model and training
python train.py
4. predicting
python predict.py

