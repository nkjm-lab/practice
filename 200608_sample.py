
#head_10000.samを読み込んで、バーコード部分を抽出し、output.txtに出力します。

import re

output = open('output.txt','w')

with open('head_10000.sam','r') as input:
	while True:
		line = input.readline()
		if line == '':
			break
		
		line_list = re.split('[\s\t]+',line)
			
		for element in line_list:
			if element.startswith('CB'):
				CB_list = re.split(':', element)
				print(CB_list[2],file=output)
		
output.close()