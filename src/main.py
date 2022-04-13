import sys
from train import trainAgent
from functions import *
import parameters

stock_name = parameters.STOCK_NAME
window_size = parameters.WINDOW_SIZE
episode_count = parameters.EPOCHS

if len(sys.argv) > 2:
    stock_name, window_size, episode_count = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
else:
	print("Usage: python main.py [stock] [window] [episodes]")
	print("Using default paramters")

trainAgent(stock_name, window_size, episode_count)