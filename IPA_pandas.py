
import os
import sys
import pandas as pd

DF = pd.read_table('Cdh2.txt',header=1)
#print(df.columns.values.tolist())

DF_MOUSE = DF[DF['Entrez Gene ID for Mouse'].str.contains('[0-9]+',na=False)]

SYMBOLS = DF_MOUSE['Symbol']

NCAD_IPA_DICT = {}

for symbol in SYMBOLS:
	NCAD_IPA_DICT[symbol] = 0

DIRNAME = 'IPA_files'

FILES_LIST = os.listdir(DIRNAME)

for a_file in FILES_LIST:
	if a_file.endswith('txt'):
		filename = DIRNAME + '/' + a_file
		df = pd.read_table(filename,header=1)
		
		symbols = df['Symbol']
		
		for symbol in symbols:
			if symbol in NCAD_IPA_DICT.keys():
				NCAD_IPA_DICT[symbol] += 1

for key in NCAD_IPA_DICT.keys():
	#if NCAD_IPA_DICT[key] >= 4:
	if NCAD_IPA_DICT[key] == 3:
		print(key)