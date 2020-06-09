
#head_10000.samを読み込んで、バーコード部分を抽出し、output.txtに出力します。

import re

output = open('output.txt','w')

with open('head_10000.sam','r') as input:
	while True:
		line = input.readline()
		if line == '':
			break
		
		line_array = re.split('[\s\t]+',line)
			
		for x in line_array:
			if x.startswith('CB'):
				array_CB = re.split(':',x)
				print(array_CB[2],file=output)
		
output.close()