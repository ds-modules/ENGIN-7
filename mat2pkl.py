# Reference: https://gist.github.com/Nixonite/bc2f69b0c4430211bcad
# A simple script to convert mat files into a more python friendly format

import scipy.io
import numpy as np
import sys
import os
import os.path
import pandas as pd
import csv
import pickle

cwd = os.getcwd()

print(cwd)

for root, dirs, files in os.walk(cwd):
	for file in files:
		if file.endswith('.mat'):
			# print(root, file)
			old_path = os.path.join(root, file)

			print("loading:", old_path)

			new_path = old_path[:-4] + ".pkl"

			print("saving to:", new_path)

			data = scipy.io.loadmat(old_path)

			print("type before saving:", type(data))

			for key in list(data.keys()):
				if "_" == key[0]:
					del data[key]

			for k, v in data.items():
				print("found data:", k, v.shape)

			with open(new_path, 'wb') as f:
				pickle.dump(data, f)

			with open(new_path, 'rb') as f:
				data = pickle.load(f)

			for k, v in data.items():
				print("pkl data, should match above:", k, v.shape)

			print("type after saving:", type(data))
			print()

			# mat = {k:v for k, v in data.items() if k[0] != '_'}
			# data = pd.DataFrame({k: pd.Series(v[0]) for k, v in mat.items()})
			# data.to_csv(new_path)
