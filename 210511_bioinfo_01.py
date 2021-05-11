
import re
import sys

DICT = {}

with open(sys.argv[1],'r') as input:
    while True:
        line = input.readline()
        if line == '':
            break
        line_list = re.split(',',line.rstrip())
        line_list2 = re.split('\s',line_list[1])

        for element in line_list2:
            DICT[element] = line_list[0]

with open(sys.argv[2],'r') as input:
    while True:
        line = input.readline()
        if line == '':
            break

        line_list = re.split(',',line.rstrip())

        if line_list[3] in DICT.keys():
            print(line,end='')




        
